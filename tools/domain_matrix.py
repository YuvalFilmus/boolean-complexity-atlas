#!/usr/bin/env python3
"""Keep general-domain comparisons separate from oracle-specific theorems."""
import json
from pathlib import Path
from fractions import Fraction
ROOT=Path(__file__).resolve().parents[1]
def build(d):
 nodes=[m['id'] for m in d['measures'] if m['id'].startswith('domain') and m['id']!='domainCoverRadius']
 paths={(a,a):(Fraction(1),[]) for a in nodes}; specialized=[];parameterized=[]
 for c in d['claims']:
  if c['A'] not in nodes or c['B'] not in nodes:continue
  if c['scope']['classes']!=['composable_query_domain']:specialized.append(c['id']);continue
  if 'parameterized' in c['id']:parameterized.append(c['id']);continue
  if c['kind']!='upper_bound' or c.get('exponent') is None:continue
  paths[c['A'],c['B']]=(Fraction(str(c['exponent'])),[c['id']])
 for k in nodes:
  for a in nodes:
   for b in nodes:
    if (a,k) in paths and (k,b) in paths:
     e=paths[a,k][0]*paths[k,b][0]
     if (a,b) not in paths or e<paths[a,b][0]:paths[a,b]=(e,paths[a,k][1]+paths[k,b][1])
 rows=[]
 for a in nodes:
  for b in nodes:
   if a==b:continue
   row={'A':a,'B':b,'status':'not_yet_indexed','best_known_certified':False}
   if (a,b) in paths:row.update(status='parameter_free_upper_chain',exponent=str(paths[a,b][0]),claim_ids=paths[a,b][1])
   row['parameterized_direct_claim_ids']=[c for c in parameterized if next(x for x in d['claims'] if x['id']==c)['A']==a and next(x for x in d['claims'] if x['id']==c)['B']==b]
   row['subclass_counterexample_claim_ids']=[c['id'] for c in d['claims'] if c['A']==a and c['B']==b and c['id'].startswith('forward-multislice-D-unbounded-')]
   if row['subclass_counterexample_claim_ids']:row['status']='no_uniform_power_subclass_witness'
   rows.append(row)
 return {'scope':'Total Boolean functions on composable query domains with the source query model. Constants and error conventions remain in cited claims.','warning':'Domain-dependent bounds are listed separately and never treated as uniform pure-power edges. Forward-only multislices and forward/inverse permutations have different oracles. Blank means unindexed, not open.','nodes':nodes,'cells':rows,'parameterized_claim_ids':parameterized,'other_oracle_claim_ids':specialized}
def main():
 d=build(json.loads((ROOT/'data/catalog.json').read_text()));(ROOT/'data/domain-matrix.json').write_text(json.dumps(d,indent=2)+'\n')
 ls=['# General-domain comparison inventory','',d['scope'],'',d['warning'],'','| A | B | Upper exponent | Evidence |','|---|---|---:|---|']
 for c in d['cells']:ls.append('| '+c['A']+' | '+c['B']+' | '+c.get('exponent','—')+' | '+', '.join(c.get('claim_ids',[])+c['parameterized_direct_claim_ids']+c['subclass_counterexample_claim_ids'])+' |')
 ls+=['','Parameterized direct bounds: '+', '.join(d['parameterized_claim_ids']), '','Other oracle scopes (not inserted above): '+', '.join(d['other_oracle_claim_ids'])]
 (ROOT/'docs/domain-matrix.md').write_text('\n'.join(ls)+'\n');print('General-domain cells:',len(d['cells']),'parameter-free chains:',sum(c['status']=='parameter_free_upper_chain' for c in d['cells']),'no-uniform-power cells:',sum(c['status']=='no_uniform_power_subclass_witness' for c in d['cells']))
if __name__=='__main__':main()
