"""Checks that the matrix respects provenance, domains, and exponent direction."""
import importlib.util,json,math
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('matrix',ROOT/'tools/matrix.py');matrix=importlib.util.module_from_spec(spec);spec.loader.exec_module(matrix)
D=json.loads((ROOT/'data/catalog.json').read_text())
RESULT=matrix.build(D);CELLS={(c['A'],c['B']):c for c in RESULT['cells']}
class MatrixTests(unittest.TestCase):
 def test_complete_core_grid(self):
  self.assertEqual(len(CELLS),144)
  self.assertEqual(sum(a!=b for a,b in CELLS),132)
 def test_no_inconsistent_interval(self):
  for c in CELLS.values():self.assertLessEqual(c['lower']['numeric_for_ranking'],float(c['upper']['exponent'])+1e-10)
 def test_logarithmic_endpoint_preserved(self):self.assertFalse(CELLS['R0','R']['upper']['endpoint_without_log'])
 def test_mixed_upper_bound_used(self):
  self.assertEqual(CELLS['C','s']['upper']['exponent'],'5')
  self.assertIn('C-bs-s',CELLS['C','s']['upper']['claim_ids'])
 def test_exact_historical_exponent(self):
  self.assertAlmostEqual(CELLS['s','deg']['lower']['numeric_for_ranking'],math.log(6)/math.log(3))
  v=CELLS['deg','R0']['lower']['numeric_for_ranking']
  self.assertAlmostEqual(v,math.log(2)/math.log((1+math.sqrt(33))/4))
  self.assertLess(v,1.33) # Historical rounded label must not become a stronger theorem.
 def test_preprint_caveat_survives_transfer(self):
  self.assertEqual(CELLS['R','Q']['lower']['numeric_for_ranking'],4)
  self.assertEqual(CELLS['R','Q']['source_publication_statuses']['OAI26'],'repository_preprint')
 def test_no_historical_table_import(self):
  empty=dict(D,claims=[],matrix_baseline_witness=D['matrix_baseline_witness'])
  U,excluded=matrix.upper_closure(empty)
  self.assertNotIn(('D','Q'),U)
 def test_restricted_and_partial_upper_bounds_excluded(self):
  import copy
  c=copy.deepcopy(next(c for c in D['claims'] if c['id']=='D-Q4'))
  c['scope']['classes']=['symmetric'];self.assertFalse(matrix.eligible(c))
  c['scope']['classes']=[];c['scope']['totality']='partial';self.assertFalse(matrix.eligible(c))
 def test_matrix_evidence_refs_exist(self):
  ids={c['id'] for c in D['claims']}
  for c in CELLS.values():
   for side in ['lower','upper']:self.assertLessEqual(set(c[side]['claim_ids']),ids)
if __name__=='__main__':unittest.main()
