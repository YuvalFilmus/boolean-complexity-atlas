import hashlib,json,runpy,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import catalog,search_matrices,proof_pages
class ExactSearchPublicationTests(unittest.TestCase):
 def test_exact_proof_and_audits_are_bound_to_manifest(self):
  m=json.loads((ROOT/'data/exact-search-proof-audit.json').read_text())
  self.assertEqual(m['verdict'],'passed_fresh_independent_source_audit')
  self.assertFalse(m['formal_verification']);self.assertFalse(m['priority_certified'])
  for key in ['proof','audit','priority']:
   self.assertEqual(m[key]['sha256'],hashlib.sha256((ROOT/m[key]['path']).read_bytes()).hexdigest())
 def test_independent_fractional_feasibility_check(self):
  d=runpy.run_path(str(ROOT/'tests/exact_search_independent_check.py'))
  self.assertEqual(d['counts'],{2:1431,3:268});self.assertEqual(d['hall_feasible'],1431)
 def test_singleton_recovery_against_independent_tree_depth(self):
  d=runpy.run_path(str(ROOT/'tests/exact_search_two_query_check.py'))
  self.assertEqual(d['tables'],146);self.assertEqual(d['mixed_counts'],{1:0,2:83191,3:1036})
 def test_small_budget_theorem_never_becomes_global_power(self):
  d=json.loads((ROOT/'data/catalog.json').read_text());c=next(c for c in d['claims'] if c['id']=='exact-search-two-query-rigidity')
  self.assertIsNone(c['exponent']);self.assertFalse(c['scalar_inference_allowed'])
  self.assertEqual(c['scope']['totality'],'total');self.assertIn('exact_quantum_at_most_two_queries',c['scope']['classes'])
  mats=search_matrices.build(d)['matrices']
  total=next(m for m in mats if m['totality']=='total' and m['group']=='query_and_lower_bounds')
  promise=next(m for m in mats if m['totality']=='partial' and m['group']=='query_and_lower_bounds')
  get=lambda m:next(x for x in m['cells'] if x['A']=='D' and x['B']=='QE')['records']
  self.assertIn(c['id'],[x['claim_id'] for x in get(total)])
  self.assertNotIn(c['id'],[x['claim_id'] for x in get(promise)])
 def test_priority_tables_render_with_safe_cells(self):
  out=proof_pages.markdown("| Source | Version |\n|---|---|\n| <bad> | checked |")
  self.assertIn("<table>",out);self.assertIn("&lt;bad&gt;",out);self.assertNotIn("<bad>",out)
 def test_asymptotic_question_remains_unresolved_with_proof_link(self):
  d=json.loads((ROOT/'data/catalog.json').read_text());q=next(q for q in d['conjectures'] if q['id']=='BK24-search-QE-R')
  self.assertEqual(q['status_audit']['verdict'],'no_resolution_found')
  self.assertEqual(q['status_audit']['proof_page'],'proofs/exact-search.html')
  self.assertIn('exact-search-audit.html',proof_pages.inline('[audit](exact-search-full-source-audit.md)'))
