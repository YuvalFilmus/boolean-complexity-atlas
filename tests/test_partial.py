"""Promise-domain regression checks and independent small witness calculations."""
import importlib.util,itertools,json,unittest
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('partial_matrix',ROOT/'tools/partial_matrix.py');pm=importlib.util.module_from_spec(spec);spec.loader.exec_module(pm)
D=json.loads((ROOT/'data/catalog.json').read_text());C={x['id']:x for x in D['claims']};W={x['id']:x for x in D['witnesses']};S={x['id']:x for x in D['sources']};M={x['id']:x for x in D['measures']}

def weak_cert(x,domain):
 n=len(x)
 for k in range(n+1):
  for subset in itertools.combinations(range(n),k):
   if all(out==domain[x] or any(x[i]!=y[i] for i in subset) for y,out in domain.items()):return k

def admits_degree(domain,k):
 """Exact rational feasibility of evaluation equations, independent of the catalogue."""
 n=len(next(iter(domain)));mons=[s for j in range(k+1) for s in itertools.combinations(range(n),j)]
 rows=[[Fraction(all(x[i] for i in s)) for s in mons]+[Fraction(y)] for x,y in domain.items()]
 row=0
 for col in range(len(mons)):
  pivot=next((i for i in range(row,len(rows)) if rows[i][col]),None)
  if pivot is None:continue
  rows[row],rows[pivot]=rows[pivot],rows[row];scale=rows[row][col];rows[row]=[v/scale for v in rows[row]]
  for i in range(len(rows)):
   if i!=row and rows[i][col]:
    scale=rows[i][col];rows[i]=[a-scale*b for a,b in zip(rows[i],rows[row])]
  row+=1
 return not any(not any(r[:-1]) and r[-1] for r in rows)

class PartialTests(unittest.TestCase):
 def test_complete_without_conflicting_evidence(self):
  result=pm.build(D);self.assertEqual(len(result['cells']),144)
  self.assertEqual(sum(v['status']=='no_finite_power' for v in result['cells']),83)
  self.assertTrue(all(v['status']!='unresolved_in_this_audit' for v in result['cells']))
  for v in result['cells']:
   if 'upper' in v:self.assertEqual(v['upper']['exponent'],v['lower']['exponent'])
 def test_no_total_upper_or_input_factor_import(self):
  self.assertFalse(pm.eligible(C['D-Q4']))
  self.assertFalse(pm.eligible(C['partial-fbs-bs-n']))
  self.assertFalse(pm.eligible(C['search-D-psQ']))
 def test_witness_denominators_bounded(self):
  for c in D['claims']:
   if c.get('witness_id') and c['kind']=='no_polynomial_bound' and c['scope']['totality']=='partial' and c['scope']['input_alphabet']=='bits':
    w=W[c['witness_id']];self.assertEqual(w['growth_upper'][c['B']],0)
    self.assertIn(c['A'],w['growth_lower'])
 def test_dense_axes_small_instances(self):
  for m in [2,3,4]:
   zero=(0,)*m;strings=list(itertools.product([0,1],repeat=m))
   domain={a+zero:0 for a in strings if sum(a)>=(m+1)//2};domain.update({zero+b:1 for b in strings if sum(b)>=(m+1)//2})
   self.assertTrue(all(weak_cert(x,domain)==1 for x in domain))
   self.assertFalse(admits_degree(domain,m//2))
   self.assertTrue(admits_degree(domain,m))
   self.assertTrue(all(2*m/sum(x)<=4 for x in domain))
   self.assertTrue(all(sum(a!=b for a,b in zip(x,y))!=1 for x in domain for y in domain if domain[x]!=domain[y]))
 def test_nonempty_axes_degree_small_instances(self):
  for m in [2,3]:
   z=(0,)*m;xs=list(itertools.product([0,1],repeat=m));dom={x+z:0 for x in xs if any(x)};dom.update({z+x:1 for x in xs if any(x)})
   self.assertFalse(admits_degree(dom,m-1));self.assertTrue(admits_degree(dom,m))
 def test_input_output_notation_clash_preserved(self):
  self.assertTrue(any(a['text']=='s_0' and a['source']=='CDM23full' for a in M['ms']['aliases']))
  self.assertIn('output',M['s0']['definition'])
  self.assertIn('Input direction',M['input1s']['notes'])
 def test_versioned_author_lists_and_published_constant(self):
  self.assertEqual(len(S['AKPV18']['authors']),4);self.assertEqual(len(S['AKPVZ18']['authors']),5)
  self.assertEqual(C['partial-CAdv-cfbs']['constant_factor'],'1')
 def test_relation_degree_not_inherited_from_decision(self):
  self.assertEqual(C['partial-AdvPlus-boundedadeg2']['scope']['object_kind'],'decision_function')
  self.assertFalse(any(c['A']=='rel_Adv' and c['B']=='rel_adeg' and c['kind']=='upper_bound' for c in D['claims']))
if __name__=='__main__':unittest.main()
