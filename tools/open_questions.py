#!/usr/bin/env python3
"""Build transparent question rankings from scoped, version-deduplicated evidence."""
import copy,json,math,re,unicodedata
from fractions import Fraction
from pathlib import Path
from matrix import CORE,expr_text,expr_value,upper_closure
ROOT=Path(__file__).resolve().parents[1]
CHECKED={'source_checked','primary_statement_and_proof_route_checked','survey_checked','primary_platform_theorem_and_attestation_checked'}

def work_index(sources,versions):
    byid={s['id']:s for s in sources};parent={k:k for k in byid}
    def find(k):
        while parent[k]!=k:k=parent[k]
        return k
    def union(a,b):
        if a in parent and b in parent:parent[find(b)]=find(a)
    def norm(s):return re.sub('[^a-z0-9]','',unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower())
    groups={}
    for s in sources:
        key=norm(s['title'])
        if key in groups:union(groups[key],s['id'])
        else:groups[key]=s['id']
    for v in versions:
        ids=[v[k] for k in ['original','later_manuscript','journal','full','proceedings'] if v.get(k) in byid]
        for sid in ids[1:]:union(ids[0],sid)
    works={};source_work={}
    for s in sources:
        if s.get('kind') in {'online_resource','notes'}:continue
        key=find(s['id']);source_work[s['id']]=key
        w=works.setdefault(key,{'id':key,'source_ids':[],'title':s['title'],'kind':'survey' if s.get('kind')=='survey' else 'research','year':s['year']})
        w['source_ids'].append(s['id']);w['year']=min(w['year'],s['year'])
        if s.get('kind')!='survey':w['kind']='research'
    return works,source_work

def centrality(d,works,source_work):
    evidence={m['id']:{} for m in d['measures']}
    def add(mid,sid,why):
        if mid in evidence and sid in source_work:
            a=evidence[mid].setdefault(source_work[sid],{'source_ids':set(),'records':set()});a['source_ids'].add(sid);a['records'].add(why)
    for m in d['measures']:
        for s in m['sources']:add(m['id'],s,'measure definition/reference')
        for a in m.get('aliases',[]):
            if a.get('status')=='source_checked':add(m['id'],a['source'],'checked notation: '+a.get('text',''))
    for c in d['claims']:
        if c['status'] not in CHECKED:continue
        for mid in [c.get('A'),c.get('B')]+[f['measure'] for f in c.get('factors',[])]:add(mid,c['source'],c['id'])
    return {mid:{'count':len(ws),'research_count':sum(works[k]['kind']=='research' for k in ws),'survey_count':sum(works[k]['kind']=='survey' for k in ws),'papers':[{'work_id':k,'source_ids':sorted(v['source_ids']),'evidence_records':sorted(v['records'])} for k,v in sorted(ws.items())]} for mid,ws in evidence.items()}

def archived(status):return bool(re.match(r'^(resolved|refuted|reported_refuted)',status))

def rational(e):
    if not isinstance(e,dict):return Fraction(str(e))
    if e['op'] in ['log_ratio','sqrt']:return None
    a,b=rational(e['left']),rational(e['right'])
    if a is None or b is None:return None
    return {'add':lambda:a+b,'mul':lambda:a*b,'div':lambda:a/b}[e['op']]()

def implication_reach(d,baseline,a,b,p):
    if a not in CORE or b not in CORE or p is None:return None
    c={'id':'hypothetical-question-bound','A':a,'B':b,'exponent':str(p),'kind':'upper_bound','loss':'none','status':'repository_derivation_checked','scope':{'object_kind':'decision_function','totality':'total','classes':[]}}
    new,_=upper_closure({**d,'claims':[*d['claims'],c]});improvements=[]
    for x in CORE:
        for y in CORE:
            if x==y or (x,y) not in baseline or (x,y) not in new:continue
            old,v=baseline[x,y],new[x,y]
            if v['exponent']<old['exponent'] or (v['exponent']==old['exponent'] and v['endpoint_without_log'] and not old['endpoint_without_log']):
                improvements.append({'A':x,'B':y,'before':str(old['exponent']),'after':str(v['exponent']),'endpoint_improved':not old['endpoint_without_log'] and v['endpoint_without_log']})
    return {'count':len(improvements),'assumption':f'{a}(f)=O({b}(f)^({p})) with a pure endpoint, for unrestricted total Boolean functions','comparisons':improvements,'warning':'Conditional upper-bound closure over the twelve core measures only; not a proof, difficulty estimate or count of all mathematical consequences.'}

