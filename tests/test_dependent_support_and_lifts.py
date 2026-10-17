import unittest,json,itertools
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class DependentSupportAndLiftTests(unittest.TestCase):
 def test_capped_one_sided_OR3_product_constant(self):
  pairs=list(itertools.combinations(range(3),2))
  for x in itertools.product([0,1],repeat=3):
   success=sum(any(x[i]for i in q)for q in pairs)/3
   if any(x):self.assertGreaterEqual(success,2/3)
   else:self.assertEqual(success,0)
  self.assertEqual(F(2,1)/F(2,3)*1,3)
 def test_kernel_amplification_primal_dual_example(self):
  # Support x1,x2; promise ++,-- gives kernel span(1,-1).
  primal=max(abs(a*x-a*y)for a in [-1,0,1]for x,y in itertools.product([-1,1],repeat=2));self.assertEqual(primal,2)
  dual=min(abs(1-t)+abs(-1-t)for t in [F(v,4)for v in range(-16,17)]);self.assertEqual(dual,2)
 def test_multigraph_matching_sensitivity_factor(self):
  pairs=list(itertools.combinations(range(4),2))
  for counts in itertools.product(range(3),repeat=6):
   deg=[sum(c for edge,c in zip(pairs,counts)if i in edge)for i in range(4)]
   if max(deg)>3:continue
   active=[set(e)for e,c in zip(pairs,counts)if c]
   nu=2 if any(a.isdisjoint(b)for a,b in itertools.combinations(active,2))else int(bool(active))
   self.assertLessEqual(sum(counts),5*nu)
 def test_uniform_lift_does_not_assume_witnessing(self):
  d=json.loads((ROOT/'data/profile-matrices.json').read_text());p=next(p for p in d['profiles']if p['profile']=='uniform-hypermatching')
  self.assertEqual(sum(c['status']!='not_yet_indexed'for c in p['cells']),132)
  c=next(c for c in p['cells']if c['A']=='domainD'and c['B']=='domainS');self.assertEqual(c['exponent'],'10');self.assertIn('uniform-hypermatching-D-sensitivity-lift',c['claim_ids'])
  self.assertFalse(any('witnessing' in v for v in c['claim_ids']))
 def test_extended_intervals_and_endpoint_caveats(self):
  d=json.loads((ROOT/'data/extended-completion-exponents.json').read_text());self.assertEqual(len(d['cells']),506)
  finite=[c for c in d['cells']if c['status']=='finite_exponent_interval'];self.assertEqual(len(finite),442)
  for c in finite:
   self.assertLessEqual(c['lower']['numeric_for_ranking'],float(F(c['upper']['exponent']))+1e-9);self.assertFalse(c['globally_best_known_certified']);self.assertIn('loss',c['endpoint_warning'])
  c=next(c for c in finite if c['A']=='completion_D'and c['B']=='completion_R1');self.assertTrue(c['matching_exponent']);self.assertEqual(c['upper']['exponent'],'2')
