import hashlib,json,runpy,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class RoundFourPublicationTests(unittest.TestCase):
 def test_published_sources_and_downloaded_verifiers_have_exact_hashes(self):
  for family in ['width-three','rooted-paths']:
   m=json.loads((ROOT/'data'/(family+'-proof-audit.json')).read_text())
   self.assertEqual(m['verdict'],'passed_fresh_cross_reviewer_audit')
   self.assertFalse(m['formal_verification']);self.assertFalse(m['priority_certified'])
   for row in [m[k] for k in ['proof','audit','priority']]+m['checkers']:
    self.assertEqual(row['sha256'],hashlib.sha256((ROOT/row['path']).read_bytes()).hexdigest(),row['path'])
 def test_fresh_four_query_certificate_uses_exact_table_and_input_pairs(self):
  d=runpy.run_path(str(ROOT/'tests/width_three_independent_check.py'));r=d['result']
  self.assertEqual((r['automorphisms'],r['orbit_unknowns'],r['constraint_rank'],r['affine_dimension']),(48,10,8,2))
  self.assertEqual(r['quadratic_scales'],['1','-2','2']);self.assertTrue(r['matching_is_exact_KRS_4MAJ_partition'])
 def test_basis_averaging_independently_checks_same_scalar_image(self):
  d=runpy.run_path(str(ROOT/'tests/width_three_check.py'))
  self.assertEqual(len(d['ms']),272)
 def test_rooted_path_exact_moments_and_truncation(self):
  runpy.run_path(str(ROOT/'tests/rooted_paths_independent_check.py'))
 def test_scope_guards_and_sharp_import_are_preserved(self):
  d=json.loads((ROOT/'data/catalog.json').read_text());c={c['id']:c for c in d['claims']}
  for key in ['four-query-4maj-certificate-obstruction','rooted-path-native-influence']:
   self.assertIsNone(c[key]['exponent']);self.assertFalse(c[key]['scalar_inference_allowed']);self.assertFalse(c[key]['best_known_certified'])
  p=c['rooted-path-native-influence'];self.assertIsNone(p['A']);self.assertIsNone(p['B']);self.assertIn('Sz76',p['proof_sources'])
  self.assertIn('ancestor_descendant_tree_path_fourier_support',p['scope']['classes'])
  qs={q['id']:q for q in d['conjectures']}
  self.assertEqual(qs['AA-bounded-polynomial-influence']['status_audit']['verdict'],'primary_reaffirmed_open')
  self.assertEqual(qs['BK24-search-QE-R']['status_audit']['verdict'],'no_resolution_found')
