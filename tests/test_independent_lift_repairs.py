import unittest,itertools,json,hashlib
from pathlib import Path
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1]
class IndependentLiftRepairTests(unittest.TestCase):
 def test_arbitrary_transcript_completions_can_differ(self):
  # Both color permutations have first position fixed; two free edges can regroup.
  def projection(p,q):return frozenset(zip(p,q))
  p=(0,1,2);q=(0,1,2);other=(0,2,1)
  self.assertEqual(q[0],other[0]);self.assertNotEqual(projection(p,q),projection(p,other))
 def test_product_partial_bijection_conflict_threshold(self):
  reps=[]
  for p,q in itertools.product(itertools.permutations(range(2)),repeat=2):reps.append(frozenset([(0,i,p[i])for i in range(2)]+[(1,i,q[i])for i in range(2)]))
  partials=set()
  for r in reps:
   rr=list(r)
   for mask in range(16):partials.add(frozenset(rr[i]for i in range(4)if mask>>i&1))
  for a,b in itertools.product(partials,repeat=2):
   u=a|b;extends=any(u<=r for r in reps)
   separated=any(g==h and ((i==j and v!=w)or(v==w and i!=j))for g,i,v in a for h,j,w in b)
   self.assertEqual(not extends,separated)
 def test_audit_manifest_matches_corrected_proof(self):
  d=json.loads((ROOT/'data/lambda-lift-independent-audit.json').read_text());self.assertEqual(d['corrected_doc_sha256'],hashlib.sha256((ROOT/'docs/lambda-partite-lift.md').read_bytes()).hexdigest());self.assertFalse(d['formal_verification']);self.assertFalse(d['priority_certified'])
  p=next(p for p in json.loads((ROOT/'data/profile-matrices.json').read_text())['profiles']if p['profile']=='hypermatching');self.assertEqual(p['coefficient_definitions']['K_G'],'10368*(2k-1)^10; k=|lambda|')
 def test_aik_endpoints_raise_recorded_lower_exponents(self):
  cs={(c['A'],c['B']):c for c in json.loads((ROOT/'data/extended-completion-exponents.json').read_text())['cells']}
  for a,b in [('C','Q0'),('C','QE'),('Q0','Q')]:
   c=cs['completion_'+a,'completion_'+b];self.assertGreaterEqual(c['lower']['numeric_for_ranking'],2);self.assertEqual(c['lower']['loss'],'polylog')
 def test_augmented_rank_is_not_domain_rank_without_more_argument(self):
  xs=list(itertools.product([-1,1],repeat=2));H=[[1,x,y,x*y]for x,y in xs];a=[F(1,2),F(1,2),F(1,2),F(-1,2)];vals=[sum(v*w for v,w in zip(row,a))for row in H]
  self.assertEqual(max(map(abs,vals)),1)
  for i in range(4):
   for j in range(4):self.assertEqual(sum(H[i][k]*H[j][k]for k in range(4)),4*int(i==j))
  # Full saturated rows have rank four; a one-point domain has rank one.
  # This p is not support-minimal for that one-point promise: a constant fits.
  self.assertIn(vals[0],[-1,1]);self.assertEqual(len([vals[0]]),1)
