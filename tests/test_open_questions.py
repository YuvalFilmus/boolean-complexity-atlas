import json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from open_questions import work_index,centrality,archived,implication_reach
from matrix import upper_closure
class QuestionEvidenceTests(unittest.TestCase):
 def test_versions_count_once_but_missions_and_derived_claims_do_not_count(self):
  sources=[{'id':'p','title':'A paper','year':2020,'kind':'preprint'},{'id':'j','title':'A paper','year':2022,'kind':'article'},{'id':'s','title':'A survey','year':2023,'kind':'survey'},{'id':'m','title':'Mission','year':2026,'kind':'online_resource'}]
  works,sw=work_index(sources,[])
  d={'measures':[{'id':'X','sources':['p','j','s','m']}], 'claims':[{'id':'unrelated-derivation','A':'X','B':'X','source':'other','status':'repository_derivation_checked'}]}
  count=centrality(d,works,sw)['X'];self.assertEqual(count['count'],2);self.assertEqual(count['research_count'],1);self.assertEqual(count['survey_count'],1);self.assertEqual(len(count['papers'][0]['source_ids']),2)
 def test_archive_does_not_hide_unverified_or_formulation_questions(self):
  for s in ['resolved','refuted_as_literally_stated','reported_refuted_in_primary_preprint']:self.assertTrue(archived(s))
  for s in ['historical_conjecture_current_status_unverified','formulation_or_current_resolution_unverified','still_proposed_in_2026_journal_current_resolution_unverified']:self.assertFalse(archived(s))
 def test_every_published_formulation_is_preserved_and_recurrence_is_work_deduplicated(self):
  data=json.loads((ROOT/'data/open-questions.json').read_text());cat=json.loads((ROOT/'data/catalog.json').read_text());qs={q['id']:q for q in data['questions']}
  self.assertEqual({q['id'] for q in data['questions'] if q['origin']=='published'},{q['id'] for q in cat['conjectures']})
  self.assertEqual(qs['AA-folklore-average-simulation']['recurrence']['count'],5);self.assertEqual(qs['AA-bounded-polynomial-influence']['recurrence']['count'],5)
  self.assertIsNone(qs['AA-bounded-polynomial-influence']['centrality']);self.assertTrue(qs['bs-s-quadratic']['archived'])
  for q in data['questions']:
   if q['origin']!='published':self.assertIsNone(q['recurrence']);self.assertIsNone(q['first_formulation_year'])
 def test_conditional_impact_preserves_total_scope_and_exposes_assumption(self):
  d=json.loads((ROOT/'data/catalog.json').read_text());base,_=upper_closure(d)
  result=implication_reach(d,base,'D','bs',__import__('fractions').Fraction(2))
  self.assertGreater(result['count'],0);self.assertTrue(any(c['A']=='D' and c['B']=='R' and c['after']=='2' for c in result['comparisons']));self.assertIn('unrestricted total Boolean functions',result['assumption'])
  self.assertIsNone(implication_reach(d,base,'completion_D','completion_bs',__import__('fractions').Fraction(2)))

class QuestionStatusAuditTests(unittest.TestCase):
 def test_status_audit_covers_all_active_candidates_without_certifying_a_negative_search(self):
  a=json.loads((ROOT/'data/question-status-audit.json').read_text());d=json.loads((ROOT/'data/catalog.json').read_text());byid={c['id']:c for c in d['conjectures']}
  self.assertEqual(a['summary'],{'primary_reaffirmed_open':6,'no_resolution_found':7,'formulation_unresolved':2})
  self.assertEqual(len(a['records']),15)
  for row in a['records']:
   self.assertTrue(row['evidence']);self.assertTrue(row['queries']);self.assertEqual(byid[row['id']]['status_audit']['checked'],'2026-10-23');self.assertFalse(archived(byid[row['id']]['status']))
   if row['verdict']=='no_resolution_found':self.assertIn('not_certified',byid[row['id']]['status'])
 def test_related_progress_is_not_falsely_counted_as_the_same_question(self):
  data=json.loads((ROOT/'data/open-questions.json').read_text());qs={q['id']:q for q in data['questions']}
  for key in ['D-bs-quadratic','extremal-forrelation-sqrt','KLMY-pure-monomial-AND']:self.assertEqual(qs[key]['recurrence']['count'],2)
  self.assertEqual(qs['domain-q-analog-framework']['recurrence']['count'],1)
  self.assertNotIn('BBCLD26',[m['source'] for m in qs['KLMY-pure-monomial-AND']['mentions']])
  self.assertEqual(qs['AA-folklore-average-simulation']['recurrence']['count'],5)
  self.assertEqual(qs['AA-bounded-polynomial-influence']['recurrence']['count'],5)
