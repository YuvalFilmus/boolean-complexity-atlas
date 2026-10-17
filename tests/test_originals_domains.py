"""Protect original-source normalization and non-cube domain isolation."""
import json,math,unittest
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[1]/'data/catalog.json').read_text());C={v['id']:v for v in D['claims']};M={v['id']:v for v in D['measures']}
class OriginalDomainTests(unittest.TestCase):
 def test_original_one_sided_constant_not_certified(self):
  c=C['Nis89-D-R1-square'];self.assertFalse(c['scalar_inference_allowed']);self.assertTrue(c['historical']);self.assertEqual(c['status'],'source_statement_refuted_under_literal_cost_convention')
  # Reject for free with probability 1/2; otherwise query the identity input.
  self.assertLess(2*(1/2)**2,1)
 def test_EH_leaf_recurrence(self):
  def leaves(n,r):
   if not n or not r:return 1
   return leaves(n-1,r)+leaves(n-1,r-1)
  for n in range(1,8):
   for r in range(n+1):self.assertEqual(leaves(n,r),sum(math.comb(n,i)for i in range(r+1)))
 def test_permutation_sensitivity_is_packing_not_degree(self):
  self.assertIn('disjoint',M['permS']['definition']);self.assertIn('not required',M['permEdgeS']['definition'])
  for id in ['permutation-degree-sensitivity','permutation-bs-degree']:
   c=C[id];self.assertEqual(c['scope']['input_alphabet'],'permutation');self.assertIn('symmetric_group',c['scope']['classes'])
 def test_relation_degree_direction_depends_on_totality(self):
  self.assertEqual(C['search-elementary-rel_adeg-rel_udeg']['scope']['totality'],'total')
  self.assertEqual(C['search-elementary-rel_udeg-rel_adeg']['scope']['totality'],'partial_or_total')
 def test_original_pdfs_have_distinct_versions(self):
  s={v['id']:v for v in D['sources']}
  self.assertEqual(s['EH89']['snapshot']['pages'],16);self.assertEqual(s['Nis89']['snapshot']['pages'],9)
  self.assertIn('still not inspected',s['Nis91']['read_version'])
if __name__=='__main__':unittest.main()
