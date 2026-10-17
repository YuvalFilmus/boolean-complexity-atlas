import unittest,importlib.util,json,itertools
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def module(name):
 spec=importlib.util.spec_from_file_location(name,ROOT/'tools'/f'{name}.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
class InventoryRepairTests(unittest.TestCase):
 def test_elementary_completion_paths_admitted(self):
  d=json.loads((ROOT/'data/catalog.json').read_text());cs={c['id']:c for c in d['claims']};e=module('extended_completions')
  for k in ['C-UC','bs-fbs','FC-C','Q0-QE','Q0-R0']:self.assertTrue(e.eligible(cs[k]),k)
  self.assertFalse(e.eligible(cs['D-Q6-history']))
 def test_domain_oracles_and_parameters_excluded_from_uniform_closure(self):
  d=module('domain_matrix').build(json.loads((ROOT/'data/catalog.json').read_text()));self.assertEqual(len(d['cells']),132)
  paths={k for c in d['cells'] for k in c.get('claim_ids',[])}
  self.assertFalse(paths.intersection(d['parameterized_claim_ids']+d['other_oracle_claim_ids']))
  self.assertIn('BD16-domainD-domainQ',d['other_oracle_claim_ids'])
 def test_l1_norm_bound_including_zero_perturbation(self):
  for coeffs in itertools.product([-2,-1,0,1,2],repeat=3):
   for x in itertools.product([-1,1],repeat=3):
    q=1+sum(a*b for a,b in zip(coeffs,x));self.assertLessEqual(abs(q),1+sum(map(abs,coeffs)))
