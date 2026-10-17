import unittest,json,itertools
from pathlib import Path
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1]
class LinearUCTests(unittest.TestCase):
 def test_uc_completion_tightening_preserves_exponent_and_witness(self):
  d=json.loads((ROOT/'data/extended-completion-inventory.json').read_text());cs={(c['A'],c['B']):c for c in d['cells']}
  for b in ['completion_UC0','completion_UC1']:
   c=cs['completion_D',b];self.assertEqual(c['upper']['exponent'],'2');self.assertTrue(any(v['exponent']==2 for v in c['direct_total_lower_witnesses']))
 def test_linear_sup_norm_and_first_zero_step(self):
  a=[F(1,4),F(1,2),F(-1,4)];delta=[F(1),F(-1),F(1)]
  slope=sum((1 if v>0 else -1)*w for v,w in zip(a,delta))
  if slope>0:delta=[-v for v in delta]
  t=min(-v/w for v,w in zip(a,delta) if v*w<0);b=[v+t*w for v,w in zip(a,delta)]
  self.assertIn(0,b);self.assertLessEqual(sum(map(abs,b)),sum(map(abs,a)))
  self.assertEqual(max(abs(a[0]+a[1]*x+a[2]*y) for x,y in itertools.product([-1,1],repeat=2)),sum(map(abs,a)))
 def test_higher_degree_norm_identity_does_not_hold(self):
  vals=[F(1+x+y-x*y,2) for x,y in itertools.product([-1,1],repeat=2)]
  self.assertEqual(max(map(abs,vals)),1);self.assertGreater(4*F(1,2),1)
