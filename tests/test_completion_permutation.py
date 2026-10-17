"""Completion minima, logarithmic endpoints, domain-qualified closure and constants."""
import importlib.util,itertools,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
D=json.loads((ROOT/'data/catalog.json').read_text());C={c['id']:c for c in D['claims']};M={m['id']:m for m in D['measures']}
def tool(name):
 spec=importlib.util.spec_from_file_location(name,ROOT/'tools'/str(name+'.py'));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
class CompletionPermutationTests(unittest.TestCase):
 def test_lift_preserves_log_endpoint(self):
  core=json.loads((ROOT/'data/core-matrix.json').read_text());out=tool('completion_matrix').build(core)
  self.assertEqual(len(out['cells']),132)
  c=next(c for c in out['cells']if(c['base_A'],c['base_B'])==('R0','R'))
  self.assertFalse(c['upper']['endpoint_without_log']);self.assertEqual(c['upper']['claim_ids'],['R0-R2'])
  self.assertIn('only total completion',c['lower_justification'])
 def test_minima_need_not_share_optimizer(self):
  # A<=2B holds for both completions; choose B's minimizer to bound min A.
  values=[(2,1),(1,5)];self.assertNotEqual(min(range(2),key=lambda i:values[i][0]),min(range(2),key=lambda i:values[i][1]))
  self.assertLessEqual(min(a for a,b in values),2*min(b for a,b in values))
 def test_nested_critical_certificate_definition(self):
  self.assertIn('block-optimal',M['criticalCertificate']['definition'])
  self.assertNotEqual(M['criticalBScompletion']['definition'],M['rel_cbs']['definition'])
 def test_permutation_closure_has_only_permutation_edges(self):
  out=tool('permutation_matrix').build(D);self.assertEqual(len(out['cells']),132)
  for c in out['cells']:
   self.assertIsNotNone(c['upper_exponent'])
   for id in c['claim_ids']:self.assertEqual(C[id]['scope']['input_alphabet'],'permutation')
 def test_failure_to_boolean_error_conversion(self):
  # On star use a fresh fair bit, retaining the query cap.
  self.assertAlmostEqual(1/3+(2/3)/2,2/3)
  self.assertIn('2/3',M['permRfail23']['definition'])
 def test_expected_one_sided_sharp_constant(self):
  c=C['Nis89-expected-one-sided-repair'];self.assertEqual(c['constant'],4)
  self.assertEqual(4*(1/2)**2,1);self.assertFalse(C['Nis89-D-R1-square']['scalar_inference_allowed'])
 def test_inside_paper_constant_improvement(self):
  self.assertEqual(C['relevant-degree-43935']['constant']['value'],'4.3935')
  self.assertIn('relevant-degree-43935',C['nRelevant-deg-exp']['superseded_by'])
 def test_minimum_relevance_equals_projection_complexity(self):
  n=2
  for vals in itertools.product([-1,0,1],repeat=1<<n):
   dom=[i for i,v in enumerate(vals)if v!=-1]
   fixed=min(s.bit_count()for s in range(1<<n)if all(vals[x]==vals[y]or(x&s)!=(y&s)for x in dom for y in dom))
   holes=[i for i,v in enumerate(vals)if v==-1];best=n
   for fill in itertools.product([0,1],repeat=len(holes)):
    f=list(vals)
    for i,v in zip(holes,fill):f[i]=v
    rel=sum(any(f[x]!=f[x^(1<<i)]for x in range(1<<n))for i in range(n))
    best=min(best,rel)
   self.assertEqual(fixed,best)
 def test_permutation_single_entry_witness(self):
  for n in range(2,5):
   counts=[]
   for pi in itertools.permutations(range(n)):
    edges=[]
    for i,j in itertools.combinations(range(n),2):
     q=list(pi);q[i],q[j]=q[j],q[i]
     if (pi[0]==0)!=(q[0]==0):edges.append({i,j})
    self.assertTrue(all(0 in e for e in edges));counts.append(len(edges))
   self.assertEqual(max(counts),n-1)
if __name__=='__main__':unittest.main()
