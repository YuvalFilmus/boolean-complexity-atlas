import unittest,math
from fractions import Fraction as F
class VerificationConstantsTests(unittest.TestCase):
 def test_half_threshold_convexity_and_identity(self):
  n,k=8,2;g=[F(math.comb(n-t,k),math.comb(n,k))if n-t>=k else F(0)for t in range(n+1)]
  self.assertTrue(all(g[t]-2*g[t+1]+g[t+2]>=0 for t in range(n-1)))
  self.assertEqual((1-F(1,2))/(1-0),F(1,2))
 def test_poisson_sampling_half_error_and_cost(self):
  for ws in [[1.0],[0.5,0.5],[0.25]*4,[0.1]*10]:
   miss=math.prod(2**(-w)for w in ws);cost=sum(1-2**(-w)for w in ws)
   self.assertLessEqual(miss,0.5+1e-12);self.assertLessEqual(cost,math.log(2)*sum(ws)+1e-12)
 def test_promise_sharpness_half_threshold_approaches_log2(self):
  ratios=[]
  for k in [3,5,10,20]:
   n=k**3
   def g(t):return math.prod((n-t-j)/(n-j)for j in range(k))
   lo,hi=0,n-k+1
   while hi-lo>1:
    mid=(lo+hi)//2
    if g(mid)>0.5:lo=mid
    else:hi=mid
   t=lo+(g(lo)-0.5)/(g(lo)-g(hi));ratios.append(t/(n/k))
   self.assertGreaterEqual(ratios[-1],0.5);self.assertLessEqual(ratios[-1],math.log(2)+1e-12)
  self.assertLess(abs(ratios[-1]-math.log(2)),abs(ratios[0]-math.log(2)))
