import hashlib,html,json,runpy,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import proof_pages
class HypermatchingPublicationTests(unittest.TestCase):
 def test_exact_published_packet_is_manifest_bound(self):
  a=json.loads((ROOT/'data/hypermatching-proof-audit.json').read_text())
  self.assertEqual(a['verdict'],'passed_after_explicit_output_transposition_repair')
  self.assertFalse(a['formal_verification']);self.assertFalse(a['priority_certified'])
  for k in ['proof','audit','priority']:self.assertEqual(a[k]['sha256'],hashlib.sha256((ROOT/a[k]['path']).read_bytes()).hexdigest(),k)
  proof=(ROOT/a['proof']['path']).read_text();self.assertIn('range over all tableaux',proof);self.assertIn('output-value transposition',proof)
 def test_covariance_and_lower_filtration_are_checked_on_the_original_characters(self):
  d=runpy.run_path(str(ROOT/'tests/hypermatching_import_check.py'))
  self.assertEqual(d['covariance_checks'],3434);self.assertEqual(d['orthogonality_checks'],1467)
 def test_fiber_mobius_formula_and_half_degree_check(self):
  d=runpy.run_path(str(ROOT/'tests/hypermatching_fiber_check.py'))
  for lam in [(2,),(1,1),(2,1)]:self.assertGreater(d['check'](lam,2,2)['exact_comparisons'],0)
 def test_new_bound_stays_in_its_full_hypermatching_profiles(self):
  d=json.loads((ROOT/'data/profile-matrices.json').read_text());cat=json.loads((ROOT/'data/catalog.json').read_text())
  claim=next(c for c in cat['claims'] if c['id']=='hypermatching-degree-sensitivity-descent');self.assertFalse(claim['scalar_inference_allowed']);self.assertFalse(claim['best_known_certified'])
  for p in d['profiles']:
   cell=next(c for c in p['cells'] if c['A']=='domainDegree' and c['B']=='domainS')
   if p['profile'] in ['hypermatching','uniform-hypermatching']:
    self.assertEqual(cell['exponent'],'2');self.assertEqual(cell['claim_ids'],[claim['id']]);self.assertIn('(2k-1);',p['coefficient_definitions']['K_H'])
   else:self.assertNotIn(claim['id'],cell['claim_ids'])
 def test_native_cube_faces_and_fixed_axes(self):
  runpy.run_path(str(ROOT/'tests/hypermatching_cube_faces_check.py'))
 def test_proof_renderer_escapes_text_and_rejects_unsafe_links(self):
  self.assertIn('&lt;script&gt;',proof_pages.inline('<script>'))
  with self.assertRaises(ValueError):proof_pages.inline('[bad](javascript:alert)')
  self.assertIn('data-display="true"',proof_pages.inline('$$x^2$$'))
  self.assertIn('hypermatching-audit.html',proof_pages.inline('[audit](hypermatching-full-source-audit.md)'))
