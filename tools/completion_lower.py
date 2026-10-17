#!/usr/bin/env python3
"""Transfer total witnesses through the audited completion upper graph."""
from pathlib import Path
from fractions import Fraction
import json
from matrix import expr_value,expr_text
ROOT=Path(__file__).resolve().parents[1]
def build(d,ext):
 mids={m['id']:m['completion_of'] for m in d['measures']if m.get('completion_of')};nodes=list(mids.values());U={(a,a):dict(exponent='1',claim_ids=[],endpoint_without_log=True)for a in nodes}
 for c in ext['cells']:
  if c.get('upper'):U[c['native_A'],c['native_B']]=c['upper']
 inv=set(nodes)-{'C0','C1','UC0','UC1','R1'};swap={'C0':'C1','C1':'C0','UC0':'UC1','UC1':'UC0'};seeds=[]
 for c in d['claims']:
  s=c['scope'];x,y=c['A'],c['B']
  if c['kind']!='separation' or x not in nodes or y not in nodes or c.get('historical') or c.get('exponent') is None or s['object_kind']!='decision_function' or s['totality']!='total' or s['input_alphabet']!='bits' or s['classes'] or s.get('assumptions') or c.get('factors'):continue
  seed=dict(X=x,Y=y,exponent=c.get('exponent_expression',c['exponent']),claim_id=c['id'],loss=c['loss'],transformation='original total witness');seeds.append(seed)
  if x!='R1' and y!='R1':seeds.append({**seed,'X':swap.get(x,x),'Y':swap.get(y,y),'transformation':'complement both outputs; invariant measures unchanged'})
  if y in inv and (x,'C') in U:
   pre=U[x,'C'];pe=Fraction(pre['exponent'])
   ex=seed['exponent'] if pe==1 else dict(op='div',left=seed['exponent'],right=str(pe))
   for side in ['C0','C1']:seeds.append({**seed,'X':side,'exponent':ex,'extra_claim_ids':pre['claim_ids'],'pretransfer_endpoint_without_log':pre.get('endpoint_without_log',False),'transformation':'First X<=O(C^u); then C=max(C0,C1): choose a fixed-side infinite subsequence and complement if needed; denominator is complement invariant'})
 rows=[]
 for c in ext['cells']:
  a,b=c['native_A'],c['native_B'];row=dict(A=c['A'],B=c['B'],globally_best_known_certified=False)
  if c.get('no_polynomial_claim_ids'):
   row.update(status='no_finite_power',claim_ids=c['no_polynomial_claim_ids']);rows.append(row);continue
  # Parity has cost Theta(n) for every listed measure except QC=Theta(sqrt(n)).
  weights={n:Fraction(1,2)if n=='QC' else Fraction(1)for n in nodes};rat=weights[a]/weights[b]
  best=dict(exponent_expression=str(rat),numeric_for_ranking=float(rat),witness='parity',claim_ids=[],loss='none',proof='All listed parity costs are Theta(n), except QC=Theta(sqrt(n)) by the certificate characterization. The total witness has a unique completion.')
  if c.get('lower') and c['lower'].get('numeric_for_ranking',0)>best['numeric_for_ranking']:best={**c['lower'],'inherited_core_record':True}
  for s in seeds:
   if (s['X'],a)not in U or (b,s['Y'])not in U:continue
   u,v=U[s['X'],a],U[b,s['Y']];den=Fraction(u['exponent'])*Fraction(v['exponent']);val=expr_value(s['exponent'])/float(den)
   if val>best['numeric_for_ranking']+1e-12:
    expr=s['exponent']if den==1 else dict(op='div',left=s['exponent'],right=str(den))
    best=dict(exponent_expression=expr,numeric_for_ranking=val,witness=s['claim_id'],claim_ids=list(dict.fromkeys([s['claim_id']]+s.get('extra_claim_ids',[])+u['claim_ids']+v['claim_ids'])),loss=s['loss'],upper_transfer_endpoints_without_log=u.get('endpoint_without_log',False)and v.get('endpoint_without_log',False)and s.get('pretransfer_endpoint_without_log',True),transformation=s['transformation'],proof='Use X<=O(A^u) and B<=O(Y^v) on a total witness X>=Y^ell (with its recorded endpoint loss). Every target exponent below ell/(u*v) is excluded. Total witnesses have unique completions; no independently minimized product or promise witness is used.')
  if 'loss' not in best:
   original=next((claim for claim in d['claims'] if claim['id']==best.get('witness')),None)
   best['loss']=original['loss'] if original else 'see_inherited_core_witness'
   best['endpoint_transfer_detail']='Inherited core exponent exclusion; inspect the cited claim paths for any additional logarithmic transfer loss.'
  upper=c.get('upper');row.update(status='finite_exponent_interval',lower=best,upper=upper,matching_exponent=bool(upper and abs(float(Fraction(upper['exponent']))-best['numeric_for_ranking'])<1e-10),endpoint_warning='Matching exponents do not erase logarithmic/subpolynomial losses or establish optimal constants.')
  if upper and best['numeric_for_ranking']>float(Fraction(upper['exponent']))+1e-9:raise ValueError('Inconsistent transferred interval: '+a+' / '+b)
  rows.append(row)
 return dict(warning='Exponent exclusions transferred through total-function witnesses and checked upper chains. Best-known status and endpoint attainment are not certified. Rounded legacy exponents are replaced by stored exact expressions where present.',cells=rows)
def main():
 out=build(json.loads((ROOT/'data/catalog.json').read_text()),json.loads((ROOT/'data/extended-completion-inventory.json').read_text()));(ROOT/'data/extended-completion-exponents.json').write_text(json.dumps(out,indent=2)+'\n');ls=['# Extended completion exponent intervals','',out['warning'],'','| A | B | Lower excluded exponent | Upper exponent | Matching exponents |','|---|---|---:|---:|---|']
 for c in out['cells']:
  if c['status']=='no_finite_power':ls.append('| '+c['A']+' | '+c['B']+' | no finite power | — | — |');continue
  ls.append('| '+c['A']+' | '+c['B']+' | '+expr_text(c['lower']['exponent_expression'])+' | '+c['upper']['exponent']+(' with log^'+c['upper']['log_power'] if c['upper'].get('log_power','0')!='0' else '')+' | '+str(c['matching_exponent'])+' |')
 queue=sorted([c for c in out['cells']if c['status']=='finite_exponent_interval'and not c['matching_exponent']],key=lambda c:(-float(Fraction(c['upper']['exponent']))/c['lower']['numeric_for_ranking'],c['A'],c['B']))
 (ROOT/'data/completion-unmatched-queue.json').write_text(json.dumps(dict(warning='Unmatched in this catalogue is not a certified literature gap or open problem. Ranking is only the recorded upper/lower ratio.',cells=queue),indent=2)+'\n')
 (ROOT/'docs/extended-completion-exponents.md').write_text('\n'.join(ls)+'\n');print('Finite intervals:',sum(c['status']=='finite_exponent_interval'for c in out['cells']),'matching:',sum(c.get('matching_exponent',False)for c in out['cells']),'no finite power:',sum(c['status']=='no_finite_power'for c in out['cells']))
if __name__=='__main__':main()
