#!/usr/bin/env python3
"""Index every ordered pair without treating missing evidence as an open problem."""
import json
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
 d=json.loads((ROOT/'data/catalog.json').read_text());core=json.loads((ROOT/'data/core-matrix.json').read_text())
 ids=[m['id'] for m in d['measures']];direct=defaultdict(list)
 for c in d['claims']:
  if c['A'] and c['B']:direct[c['A'],c['B']].append(c)
 completion=json.loads((ROOT/'data/completion-matrix.json').read_text()) if (ROOT/'data/completion-matrix.json').exists() else {'cells':[]};permutation=json.loads((ROOT/'data/permutation-matrix.json').read_text()) if (ROOT/'data/permutation-matrix.json').exists() else {'cells':[]};completionkeys={(c['A'],c['B'])for c in completion['cells']};permutationkeys={(c['A'],c['B'])for c in permutation['cells']if c['upper_exponent']is not None};ext=json.loads((ROOT/'data/extended-completion-inventory.json').read_text()) if (ROOT/'data/extended-completion-inventory.json').exists() else {'cells':[]};extkeys={(c['A'],c['B'])for c in ext['cells']if c['status']!='not_yet_indexed'};corekeys={(c['A'],c['B']) for c in core['cells']};partial=json.loads((ROOT/'data/partial-matrix.json').read_text());partialkeys={(c['A'],c['B']) for c in partial['cells']};domain=json.loads((ROOT/'data/domain-matrix.json').read_text()) if (ROOT/'data/domain-matrix.json').exists() else {'cells':[]};domainkeys={(c['A'],c['B']) for c in domain['cells'] if c['status']!='not_yet_indexed' or c.get('parameterized_direct_claim_ids')};rows=[]
 for a in ids:
  for b in ids:
   if a==b:continue
   groups={}
   for c in direct[a,b]:
    key=json.dumps(c['scope'],sort_keys=True)
    g=groups.setdefault(key,dict(scope=c['scope'],claim_ids=[],historical_claim_ids=[]))
    g['historical_claim_ids' if c.get('historical') else 'claim_ids'].append(c['id'])
   rows.append(dict(A=a,B=b,evidence_groups=list(groups.values()),core_matrix_record=(a,b) in corekeys,partial_matrix_record=(a,b) in partialkeys,extended_completion_record=(a,b)in extkeys,general_domain_record=(a,b)in domainkeys,completion_matrix_record=(a,b)in completionkeys,permutation_matrix_record=(a,b)in permutationkeys,status='evidence_indexed' if groups or (a,b) in corekeys or(a,b)in completionkeys or(a,b)in permutationkeys or(a,b)in extkeys or(a,b)in domainkeys else 'not_yet_indexed'))
 summary=dict(measures=len(ids),ordered_distinct_pairs=len(rows),pairs_with_indexed_evidence=sum(r['status']=='evidence_indexed' for r in rows),core_off_diagonal_pairs=132,partial_off_diagonal_pairs=132)
 (ROOT/'data/pair-index.json').write_text(json.dumps(dict(warning='Not yet indexed does not mean no bound is known. Evidence groups with different scopes must never be merged automatically.',summary=summary,pairs=rows),ensure_ascii=False,indent=2)+'\n')
 print(summary)
if __name__=='__main__':main()
