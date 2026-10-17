import unittest,itertools,json
from pathlib import Path
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1]
class LambdaAndKernelTests(unittest.TestCase):
 def test_lambda_product_fibers(self):
  for lam in [(1,1),(2,1),(1,1,1)]:
   groups=[[(i,j)for j in range(2*a)]for i,a in enumerate(lam)];fibers={}
   for ps in itertools.product(*(list(itertools.permutations(g))for g in groups)):
    edges=tuple(sorted(tuple(sorted(v for i,a in enumerate(lam)for v in ps[i][b*a:(b+1)*a]))for b in range(2)))
    fibers[edges]=fibers.get(edges,0)+1
   self.assertEqual(len(set(fibers.values())),1)
   self.assertTrue(all(len(e)==sum(lam)for part in fibers for e in part))
 def test_lazy_lambda_query_simulation(self):
  lam=(2,1);edges=[((0,0),(0,2),(1,1)),((0,1),(0,3),(1,0))];groups=[[(i,j)for j in range(2*a)]for i,a in enumerate(lam)];oracle={v:e for e in edges for v in e};pi={};inv={};used=set();calls=0
  def discover(v,b):
   nonlocal calls
   calls+=1;used.add(b)
   for i,a in enumerate(lam):
    vs=sorted(w for w in oracle[v]if w[0]==i)
    for j,w in enumerate(vs):pi[i,b*a+j]=w;inv[w]=(i,b*a+j)
  queries=[('inv',(1,0)),('fwd',(0,0)),('inv',(0,2)),('fwd',(1,1)),('fwd',(0,3))]
  for typ,arg in queries:
   before=calls
   if typ=='inv':
    if arg not in inv:discover(arg,min(set(range(2))-used))
    i,pos=inv[arg];self.assertEqual(pi[i,pos],arg)
   else:
    i,pos=arg
    if (i,pos)not in pi:discover(next(v for v in groups[i]if v not in inv),pos//lam[i])
    self.assertEqual(inv[pi[i,pos]],(i,pos))
   self.assertLessEqual(calls-before,1)
  got={frozenset(pi[i,b*a+j]for i,a in enumerate(lam)for j in range(a))for b in used};self.assertEqual(got,{frozenset(e)for e in edges})
 def test_quantitative_kernel_line_margin(self):
  gamma=F(1,4);R=F(1,2);t=F(3,10);nonzero=[]
  for x,y in itertools.product([-1,1],repeat=2):
   p=F(x+y,2);h=x-y
   if h:nonzero.append(F(1,abs(h)))
   self.assertGreaterEqual(abs(p+t*h),gamma);self.assertLessEqual(abs(t),R)
  self.assertGreater(R,gamma*sum(nonzero))
 def test_quadratic_log_is_not_reported_as_pure_endpoint(self):
  d=json.loads((ROOT/'data/extended-completion-inventory.json').read_text())
  for a in ['Q0','R1']:
   c=next(c for c in d['cells']if c['native_A']==a and c['native_B']=='R');self.assertEqual(c['upper']['exponent'],'2');self.assertEqual(c['upper']['log_power'],'1');self.assertFalse(c['upper']['endpoint_without_log']);self.assertEqual(c['pure_upper']['exponent'],'3')
 def test_fractional_verifier_constants_are_convention_specific(self):
  d=json.loads((ROOT/'data/catalog.json').read_text());cs={c['id']:c for c in d['claims']}
  self.assertIn('2*RC',cs['completion-support-FC-RC']['statement']);self.assertIn('RC(f)<=(ln 2)*FC',cs['completion-support-RC-FC']['statement'])
