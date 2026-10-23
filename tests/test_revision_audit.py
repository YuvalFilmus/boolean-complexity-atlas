"""Guard model changes and the counterexample behind the conjecture correction."""
import itertools,json,unittest
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[1]/'data/catalog.json').read_text())
C={v['id']:v for v in D['claims']};Q={v['id']:v for v in D['conjectures']}
class RevisionAuditTests(unittest.TestCase):
 def test_literal_sparsity_conjecture_refuted_with_evidence(self):
  q=Q['KLMY-monomial-approximation'];self.assertEqual(q['status'],'refuted_as_literally_stated')
  self.assertIn('monomial-sparsity-no-pure-approx-power',q['resolution'])
  self.assertEqual(C[q['resolution'][0]]['kind'],'no_polynomial_bound')
 def test_nonadaptive_revision_does_not_resolve_adaptive_question(self):
  c=C['extremal-forrelation-nonadaptive-2026'];self.assertEqual(c['A'],'Rna')
  self.assertEqual(Q['extremal-forrelation-sqrt']['status_audit']['verdict'],'primary_reaffirmed_open');self.assertNotIn('resolution',Q['extremal-forrelation-sqrt'])
  self.assertIn('NONADAPTIVE',' '.join(Q['extremal-forrelation-sqrt']['implications']))
 def test_logarithmic_bounds_cannot_enter_scalar_matrix(self):
  cs=[c for c in D['claims']if c['id'].startswith('restriction-log-')];self.assertEqual(len(cs),8)
  for c in cs:self.assertFalse(c['scalar_inference_allowed']);self.assertIsNone(c['exponent']);self.assertIn('log(2n)',c['statement'])
 def test_threshold_exact_coefficients(self):
  for n in range(2,7):
   vals=[int(x.bit_count()>=n-1) for x in range(1<<n)];a=list(vals)
   for i in range(n):
    for x in range(1<<n):
     if x&(1<<i):a[x]-=a[x^(1<<i)]
   self.assertEqual(sum(v!=0 for v in a),n+1);self.assertEqual(sum(map(abs,a)),2*n-1)
 def test_partition_approximant(self):
  # Averaging over all pairs verifies the elementary tester. Chernoff sampling
  # in the paper sparsifies this family to O(log n), which this test does not assert.
  for n in range(2,5):
   universe=(1<<n)-1
   for x in range(1<<n):
    def one(s):return int((x&s)==s or (x&(universe^s))==(universe^s))
    total=sum(one(s)*one(t) for s,t in itertools.product(range(1<<n),repeat=2))
    approx=total/(1<<(2*n));truth=int(x.bit_count()>=n-1)
    self.assertLessEqual(abs(approx-truth),1/3)
if __name__=='__main__':unittest.main()