def build(d,annotations,versions,core,completion):
    works,source_work=work_index(d['sources'],versions);cent=centrality(d,works,source_work);sources={s['id']:s for s in d['sources']};ms={m['id'] for m in d['measures']};claims={c['id']:c for c in d['claims']};baseline,_=upper_closure(d)
    notes={q['id']:q for q in annotations['questions']};out=[]
    def enrich(q):
        q['activity_sources']=[sid for sid in q.get('activity_sources',[]) if sid in sources]
        ids=q['measure_ids'];counts=[cent[m]['count'] for m in ids]
        q['centrality']=math.prod(counts)**(1/len(counts)) if counts and all(counts) else None
        q['centrality_counts']={m:cent[m]['count'] for m in ids}
        sightings={}
        for mention in q['mentions']:
            if mention['source'] in source_work:sightings.setdefault(source_work[mention['source']],[]).append(mention)
        q['recurrence']={'count':len(sightings),'research_count':sum(works[k]['kind']=='research' for k in sightings),'survey_count':sum(works[k]['kind']=='survey' for k in sightings),'works':[{'work_id':k,'passages':v} for k,v in sightings.items()]} if sightings else None
        q['first_formulation_year']=min((sources[m['source']]['year'] for m in q['mentions']),default=None)
        q['latest_activity_year']=max((sources[s]['year'] for s in q.get('activity_sources',[]) if s in sources),default=q['first_formulation_year'])
        q['scope_label']={'total':'Total functions','partial':'Partial functions','completion':'Minimum completions','search-total':'Total search','distributional':'Distributional / real polynomials','other':'Other domains'}.get(q['context'],q['context'])
        for mid in ids:
            if mid not in ms:raise ValueError('Unknown question measure '+mid)
        out.append(q)
    core_by={(c['A'],c['B']):c for c in core['cells']}
    for c in d['conjectures']:
        n=notes.get(c['id'],{'measure_ids':[],'context':'other','mentions':[],'mapping_note':'Measure mapping not assessed.'});pair=n.get('pair');reach=implication_reach(d,baseline,pair['A'],pair['B'],Fraction(pair['exponent'])) if pair else None
        q={'id':c['id'],'origin':'published','statement':c['statement'],'statement_latex':c.get('statement_latex'),'measure_ids':n['measure_ids'],'context':n['context'],'mentions':n['mentions'],'mapping_note':n.get('mapping_note',''),'status':c['status'],'archived':archived(c['status']),'formulation_review':bool(re.search('formulation|precise_exponent',c['status'])),'status_note':'Status is retained from the cited catalogue audit; inclusion does not certify a current open problem.','activity_sources':list(dict.fromkeys([c['source'],*c.get('status_sources',[]),*([c['status_source']] if c.get('status_source') else []),*[claims[cid]['source'] for cid in c.get('resolution',[]) if cid in claims],*[m['source'] for m in n['mentions']]])),'implications':c.get('implications',[]),'implication_reach':reach,'gap':None,'comparison':None,'status_snapshot_date':c.get('status_date',c.get('status_checked',d.get('audit_date'))),'catalogue_record':c}
        if pair:
            rec=core_by.get((pair['A'],pair['B']));q['comparison']={'A':pair['A'],'B':pair['B'],'context':'total'}
            if rec and rec.get('lower') and rec.get('upper'):q['gap']=gap_record(rec)
        enrich(q)
    # Inventory gaps are explicitly distinct from published open questions.
    named_pairs={(q['comparison']['context'],q['comparison']['A'],q['comparison']['B']) for q in out if not q['archived'] and q.get('comparison')}
    for context,dataset in [('total',core),('completion',completion)]:
        for c in dataset['cells']:
            if (context,c['A'],c['B']) in named_pairs or c['A']==c['B'] or not c.get('lower') or not c.get('upper'):continue
            g=gap_record(c)
            if not g or (g['width']<=1e-9 and not g['endpoint_loss']):continue
            ids=list(dict.fromkeys([*c['lower'].get('claim_ids',[]),*c['upper'].get('claim_ids',[])]));refs=list(dict.fromkeys(claims[k]['source'] for k in ids if k in claims and claims[k]['source'] in sources))
            p=rational(c['lower'].get('exponent_expression',c['lower'].get('exponent')))
            # An exact transcendental endpoint is not rounded into a hypothetical rational theorem.
            reach=implication_reach(d,baseline,c['A'],c['B'],p) if context=='total' else None
            enrich({'id':'gap-'+context+'-'+c['A']+'-'+c['B'],'origin':'endpoint' if g['width']<=1e-9 else 'gap','statement':'Can the recorded upper and lower bounds be brought together?' if g['width']>1e-9 else 'Can the recorded upper endpoint loss be removed?','measure_ids':[c['A'],c['B']],'context':context,'mentions':[],'mapping_note':'This is a recorded comparison gap, not an independently verified open problem.','status':'recorded_gap_current_openness_not_certified','status_note':'No claim that this exact question was posed in any cited paper. References support the bounds.','archived':False,'formulation_review':False,'activity_sources':refs,'implications':[],'implication_reach':reach,'gap':g,'comparison':{'A':c['A'],'B':c['B'],'context':context},'claim_ids':ids})
    return {'as_of':annotations['as_of'],'methodology':{'centrality':'Geometric mean of distinct indexed scholarly-work counts for the mapped measures. Surveys included; web missions, notes, derived claims and citation-only proof_sources excluded. Definition/notation references and direct checked comparison records supply the evidence. Counts are lower counts within this corpus, not a full-text census.','recurrence':'Distinct works with a curated passage discussing this same question; survey and research counts shown separately. Paper versions count once. Bound citations alone are not question mentions.','implication_reach':'Number of improved ordered core upper-bound comparisons under the stated hypothetical pure bound, preserving scope. Not assessed for unsupported models or nonrational target endpoints.','gap':'Upper exponent minus lower exponent, only when both finite endpoints are recorded. Endpoint losses are listed separately and have no exponent-gap score.','recent':'Latest year of a recorded substantive source, formulation or bound in the entry. Access dates are not activity dates.','longevity':'Earliest formulation year verified in the listed question passages; inferred gaps have no historical origin assigned.','missing':'Missing or inapplicable ranking values are null, displayed as not assessed and sorted last. There is no combined importance score.','scope_warning':'Centrality may be compared across domains, but mathematical bounds and conditional implications never transfer across domains without recorded evidence.','version_policy':'Merge exact normalized titles and explicitly audited version families; this is a conservative editorial work index, available for inspection.'},'works':list(works.values()),'centrality':cent,'questions':out,'summary':{'published':sum(q['origin']=='published' and not q['archived'] for q in out),'archive':sum(q['archived'] for q in out),'gaps':sum(q['origin']=='gap' for q in out),'endpoint_questions':sum(q['origin']=='endpoint' for q in out),'scholarly_works':len(works)}}

def gap_record(c):
    lo=c['lower'].get('numeric_for_ranking');up=c['upper'].get('exponent')
    try:upper=float(Fraction(str(up)))
    except (ValueError,TypeError,ZeroDivisionError):return None
    if lo is None or not math.isfinite(lo) or not math.isfinite(upper):return None
    width=max(0.,upper-lo)
    return {'lower':lo,'upper':upper,'lower_expression':c['lower'].get('exponent_expression',c['lower'].get('exponent')),'lower_label':expr_text(c['lower'].get('exponent_expression',c['lower'].get('exponent'))),'width':width,'score':width if width>1e-9 else None,'endpoint_loss':c['upper'].get('endpoint_without_log') is False,'claim_ids':list(dict.fromkeys([*c['lower'].get('claim_ids',[]),*c['upper'].get('claim_ids',[])]))}

def from_files():
    read=lambda name:json.loads((ROOT/'data'/name).read_text())
    return build(read('catalog.json'),read('question-annotations.json'),read('journal-version-audit.json'),read('core-matrix.json'),read('extended-completion-exponents.json'))
if __name__=='__main__':
    result=from_files();(ROOT/'data/open-questions.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n');print('Open questions:',result['summary'])
