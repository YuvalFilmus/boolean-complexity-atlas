#!/usr/bin/env python3
"""Promise-only scalar closure and explicit bounded-denominator witnesses.

Total-function upper bounds are never admitted. No matrix value is declared best known.
"""
import argparse,json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CORE=['D','R0','R','C','RC','bs','s','lambda','QE','deg','Q','adeg']
def eligible(c):
 s=c['scope']
 return (s['object_kind']=='decision_function' and s['totality'] in ['partial','partial_or_total'] and not s['classes'] and not s.get('assumptions') and c['kind'] in ['upper_bound','theta_bound','identity'] and c['exponent'] is not None and c['loss']=='none' and not c.get('input_length_factor') and not c.get('historical') and c.get('scalar_inference_allowed',True) and c['status'] not in ['secondary_checked','statement_checked_proof_pending','survey_checked'])
def build(d):
 nodes=CORE+['fbs','FC','QC'];U={(a,a):{'exponent':Fraction(1),'claim_ids':[]} for a in nodes}
 def put(a,b,e,ids):
  if a not in nodes or b not in nodes:return
  v={'exponent':e,'claim_ids':list(dict.fromkeys(ids))};old=U.get((a,b))
  if old is None or (e,len(v['claim_ids']))<(old['exponent'],len(old['claim_ids'])):U[a,b]=v
 for c in d['claims']:
  if not eligible(c):continue
  e=Fraction(str(c['exponent']));put(c['A'],c['B'],e,[c['id']])
  if c['kind'] in ['identity','theta_bound']:put(c['B'],c['A'],1/e,[c['id']])
 for k in nodes:
  for a in nodes:
   for b in nodes:
    if (a,k) in U and (k,b) in U:
     x,y=U[a,k],U[k,b];put(a,b,x['exponent']*y['exponent'],x['claim_ids']+y['claim_ids'])
 N={}
 for c in d['claims']:
  if c['kind']!='no_polynomial_bound' or c['A'] not in CORE or c['B'] not in CORE:continue
  s=c['scope']
  if s['object_kind']=='decision_function' and s['totality']=='partial':N.setdefault((c['A'],c['B']),[]).append(c['id'])
 cells=[]
 for a in CORE:
  for b in CORE:
   v=dict(A=a,B=b,status='unresolved_in_this_audit')
   if (a,b) in U:
    u=U[a,b];v.update(status='finite_upper_bound',upper={'exponent':str(u['exponent']),'claim_ids':u['claim_ids']})
    if u['exponent']==1:v['lower']={'exponent':'1','witness_id':d['matrix_baseline_witness']['id'],'source':d['matrix_baseline_witness']['source'],'note':'Total parity is included among arbitrary-promise functions.'}
    elif u['exponent']==2:v['lower']={'exponent':'2','witness_id':'promise-unit-OR','claim_ids':['partial-quadratic-'+a+'-'+b]}
    else:raise ValueError('No matching lower bound registered for '+a+'/'+b)
   if (a,b) in N:
    if (a,b) in U:raise ValueError(f'Contradictory finite / unbounded evidence: {a}/{b}')
    v.update(status='no_finite_power',claim_ids=N[a,b])
   cells.append(v)
 return dict(scope='Boolean decision functions on arbitrary promises; weak certificates; unrestricted promise polynomial degrees; R0 worst-case expected Las Vegas cost',convention='A=O(max(1,B)^p). A no_finite_power entry uses a growing numerator and bounded denominator, or an original-source superpolynomial separation.',certification='Evidence inventory, not a globally certified best-known table. Finite entries have matching lower exponents from parity or the zero-or-unit-vector promise. These are statements about power exponents, not optimal constants.',nodes=CORE,cells=cells)
def write(d):
 out=build(d);(ROOT/'data/partial-matrix.json').write_text(json.dumps(out,indent=2)+'\n');cs={(v['A'],v['B']):v for v in out['cells']}
 lines=['# Promise-function comparison matrix','',out['scope']+'.','',out['convention'],'',out['certification'],'','A row A and column B describe A versus B. `p` is a matched finite power exponent; `∞` disproves every finite exponent; `?` is an unresolved audit cell, not a claim that the literature has no answer. Finite cells have matching witness exponents; consult the per-cell JSON lower record.','', '| A / B | '+' | '.join(CORE)+' |','|---|'+'---|'*len(CORE)]
 for a in CORE:lines.append('| '+a+' | '+' | '.join((cs[a,b]['upper']['exponent']) if cs[a,b]['status']=='finite_upper_bound' else ('∞' if cs[a,b]['status']=='no_finite_power' else '?') for b in CORE)+' |')
 lines+=['','## Cell provenance','']
 for v in out['cells']:
  if v['A']==v['B']:continue
  ids=v.get('upper',{}).get('claim_ids',v.get('claim_ids',[]));lines.append('- '+v['A']+' / '+v['B']+': '+v['status']+'; '+', '.join('['+id+'](claims.md#'+id+')' for id in ids)+'.')
 (ROOT/'docs/partial-matrix.md').write_text('\n'.join(lines)+'\n')
 print({status:sum(v['status']==status for v in out['cells']) for status in sorted({v['status'] for v in out['cells']})})
if __name__=='__main__':write(json.loads((ROOT/'data/catalog.json').read_text()))
