"""Exact finite checks of the polynomial printed in NW95, footnote 1."""
from itertools import combinations,product
import unittest
TRIPLES=[(1,3,4),(1,2,5),(1,4,5),(2,3,4),(2,3,5),(1,2,6),(1,3,6),(2,4,6),(3,5,6),(4,5,6)]
def kushilevitz(x):
 return sum(x)-sum(x[i]*x[j] for i,j in combinations(range(6),2))+sum(x[i-1]*x[j-1]*x[k-1] for i,j,k in TRIPLES)
class WitnessTests(unittest.TestCase):
 def test_boolean_polynomial(self):
  self.assertEqual({kushilevitz(x) for x in product([0,1],repeat=6)},{0,1})
 def test_full_sensitivity_at_zero(self):
  self.assertEqual(kushilevitz([0]*6),0)
  for i in range(6):
   x=[0]*6;x[i]=1;self.assertEqual(kushilevitz(x),1)
 def test_exact_real_degree(self):
  # Mobius inversion obtains the unique multilinear coefficients exactly.
  values=[kushilevitz([(mask>>i)&1 for i in range(6)]) for mask in range(64)]
  for i in range(6):
   for mask in range(64):
    if mask&(1<<i):values[mask]-=values[mask^(1<<i)]
  self.assertEqual(max(mask.bit_count() for mask,c in enumerate(values) if c),3)
if __name__=='__main__':unittest.main()
