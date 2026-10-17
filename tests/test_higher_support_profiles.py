import unittest,json,itertools,importlib.util,copy
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class HigherSupportProfilesTests(unittest.TestCase):
 def test_independent_quadratic_characters_attain_all_signs(self):
  seen={(x[0]*x[1],x[1]*x[2],x[2]*x[3])for x in itertools.product([-1,1],repeat=4)}
  self.assertEqual(len(seen),8)
  a=[F(1,5),F(-1,3),F(2,7),F(1,11)]
  sup=max(abs(a[0]+sum(a[i+1]*v[i]for i in range(3)))for v in seen)
  self.assertEqual(sup,sum(map(abs,a)))
 def test_general_hypermatching_uses_product_lift_without_direct_witnessing(self):
  d=json.loads((ROOT/'data/profile-matrices.json').read_text());p=next(p for p in d['profiles']if p['profile']=='hypermatching')
  self.assertEqual(sum(c['status']=='not_yet_indexed'for c in p['cells']),0)
  for c in p['cells']:
   if c['B']=='domainS':self.assertIn('lambda-partite-D-sensitivity-product-lift',c['claim_ids']);self.assertNotIn('profile-witnessing-degree-sensitivity',c['claim_ids'])
 def test_profile_guards_and_claim_provenance(self):
  d=json.loads((ROOT/'data/catalog.json').read_text());ids={c['id']for c in d['claims']};ps=json.loads((ROOT/'data/profile-matrices.json').read_text())['profiles']
  for p in ps:
   for c in p['cells']:
    self.assertTrue(set(c.get('claim_ids',[]))<=ids)
    if p['profile']in ['slice','multislice'] and any(v in c.get('claim_ids',[])for v in ['domain-parameterized-domainD-domainBS','domain-parameterized-domainD-domainC']):self.assertIn('M>0',c['assumptions'])
  perm=next(p for p in ps if p['profile']=='permutation');cell=next(c for c in perm['cells']if c['A']=='domainD'and c['B']=='domainS');self.assertEqual(cell['exponent'],'10')
 def test_core_chains_tighten_noncore_without_dropping_endpoint_losses(self):
  d=json.loads((ROOT/'data/extended-completion-inventory.json').read_text());c=next(c for c in d['cells']if c['A']=='completion_D'and c['B']=='completion_Q0');self.assertEqual(c['upper']['exponent'],'4');self.assertIn('D-Q4',c['upper']['claim_ids'])
  spec=importlib.util.spec_from_file_location('ec',ROOT/'tools/extended_completions.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
  core=json.loads((ROOT/'data/completion-matrix.json').read_text());data=json.loads((ROOT/'data/catalog.json').read_text());fake=copy.deepcopy(core)
  for row in fake['cells']:
   if row['base_A']=='D'and row['base_B']=='Q':row['upper'].update(exponent='1/100',endpoint_without_log=False)
  got=m.build(data,fake);cell=next(c for c in got['cells']if c['A']=='completion_D'and c['B']=='completion_Q0');self.assertGreaterEqual(F(cell['upper']['exponent']),1)
