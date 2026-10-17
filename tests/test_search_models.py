"""Prevent loss of error/cost conventions when exporting search comparisons."""
import itertools,json,unittest
from fractions import Fraction
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[1]/'data/catalog.json').read_text());C={v['id']:v for v in D['claims']};M={v['id']:v for v in D['measures']}
class SearchModelTests(unittest.TestCase):
 def test_quantum_relation_error_preserved(self):
  c=C['quantum-search-random-node-size'];self.assertEqual(c['A'],'rel_Qeps');self.assertIn('epsilon=2/5',c['scope']['assumptions'])
  self.assertEqual(C['quantum-Boolean-random-node-size']['scope']['object_kind'],'decision_function')
 def test_coupled_tree_parameters_not_separately_minimized(self):
  v=next(v for v in D['algorithmic_bounds'] if v['id']=='CMP22-tree-rank-depth')
  self.assertIn('SAME tree',v['notes'])
  self.assertFalse(any(c.get('A')=='Q' and {f['measure'] for f in c.get('factors',[])}=={'DTRank','D'} for c in D['claims']))
 def test_size_and_sparsity_bases_separate(self):
  self.assertIn('nodes',M['DTNodes']['definition']);self.assertIn('leaves',M['DTSize']['definition'])
  self.assertNotEqual(M['monomialSparsity']['definition'],M['sparsity']['definition'])
  self.assertIn('0/1',M['approxMonomialSparsity']['notes'] if '0/1' in M['approxMonomialSparsity']['notes'] else M['approxMonomialSparsity']['definition'])
 def test_actual_AND_polynomial_has_one_monomial(self):
  # Möbius transform of AND on 0/1 inputs versus Walsh coefficients.
  for n in range(1,6):
   f=[int(mask==(1<<n)-1) for mask in range(1<<n)];a=list(f)
   for bit in range(n):
    for mask in range(1<<n):
     if mask&(1<<bit):a[mask]-=a[mask^(1<<bit)]
   walsh=[sum(f[x]*(-1)**((x&s).bit_count()) for x in range(1<<n)) for s in range(1<<n)]
   self.assertEqual(sum(v!=0 for v in a),1);self.assertEqual(sum(v!=0 for v in walsh),1<<n)
 def test_scan_permutation_expectation(self):
  for n in range(2,7):
   perms=list(itertools.permutations(range(n)))
   for k in range((n+1)//2,n+1):
    mean=Fraction(sum(next(i+1 for i,j in enumerate(p) if j<k) for p in perms),len(perms))
    self.assertEqual(mean,Fraction(n+1,k+1));self.assertLess(mean,2)
 def test_input_logs_not_erased_in_restricted_derandomization(self):
  for id in ['and-D-R3','andor-D-R4','search-derandomization-DandOr','search-log-size-ps-size']:
   self.assertFalse(C[id]['scalar_inference_allowed'])
  self.assertEqual(C['and-threshold-no-pure-power']['kind'],'no_polynomial_bound')
 def test_bomb_parameters_not_suppressed(self):
  c=C['bomb-quantum-explosion-parameter'];self.assertFalse(c['scalar_inference_allowed']);self.assertEqual(c['parameter_dependencies']['multiplicative_factor'],'1/epsilon')
 def test_source_dated_stronger_conjecture_not_marked_resolved(self):
  q={v['id']:v for v in D['conjectures']}
  self.assertEqual(q['KLMY-randomized-AND-derandomization']['status'],'resolved_as_stated_by_2023')
  self.assertEqual(q['KLMY-monomial-approximation']['status'],'refuted_as_literally_stated')
if __name__=='__main__':unittest.main()
