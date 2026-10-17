import unittest,json,itertools,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class CompletionClosureTests(unittest.TestCase):
 def test_extended_grid_has_evidence_and_provenance(self):
  d=json.loads((ROOT/'data/extended-completion-inventory.json').read_text());self.assertEqual(len(d['cells']),506)
  for c in d['cells']:
   self.assertNotEqual(c['status'],'not_yet_indexed');self.assertFalse(c['globally_best_known_certified'])
   self.assertTrue(c.get('upper') or c.get('no_polynomial_claim_ids'))
 def test_majority_perturbation_preserves_promise_but_not_global_sign(self):
  for n in [3,5,7]:
   vals=list(itertools.product([-1,1],repeat=n));self.assertEqual(min(abs(sum(x)) for x in vals),1);self.assertEqual(max(abs(sum(x)) for x in vals),n)
   for x in vals:
    if sum(x[1:])==0:self.assertEqual(sum(x),x[0])
   self.assertTrue(any((sum(x)>0)!=(x[0]>0) for x in vals))
 def test_permutation_witness_certificate_and_sensitive_changes(self):
  for n in [2,4]:
   ps=list(itertools.permutations(range(n)))
   for p in ps:
    pos=p.index(0);f=int(pos<n//2)
    self.assertTrue(all(int(q.index(0)<n//2)==f for q in ps if q[pos]==0))
    self.assertTrue(all(q[pos]!=0 for q in ps if int(q.index(0)<n//2)!=f))
 def test_general_counterexamples_never_contradict_uniform_upper_paths(self):
  d=json.loads((ROOT/'data/domain-matrix.json').read_text());self.assertEqual(sum(bool(c['subclass_counterexample_claim_ids']) for c in d['cells']),7)
  for c in d['cells']:
   if c['subclass_counterexample_claim_ids']:self.assertNotIn('exponent',c)
