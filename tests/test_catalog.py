"""Regression checks for mathematical domain and normalization isolation."""
import argparse
import copy
import importlib.util
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('catalog',ROOT/'tools/catalog.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
D=json.loads((ROOT/'data/catalog.json').read_text())
M={m['id']:m for m in D['measures']}
C={c['id']:c for c in D['claims']}
def args(**kw):
 v=dict(A=None,B=None,kind='decision_function',totality='total',class_name=['unrestricted'],historical=False);v.update(kw);return argparse.Namespace(**v)
class CatalogueTests(unittest.TestCase):
 def test_references_and_domains(self):mod.validate(D)
 def test_general_upper_bound_restricts(self):
  c=dict(A='D',B='Q',kind='upper_bound',scope=dict(object_kind='decision_function',totality='total',classes=[]))
  self.assertTrue(mod.matches(c,args(class_name=['symmetric'])))
  c['scope']['classes']=['monotone'];self.assertFalse(mod.matches(c,args()))
 def test_witness_direction(self):
  c=dict(A='D',B='Q',kind='separation',scope=dict(object_kind='decision_function',totality='total',classes=['symmetric','monotone']))
  self.assertTrue(mod.matches(c,args()))
  self.assertTrue(mod.matches(c,args(class_name=['symmetric'])))
  c['scope']['classes']=[];self.assertFalse(mod.matches(c,args(class_name=['symmetric'])))
 def test_promise_and_object_isolation(self):
  c=dict(A='D',B='Q',kind='upper_bound',scope=dict(object_kind='search_relation',totality='partial',classes=[]))
  self.assertFalse(mod.matches(c,args()))
  self.assertTrue(mod.matches(c,args(kind='search_relation',totality='partial')))
 def test_degree_normalizations_stay_separate(self):
  for id in ['deg','cubeBoundedDeg','adeg','cubeBoundedAdeg','bmAdeg']:self.assertIn(id,M)
  self.assertNotEqual(M['deg']['definition'],M['cubeBoundedDeg']['definition'])
  self.assertIn('0/1',M['bmAdeg']['definition'])
 def test_new_preprint_is_not_best_known_certification(self):
  c=C['R-Q4-sep-2026'];self.assertFalse(c['best_known_certified'])
  s=next(s for s in D['sources'] if s['id']==c['source'])
  self.assertEqual(s['publication_status'],'repository_preprint')
 def test_input_length_log_not_suppressed(self):
  c=C['D-rdeg3-n'];self.assertIn('log',c['statement']);self.assertFalse(c['best_known_certified'])
 def test_local_measure_not_globalized(self):
  c=C['fbs0-Qneg'];self.assertEqual(c['A'],'fbs_at0');self.assertFalse(c['scalar_inference_allowed'])
 def test_reject_dangling_reference(self):
  bad=copy.deepcopy(D);bad['claims'][0]['B']='unknown-measure'
  with self.assertRaises(ValueError):mod.validate(bad)
if __name__=='__main__':unittest.main()
