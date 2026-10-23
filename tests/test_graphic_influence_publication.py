import hashlib,json,runpy,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class GraphicInfluencePublicationTests(unittest.TestCase):
 def test_exact_publication_and_download_verifiers_are_manifest_bound(self):
  m=json.loads((ROOT/'data/graphic-influence-proof-audit.json').read_text())
  self.assertEqual(m['verdict'],'passed_fresh_cross_reviewer_audit');self.assertFalse(m['formal_verification']);self.assertFalse(m['priority_certified'])
  for row in [m[k] for k in ['proof','audit','priority']]+m['checkers']:
   self.assertEqual(row['sha256'],hashlib.sha256((ROOT/row['path']).read_bytes()).hexdigest(),row['path'])
 def test_fresh_exhaustive_basis_and_endpoint_allocation_checks(self):
  out=runpy.run_path(str(ROOT/'tests/graphic_influence_independent_check.py'))['out']
  self.assertEqual(out['status'],'PASS');self.assertEqual(out['invertible_bases_exhausted'],168);self.assertEqual(out['signed_polynomials_exhausted'],122304);self.assertEqual(out['distinct_label_weighted_cut_cases'],4980)
  self.assertEqual(out['dependent_label_range_counterexample'],dict(native_oscillation=8,free_graph_oscillation=14))
 def test_exact_author_flow_and_density_checks(self):
  d=runpy.run_path(str(ROOT/'tests/graphic_influence_check.py'))['result']
  self.assertEqual(d['graphic_basis_cases'],315);self.assertEqual(d['induced_density_checks'],22545);self.assertEqual(d['exact_endpoint_flows'],315)
 def test_native_influence_scope_never_becomes_a_global_scalar_bound(self):
  d=json.loads((ROOT/'data/catalog.json').read_text());c=next(c for c in d['claims'] if c['id']=='quadratic-character-native-influence')
  self.assertIsNone(c['A']);self.assertIsNone(c['B']);self.assertIsNone(c['exponent']);self.assertFalse(c['scalar_inference_allowed']);self.assertFalse(c['best_known_certified'])
  self.assertIn('invertibly_quadratic_fourier_character_support',c['scope']['classes']);self.assertIn('Sz76',c['proof_sources'])
  q=next(q for q in d['conjectures'] if q['id']=='AA-bounded-polynomial-influence');self.assertEqual(q['status_audit']['verdict'],'primary_reaffirmed_open');self.assertEqual(q['status_audit']['proof_page'],c['proof_page'])
