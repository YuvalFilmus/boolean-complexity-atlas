#!/usr/bin/env python3
"""Generate the total-function core matrix from explicitly eligible recorded evidence.

This restricted exponent closure is not a general mathematical inference engine.
It never imports historical-table entries as proved bounds.
"""
import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CORE=['D','R0','R','C','RC','bs','s','lambda','QE','deg','Q','adeg']
AUX=['fbs','FC','QC','UC','UC1','UC0','UCmin']

def expr_value(e):
 if not isinstance(e,dict):return float(Fraction(str(e)))
 op=e['op']
 if op=='log_ratio':return math.log(expr_value(e['numerator']))/math.log(expr_value(e['denominator']))
 if op=='sqrt':return math.sqrt(expr_value(e['arg']))
 a,b=expr_value(e['left']),expr_value(e['right'])
 return {'add':lambda:a+b,'mul':lambda:a*b,'div':lambda:a/b}[op]()

def expr_text(e):
 if not isinstance(e,dict):return str(e)
 if e['op']=='log_ratio':return 'log('+expr_text(e['numerator'])+')/log('+expr_text(e['denominator'])+')'
 if e['op']=='sqrt':return 'sqrt('+expr_text(e['arg'])+')'
 return '('+expr_text(e['left'])+{'add':'+','mul':'*','div':'/'}[e['op']]+expr_text(e['right'])+')'

def eligible(c):
 s=c['scope']
 return (s['object_kind']=='decision_function' and s['totality'] in ['total','partial_or_total']
         and not s['classes'] and not s.get('assumptions') and not c.get('historical')
         and c.get('scalar_inference_allowed',True)
         and c['status'] not in ['secondary_checked','statement_checked_proof_pending','survey_checked'])

def upper_closure(d):
 nodes=CORE+AUX; U={};excluded=[]
 def put(a,b,p,ids,loss=False):
  if a not in nodes or b not in nodes or p<=0:return False
  candidate=dict(exponent=p,claim_ids=list(dict.fromkeys(ids)),endpoint_without_log=not loss)
  old=U.get((a,b))
  if old is None or (p,loss,len(candidate['claim_ids'])) < (old['exponent'],not old['endpoint_without_log'],len(old['claim_ids'])):
   U[a,b]=candidate;return True
  return False
 for a in nodes:put(a,a,Fraction(1),[])
 hyper=[]
 for c in d['claims']:
  if not eligible(c):continue
  if c['kind'] not in ['upper_bound','theta_bound','identity','multivariate_upper_bound']:continue
  # No input-length, undefined, or other parameter-dependent losses are erased.
  loss=c['loss']!='none'
  if loss and not (c['loss']=='explicit_log' and c.get('log_factor')=='log(2+R)'):
   excluded.append(c['id']);continue
  if c['kind']=='multivariate_upper_bound':
   if c['A'] in nodes and c.get('factors') and all(f['measure'] in nodes for f in c['factors']):hyper.append(c)
   continue
  if c['exponent'] is None:continue
  p=Fraction(str(c['exponent']));put(c['A'],c['B'],p,[c['id']],loss)
  if c['kind'] in ['identity','theta_bound'] and not loss:put(c['B'],c['A'],1/p,[c['id']])
 for iteration in range(100):
  changed=False
  for k in nodes:
   for a in nodes:
    for b in nodes:
     if (a,k) in U and (k,b) in U:
      x,y=U[a,k],U[k,b]
      changed=put(a,b,x['exponent']*y['exponent'],x['claim_ids']+y['claim_ids'],not(x['endpoint_without_log'] and y['endpoint_without_log'])) or changed
  for c in hyper:
   for b in nodes:
    if all((f['measure'],b) in U for f in c['factors']):
     terms=[(f,U[f['measure'],b]) for f in c['factors']]
     p=sum((Fraction(str(f['power']))*v['exponent'] for f,v in terms),Fraction(0))
     ids=[c['id']]+[id for f,v in terms for id in v['claim_ids']]
     changed=put(c['A'],b,p,ids,any(not v['endpoint_without_log'] for f,v in terms)) or changed
  if not changed:break
 else:raise ValueError('Exponent closure did not stabilize')
 return U,excluded

