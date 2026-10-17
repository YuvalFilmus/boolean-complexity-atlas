"""Guard parameter, completion and polynomial-extension audit distinctions."""
import importlib.util,itertools,json,unittest
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];D=json.loads((ROOT/'data/catalog.json').read_text());C={c['id']:c for c in D['claims']}
spec=importlib.util.spec_from_file_location('ec',ROOT/'tools/extended_completions.py');ec=importlib.util.module_from_spec(spec);spec.loader.exec_module(ec)
class BroaderDomainTests(unittest.TestCase):
 def test_mixed_products_not_lifted_by_independent_minima(self):
  c=dict(C['C-bs2']);c['factors']=[dict(measure='bs',exponent=1),dict(measure='s',exponent=1)]
  self.assertFalse(ec.eligible(c))
  values=[(1,100),(100,1)];self.assertEqual(min(a*b for a,b in values),100);self.assertEqual(min(a for a,b in values)*min(b for a,b in values),1)
 def test_min_max_not_interchanged(self):
  values=[(0,5),(5,0)];self.assertEqual(min(max(a,b)for a,b in values),5);self.assertEqual(max(min(a for a,b in values),min(b for a,b in values)),0)
 def test_domain_parameters_not_erased(self):
  for id in ['domain-parameterized-domainD-domainBS','domain-parameterized-domainC-domainBS']:self.assertFalse(C[id]['scalar_inference_allowed'])
  profiles=json.loads((ROOT/'data/general-domains.json').read_text())['profiles'];m=next(v for v in profiles if v['id']=='multislice');self.assertIn('min(lambda)=1',m['caveat'])
 def test_polynomial_norm_counterexample_to_specific_step(self):
  # p=(x1+x2+x3+x4)/4. Delta preserves p at the two promised points.
  delta=[F(1),F(9,10),F(-4,5),F(-11,10)];self.assertEqual(sum(delta),0)
  vals=[sum((F(1,4)+delta[i])*x[i]for i in range(4))for x in itertools.product([-1,1],repeat=4)]
  self.assertEqual(min(map(abs,vals)),F(1,5));self.assertEqual(max(map(abs,vals)),F(19,5));self.assertGreater(max(map(abs,vals)),2*max(map(abs,delta)))
  record=next(v for v in D['algorithmic_bounds']if v['id']=='perturbation-Lemma71-audit');self.assertEqual(record['status'],'statement_checked_proof_pending')
 def test_slice_flips_depend_on_extension(self):
  support=[1,2] # 01 and 10
  zero=lambda x:0;other=lambda x:int(x==0)
  self.assertTrue(all(zero(x)==other(x)for x in support))
  flip=lambda f:sum((f(x)-f(x^1))**2 for x in support)/2
  self.assertEqual(flip(zero),0);self.assertEqual(flip(other),1/2)
  self.assertTrue(all(other(x)==other(3^x)for x in support))
 def test_distributional_equivalence_not_resolution(self):
  qs={q['id']:q for q in D['conjectures']};self.assertIn('no_resolution_verified',qs['AA-bounded-polynomial-influence']['status']);self.assertIn('not its truth',qs['AA-bounded-polynomial-influence']['implications'][0])
 def test_extended_inventory_size(self):
  out=ec.build(D,json.loads((ROOT/'data/completion-matrix.json').read_text()));self.assertEqual(len(out['order']),23);self.assertEqual(len(out['cells']),506)
if __name__=='__main__':unittest.main()
