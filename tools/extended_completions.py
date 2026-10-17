#!/usr/bin/env python3
"""Conservative inventory beyond the twelve-measure completion core."""
import json,copy
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def eligible(c):
 s=c['scope']
 return c['kind']=='upper_bound' and c['exponent']is not None and c.get('scalar_inference_allowed',True) and not c.get('factors') and not c.get('input_length_factor') and c['loss']=='none' and not c.get('historical') and s['object_kind']=='decision_function' and s['totality']in ['total','partial_or_total'] and s['input_alphabet']=='bits' and not s['classes'] and not s.get('assumptions') and (c['status']in ['primary_statement_and_proof_route_checked','repository_derivation_checked','definition_proof'] or c['id'] in {'C-R0','R0-D','R-R0','Q0-QE','Q0-R0'})
def build(d,core):
 mids={m['completion_of']:m['id']for m in d['measures']if m.get('completion_of')};nodes=list(mids);paths={(a,a):(Fraction(1),[])for a in nodes}
 for c in d['claims']:
  a,b=c['A'],c['B']
  if a not in mids or b not in mids or not eligible(c):continue
  e=Fraction(str(c['exponent']))
  if(a,b)not in paths or e<paths[a,b][0]:paths[a,b]=(e,[c['id']])
 # Reuse already audited pure core chains before extending to the larger inventory.
 for cell in core['cells']:
  a,b=cell['base_A'],cell['base_B'];u=cell['upper']
  if a in mids and b in mids and u.get('endpoint_without_log'):
   e=Fraction(str(u['exponent']))
   if (a,b) not in paths or e<paths[a,b][0]:paths[a,b]=(e,list(u['claim_ids']))
 for k in nodes:
  for a in nodes:
   for b in nodes:
    if(a,k)in paths and(k,b)in paths:
     e=paths[a,k][0]*paths[k,b][0]
     if(a,b)not in paths or e<paths[a,b][0]:paths[a,b]=(e,paths[a,k][1]+paths[k,b][1])
 # Keep the known quadratic-log zero-error simulation in a separate closure.
 # x^a log(2+x)^b composed with x^c log(2+x)^d has powers ac, ad+b.
 soft={key:(v[0],Fraction(0),list(v[1])) for key,v in paths.items()}
 log_claim=next((c for c in d['claims'] if c['id']=='R0-R2' and c['loss']=='explicit_log' and c.get('log_factor')=='log(2+R)'),None)
 if log_claim:soft['R0','R']=(Fraction(2),Fraction(1),['R0-R2'])
 for k in nodes:
  for a in nodes:
   for b in nodes:
    if (a,k) in soft and (k,b) in soft:
     u,v=soft[a,k],soft[k,b];e=u[0]*v[0];l=u[0]*v[1]+u[1]
     if (a,b) not in soft or (e,l)<soft[a,b][:2]:soft[a,b]=(e,l,u[2]+v[2])
 corecells={(c['A'],c['B']):c for c in core['cells']};rows=[]
 for a in nodes:
  for b in nodes:
   if a==b:continue
   ca,cb=mids[a],mids[b];row=dict(A=ca,B=cb,native_A=a,native_B=b,status='not_yet_indexed',globally_best_known_certified=False)
   if(a,b)in paths:row.update(status='pure_upper_chain_indexed',upper=dict(exponent=str(paths[a,b][0]),claim_ids=paths[a,b][1],endpoint_without_log=True))
   if(ca,cb)in corecells:row.update(status='completion_core_evidence',upper=copy.deepcopy(corecells[ca,cb]['upper']),lower=copy.deepcopy(corecells[ca,cb]['lower']))
   if (a,b) in soft:
    se,sl,si=soft[a,b]
    current=row.get('upper')
    if current and se<Fraction(str(current['exponent'])):
     row['pure_upper']=copy.deepcopy(current)
     row['upper']=dict(exponent=str(se),log_power=str(sl),claim_ids=si,endpoint_without_log=(sl==0))
     row['status']='upper_chain_with_logarithmic_loss' if sl else row['status']
    elif current and not current.get('endpoint_without_log',True) and (a,b)==('R0','R'):current['log_power']='1'
   neg=[c['id']for c in d['claims']if c['A']==a and c['B']==b and c['kind']=='no_polynomial_bound'and not c.get('historical')and c['scope']['object_kind']=='decision_function'and c['scope']['totality']=='total'and c['scope']['input_alphabet']=='bits']
   if neg:row.update(status='total_witness_excludes_every_power',no_polynomial_claim_ids=neg)
   lower=[]
   invariant={'D','R','R0','Q','QE','Q0','C','RC','QC','UC','bs','s','lambda','deg','adeg','fbs','FC','nRelevant'}
   for c in d['claims']:
    sc=c['scope']
    if c['kind']!='separation' or c.get('historical') or sc['totality']!='total' or sc['input_alphabet']!='bits' or sc['classes'] or sc.get('assumptions') or c.get('exponent') is None or c.get('factors'):continue
    direct=c['A']==a and c['B']==b
    complemented=(a in invariant and c['A']==a and ((c['B']=='UC1' and b=='UC0') or (c['B']=='UC0' and b=='UC1')))
    if direct or complemented:lower.append(dict(claim_id=c['id'],exponent=c['exponent'],loss=c['loss'],complemented_witness=complemented,total_witness_unique_completion=True))
   if lower:row['direct_total_lower_witnesses']=lower
   rows.append(row)
 return dict(order=list(mids.values()),warning='Minimum-completion inventory. Upper bounds choose a completion optimal for B; mixed products of independently minimized measures are excluded. Lower witnesses here are total functions, which have unique completions. Blank means not indexed, not open. Pure closure may be weaker than an unindexed logarithmic endpoint.',cells=rows)
def main():
 out=build(json.loads((ROOT/'data/catalog.json').read_text()),json.loads((ROOT/'data/completion-matrix.json').read_text()));(ROOT/'data/extended-completion-inventory.json').write_text(json.dumps(out,indent=2)+'\n');ls=['# Extended minimum-completion inventory','',out['warning'],'',f"{len(out['order'])} measures; {len(out['cells'])} off-diagonal cells.",'','| A | B | Evidence | Upper exponent | Direct lower witnesses |','|---|---|---|---:|---|']
 for c in out['cells']:ls.append('| '+c['A']+' | '+c['B']+' | '+c['status']+' | '+c.get('upper',{}).get('exponent','—')+(' + log^'+c['upper']['log_power'] if c.get('upper',{}).get('log_power','0')!='0' else '')+' | '+', '.join(v['claim_id']+(' (complement)' if v['complemented_witness'] else '') for v in c.get('direct_total_lower_witnesses',[]))+' |')
 (ROOT/'docs/extended-completion-inventory.md').write_text('\n'.join(ls)+'\n');print('Extended completion cells:',len(out['cells']),'with evidence:',sum(c['status']!='not_yet_indexed'for c in out['cells']))
if __name__=='__main__':main()