def build(d):
 U,excluded=upper_closure(d);hist=json.loads((ROOT/'data/historical-matrix-2021.json').read_text());H={(r['A'],r['B']):r for r in hist['cells']}
 sources={s['id']:s for s in d['sources']};claims={c['id']:c for c in d['claims']};seeds=[]
 for c in d['claims']:
  # Restricted-class witnesses are witnesses in the general total class, but never in arbitrary other subclasses.
  s=c['scope']
  if (c['kind']=='separation' and s['object_kind']=='decision_function' and s['totality']=='total'
      and c.get('exponent') is not None and not c.get('historical') and c.get('scalar_inference_allowed',True)):
   seeds.append(c)
 cells=[]
 for a in CORE:
  for b in CORE:
   lo=dict(exponent_expression=1,numeric_for_ranking=1.0,witness='parity-core',claim_ids=[],proof='All twelve core measures are Theta(n) on parity.')
   for c in seeds:
    x,y=U.get((c['A'],a)),U.get((b,c['B']))
    if x is None or y is None:continue
    divisor=x['exponent']*y['exponent'];e=c.get('exponent_expression',c['exponent'])
    v=expr_value(e)/float(divisor)
    ids=list(dict.fromkeys([c['id']]+x['claim_ids']+y['claim_ids']))
    if v>lo['numeric_for_ranking']+1e-10 or (abs(v-lo['numeric_for_ranking'])<1e-10 and len(ids)<len(lo['claim_ids'])):
     expression=e if divisor==1 else dict(op='div',left=e,right=str(divisor))
     lo=dict(exponent_expression=expression,numeric_for_ranking=v,witness=c['id'],claim_ids=ids,
       proof='Transfer the witness using A_witness<=O(A_target^u) and B_target<=O(B_witness^v); a target exponent below ell/(u*v) contradicts the witness. Logarithmic upper losses affect endpoint attainment, not this excluded-exponent argument.')
   up=U.get((a,b));assert up is not None,(a,b)
   assert lo['numeric_for_ranking']<=float(up['exponent'])+1e-9,(a,b,lo,up)
   ids=list(dict.fromkeys(lo['claim_ids']+up['claim_ids']));refs=[]
   for id in ids:
    c=claims[id]
    if c['source']!='definitions':refs.append(c['source'])
    refs.extend(c.get('proof_sources',[]))
   # Flatten derivation dependencies for publication caveats.
   todo=list(ids);seen=set()
   while todo:
    id=todo.pop()
    if id in seen:continue
    seen.add(id);c=claims[id]
    if c['source']!='definitions':refs.append(c['source'])
    todo.extend(c.get('depends_on',[]))
   statuses={r:sources[r].get('publication_status','see_bibliography') for r in sorted(set(refs))}
   cells.append(dict(A=a,B=b,lower=lo,upper=dict(exponent=str(up['exponent']),endpoint_without_log=up['endpoint_without_log'],claim_ids=up['claim_ids']),
      matched_recorded_exponents=abs(lo['numeric_for_ranking']-float(up['exponent']))<1e-9,
      source_publication_statuses=statuses,historical_2021=H.get((a,b)),globally_best_known_certified=False))
 return dict(scope='total Boolean decision functions, unrestricted class, fixed error, measure-specific zero-error conventions',order=CORE,cells=cells,
             inference_policy='Restricted scalar power closure and explicitly stored multivariate bounds; every witness retains provenance. Not a complete current-best literature certification.',excluded_loss_claims=excluded)

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--pair',nargs=2,metavar=('A','B'));args=parser.parse_args()
 d=json.loads((ROOT/'data/catalog.json').read_text());result=build(d)
 if args.pair:
  pair=next((c for c in result['cells'] if [c['A'],c['B']]==args.pair),None)
  if pair is None:parser.error('Pair must use two core measure IDs: '+', '.join(CORE))
  print(json.dumps(pair,ensure_ascii=False,indent=2));return
 (ROOT/'data/core-matrix.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 lines=['# Total-function core matrix','','Each entry is **recorded lower exponent / recorded upper exponent**. Rows are A, columns B for A=O(B^p). These are infimum-exponent bounds; matching endpoints do not assert constant-factor tightness. A † marks an upper bound whose endpoint still has a logarithmic loss.','','All 132 off-diagonal cells have source-linked support or an explicit derivation. This is complete grid coverage for these twelve measures, not exhaustive literature verification or coverage of all 134+ measures. The JSON stores claim IDs, exact lower-exponent expressions, publication caveats and historical entries. Repository-preprint evidence is included and remains labelled.','','| A \\ B | '+' | '.join(CORE)+' |','|---|'+'---|'*len(CORE)]
 for a in CORE:
  row=[]
  for c in result['cells']:
   if c['A']!=a:continue
   lo=c['lower'];v=lo['numeric_for_ranking'];lower=str(int(round(v))) if abs(v-round(v))<1e-9 else f'{v:.5f}…'
   row.append(lower+'/'+c['upper']['exponent']+('†' if not c['upper']['endpoint_without_log'] else ''))
  lines.append('| '+a+' | '+' | '.join(row)+' |')
 lines+=['','## Evidence for each ordered pair','']
 for c in result['cells']:
  if c['A']==c['B']:continue
  lines += ['### '+c['A']+' / '+c['B'],'', 'Lower: '+expr_text(c['lower']['exponent_expression'])+'; witness `'+c['lower']['witness']+'`; claims '+', '.join('`'+i+'`' for i in c['lower']['claim_ids'])+'.', '', 'Upper: '+c['upper']['exponent']+(' (endpoint without logarithmic loss).' if c['upper']['endpoint_without_log'] else ' (infimum bound; logarithmic endpoint loss retained).')+' Claims: '+', '.join('`'+i+'`' for i in c['upper']['claim_ids'])+'.','']
  if c['historical_2021']:
   h=c['historical_2021'];lines+=['2021 table: '+h['lower_label']+'/'+h['upper_label']+'; attributed there to '+h['attribution_label']+'. Historical rounded labels are not exact exponents.','']
 (ROOT/'docs/core-matrix.md').write_text('\n'.join(lines)+'\n')
 print('Generated 12×12 core matrix, 132 off-diagonal evidence records.')
if __name__=='__main__':main()
