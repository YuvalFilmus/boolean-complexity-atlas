#!/usr/bin/env python3
"""Validate, browse, and export the source catalogue; standard library only."""
import argparse
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data/catalog.json'


def validate(d):
    errors = []
    groups = ['sources', 'measures', 'claims', 'conjectures', 'leads']
    ids = {}
    for group in groups:
        seq = [x['id'] for x in d[group]]
        if len(seq) != len(set(seq)):
            errors.append(f'duplicate IDs in {group}')
        ids[group] = set(seq)
    def check(value, group, where):
        if value not in ids[group]:
            errors.append(f'{where}: unknown {group} ID {value}')
    for m in d['measures']:
        for source in m['sources']:
            check(source, 'sources', m['id'])
        for field in ['aliases','alias_candidates','alias_attribution_history','repository_display_variants']:
            for alias in m.get(field,[]):
                check(alias['source'], 'sources', m['id'])
                if alias.get('status')=='source_checked' and not alias.get('locator'):
                    errors.append(m['id']+': checked alias lacks locator')
    for c in d['claims']:
        for field in ['A', 'B']:
            if c[field] is not None:
                check(c[field], 'measures', c['id'])
        for factor in c.get('factors', []):
            check(factor['measure'], 'measures', c['id'])
        if c['source'] != 'definitions':
            check(c['source'], 'sources', c['id'])
        for source in c.get('proof_sources',[]):
            check(source, 'sources', c['id'])
        for dep in c.get('depends_on', []):
            check(dep, 'claims', c['id'])
        for sup in c.get('superseded_by', []):
            check(sup, 'claims', c['id'])
        for field in ['statement', 'locator', 'proof_summary', 'status', 'scope', 'loss']:
            if not c.get(field):
                errors.append(f'{c["id"]}: empty {field}')
        if c['exponent'] is not None:
            try:
                if Fraction(str(c['exponent'])) < 0:
                    raise ValueError()
            except (ValueError, ZeroDivisionError):
                errors.append(f'{c["id"]}: invalid exponent')
        s = c['scope']
        if s['object_kind'] not in {'decision_function', 'search_relation', 'multi_output_function', 'real_valued_function', 'hazard_free_extension'}:
            errors.append(f'{c["id"]}: invalid object kind')
        if s['totality'] not in {'total', 'partial', 'partial_or_total'}:
            errors.append(f'{c["id"]}: invalid totality')
        if c.get('best_known_certified') and c['status'] in {'secondary_checked', 'statement_checked_proof_pending'}:
            errors.append(f'{c["id"]}: premature best-known certification')
    witness_ids={w['id'] for w in d.get('witnesses',[])}
    if len(witness_ids)!=len(d.get('witnesses',[])):
        errors.append('duplicate witness IDs')
    for c in d['claims']:
        if c.get('witness_id') and c['witness_id'] not in witness_ids:
            errors.append(c['id']+': missing shared witness')
    for v in d.get('priority_audits',[]):
        for source in v['sources']:check(source,'sources',v['id'])
    for group in ['reductions','algorithmic_bounds','problem_classes']:
        for v in d.get(group,[]):
            check(v['source'],'sources',v['id'])
            for source in v.get('proof_sources',[]):check(source,'sources',v['id'])
    for v in d.get('literature_searches',[]):
        for source in v.get('primary_hits',[]):check(source,'sources',v['id'])
    for c in d['conjectures']:
        check(c['source'], 'sources', c['id'])
        for dep in c.get('resolution', []):
            check(dep, 'claims', c['id'])
    for pair in d.get('pair_summaries', []):
        check(pair['A'], 'measures', 'pair')
        check(pair['B'], 'measures', 'pair')
        for field in ['upper_claim', 'lower_claim']:
            if pair[field]:
                check(pair[field], 'claims', 'pair')
    for witness in d.get('witnesses', []):
        if witness.get('source'):
            check(witness['source'], 'sources', witness['id'])
    for witness in d.get('witnesses',[]):
        for source in witness.get('proof_sources',[]):check(source,'sources',witness['id'])
    if errors:
        raise ValueError('\n'.join(errors))
    return f'Validated {len(d["measures"])} measures, {len(d["claims"])} claims, {len(d["sources"])} sources. Structural checks only; no mathematical completeness claim.'


def matches(c, args):
    if getattr(args, 'A', None) and c['A'] != args.A:
        return False
    if getattr(args, 'B', None) and c['B'] != args.B:
        return False
    s = c['scope']
    if args.kind and s['object_kind'] != args.kind:
        return False
    # Claims applying to both promised and total inputs are applicable in either query.
    if args.totality and s['totality'] not in {args.totality, 'partial_or_total'}:
        return False
    # A general-class theorem applies in a restricted class, but a restricted theorem
    # must not appear in an unqualified domain query. Unfiltered queries display all.
    if args.class_name is not None:
        requested = set(args.class_name) - {'unrestricted'}
        recorded = set(s['classes'])
        existential = c['kind'] in {'separation', 'no_polynomial_bound', 'superpolynomial_separation'}
        if existential:
            # A symmetric-and-monotone witness is a witness in either superclass.
            if not requested.issubset(recorded):
                return False
        elif not recorded.issubset(requested):
            return False
    if not args.historical and c.get('historical'):
        return False
    return True


def bibtex(d):
    out = ['% Generated from data/catalog.json. Preserve the source JSON as authoritative.', '% Preprint entries do not imply absence of a later published version.\n']
    for r in d['sources']:
        kind = 'book' if r.get('kind')=='book' else ('article' if r.get('journal') else ('inproceedings' if r.get('booktitle') else 'misc'))
        fields = dict(author=r.get('bibtex_author',' and '.join(r['authors'])), title='{'+r['title']+'}', year=str(r['year']))
        for key in ['journal', 'booktitle', 'publisher', 'series', 'volume', 'number', 'pages', 'doi', 'url', 'eprint', 'edition']:
            if key in r:
                fields[key] = str(r[key])
        if r.get('eprint'):
            fields['archivePrefix'] = 'arXiv'
        notes = [str(r[k]) for k in ['report', 'metadata_note', 'related_publication', 'publication_status'] if r.get(k)]
        if r.get('article_number'):
            notes.append('Article '+str(r['article_number']))
        if r.get('read_version'):
            notes.append('Inspected source: '+r['read_version'])
        if notes:
            fields['note'] = '; '.join(notes)
        def textext(v):
            replacements={'&':r'\&','%':r'\%','_':r'\_','#':r'\#','^':r'\textasciicircum{}','~':r'\textasciitilde{}'}
            return ''.join(replacements.get(ch,ch) for ch in v)
        fields={k:(textext(v) if k not in ['url','doi','eprint','archivePrefix'] else v) for k,v in fields.items()}
        out.append('@'+kind+'{'+r['id']+',\n'+',\n'.join('  '+k+' = {'+v+'}' for k,v in fields.items())+'\n}\n')
    return '\n'.join(out)


def export(d):
    (ROOT/'bibliography.bib').write_text(bibtex(d))
    rmap = {r['id']:r for r in d['sources']}
    lines = ['# Annotated surveys', '', 'Generated from the source catalogue. These are entry points, not certifications of current best bounds.', '']
    for r in d['sources']:
        if r['kind'] == 'survey':
            lines += [f'## {r["id"]}', '', f'{", ".join(r["authors"])}. [{r["title"]}]({r["url"]}) ({r["year"]}).', '', r['annotation'], '']
    lines += ['## Results papers with useful overview tables', '', '[ABK16](https://arxiv.org/abs/1511.01937), Section 2.3, and [ABKBRT21](https://arxiv.org/abs/2010.12629), Table 1. Both require forward-citation updates before their tables are treated as current.', '']
    lines += ['', '## Promise and search reading routes', '', 'For promises, combine Amb18 and Aar21survey with the polynomial conventions in AB23 and ABK21. For search, BK24, GIPS21, CDM23 and AGL26 provide useful introductory comparisons and precise definitions; they remain research papers rather than survey entries. See [the search audit](search-problems.md) and [the promise audit](partial-functions.md).', '']
    (ROOT/'docs/surveys.md').write_text('\n'.join(lines))
    lines = ['# Source-linked claims', '', 'Generated from data/catalog.json. This is an expanding, incomplete catalogue. Status labels describe the evidence inspected; none of these entries is certified globally best-known.', '']
    for c in d['claims']:
        s = c['scope']
        source = 'Repository proof' if c['source']=='definitions' else f'[{c["source"]}]({rmap[c["source"]]["url"]})'
        lines += [f'## {c["id"]}', '', c['statement'], '', f'- Kind: {c["kind"]}; domain: {s["totality"]} {s["object_kind"]}; classes: {", ".join(s["classes"]) or "unrestricted"}.', f'- Evidence: {c["status"]}; loss: {c["loss"]}.', f'- Source: {source}, {c["locator"]}.', f'- Proof: {c["proof_summary"]}', '']
        if c.get('depends_on'):
            lines += ['Dependencies: '+', '.join(c['depends_on'])+'.', '']
        if c.get('historical'):
            lines += ['Historical result; inspect superseding records before selecting a frontier.', '']
        if rmap.get(c['source'], {}).get('publication_status'):
            lines += ['Publication status: '+rmap[c['source']]['publication_status']+'.', '']
        if c.get('notes'):
            lines += [c['notes'], '']
    (ROOT/'docs/claims.md').write_text('\n'.join(lines))
    lines = ['# Measures and notation', '', 'Generated from data/catalog.json. Alias lists are seeds; exact occurrences and full historical coverage remain to be audited. Stable IDs, not symbols, identify measures.', '']
    for m in d['measures']:
        lines += [f'## {m["id"]}: {m["name"]}', '', f'Symbol: `{m["symbol"]}`. Definition status: {m["definition_status"]}.', '', m['definition'], '', m.get('notes',''), '']
        if m.get('definition_locator'):
            lines += ['Definition locator: '+m['definition_locator']+'.', '']
        for a in m['aliases']:
            lines += ['- Alias `'+a['text']+'`: ['+a['source']+']('+rmap[a['source']]['url']+'), '+a.get('locator','exact occurrence pending')+'; '+a.get('status','pending')+'.']
        if m.get('alias_candidates') or m.get('repository_display_variants'):
            lines += ['', 'Unverified occurrences / repository variants (not established historical notation):']
            for a in m.get('alias_candidates',[])+m.get('repository_display_variants',[]):
                lines += ['- `'+a['text']+'`: '+a['source']+'; '+a.get('status','pending')+'.']
        if m.get('alias_attribution_history'):
            lines += ['', 'Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.']
        lines += ['', 'Sources: '+', '.join('['+s+']('+rmap[s]['url']+')' for s in m['sources'])+'.', '']
    (ROOT/'docs/measures.md').write_text('\n'.join(lines))
    lines = ['# Conjectures and research queue', '', 'Historical conjectures are preserved. “Current status unverified” means precisely that; it does not mean open.', '']
    for c in d['conjectures']:
        lines += [f'## {c["id"]}', '', c['statement'], '', 'Status: '+c['status']+'.', '', f'Source: [{c["source"]}]({rmap[c["source"]]["url"]}), {c["locator"]}.', '', *['- '+i for i in c['implications']], '']
        if c.get('resolution'):
            lines += ['Resolution records: '+', '.join(c['resolution'])+'.', '']
    for lead in d['leads']:
        lines += [f'## Queue: {lead["id"]}', '', lead.get('action',''), '', 'Status: '+lead['status']+'.', '']
        if lead.get('url'):
            lines += ['[Primary source]('+lead['url']+')', '']
    (ROOT/'docs/research-queue.md').write_text('\n'.join(lines))
    lines = ['# Recorded exponent overview', '',
             'These rows summarize the cited evidence in the repository, not a completed literature audit. Matching exponents identify the infimum exponent subject to correctness of the cited theorems; logarithmic or subpolynomial lower-bound losses do not establish constant-factor tightness. See each claim for its evidence status. Incomplete rows must not be labelled best-known.', '',
             '| A | B | Domain | Recorded lower exponent | Recorded upper exponent | Evidence |',
             '|---|---|---|---:|---:|---|']
    for pair in d.get('pair_summaries', []):
        s = pair['scope']
        domain = s['totality']+' '+(', '.join(s['classes']) or 'unrestricted')
        lines.append(f'| {pair["A"]} | {pair["B"]} | {domain} | {pair["lower"]} | {pair["upper"] if pair["upper"] is not None else "—"} | {pair["status"]}; {pair["lower_claim"]}; {pair["upper_claim"] or ""} |')
    lines += ['', 'Recent repository preprints are explicitly labelled in the claim records. Equality of recorded endpoint exponents does not certify the correctness or publication status of a new preprint.', '']
    (ROOT/'docs/exponents.md').write_text('\n'.join(lines))
    from collections import Counter, defaultdict
    counts = dict(measure_entries=len(d['measures']), definition_statuses=dict(Counter(m['definition_status'] for m in d['measures'])), claim_records=len(d['claims']), claim_statuses=dict(Counter(c['status'] for c in d['claims'])), bibliographic_records=len(d['sources']), surveys=sum(r['kind']=='survey' for r in d['sources']), pair_summaries=len(d.get('pair_summaries',[])), audited_as_of=d.get('audit_date'), exhaustive=False, globally_best_known_certified=sum(bool(c.get('best_known_certified')) for c in d['claims']))
    (ROOT/'data/coverage.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n')
    by_symbol = defaultdict(set)
    for m in d['measures']:
        by_symbol[m['symbol']].add(m['id'])
        for a in m['aliases']:
            by_symbol[a['text']].add(m['id'])
    lines = ['# Notation collisions', '', 'Exact display-string collisions only; visually equivalent TeX is not normalized. A collision does not assert equivalence.', '']
    for symbol, mids in sorted(by_symbol.items()):
        if len(mids)>1:
            lines += ['- `'+symbol+'`: '+', '.join(sorted(mids))+'.']
    lines += ['', '# Measure families', '', 'These are parameterized constructions or discovery groupings, rather than single scalar measures.', '', json.dumps(d.get('measure_families',[]),ensure_ascii=False,indent=2)]
    (ROOT/'docs/notation-collisions.md').write_text('\n'.join(lines)+'\n')
    register=[]
    for m in d['measures']:
        for category in ['aliases','alias_candidates','alias_attribution_history','repository_display_variants']:
            for a in m.get(category,[]):
                register.append(dict(measure=m['id'],category=category,**a))
    (ROOT/'data/notation-register.json').write_text(json.dumps(register,ensure_ascii=False,indent=2)+'\n')
    lines=['# Historical notation register','','TeX strings transcribe printed notation; they are not quotations of the authors’ TeX source. Source-dependent cost conventions and parameter conversions are part of the alias. Candidate names and repaired seed attributions remain visible in the JSON and are not silently treated as established occurrences.','','| Measure | Name or notation | Source and locator | Normalization / status |','|---|---|---|---|']
    for a in register:
        if a['category']!='aliases':continue
        lines.append('| '+a['measure']+' | `'+a['text']+'` | ['+a['source']+']('+rmap[a['source']]['url']+'), '+a.get('locator','pending')+' | '+a.get('normalization','')+'; '+a.get('status','pending')+' |')
    (ROOT/'docs/historical-notation.md').write_text('\n'.join(lines)+'\n')
    print('Exported bibliography, documentation, notation register, collisions, and coverage counts.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['validate','export','pair','list'])
    parser.add_argument('A', nargs='?')
    parser.add_argument('B', nargs='?')
    parser.add_argument('--kind', choices=['decision_function','search_relation','multi_output_function','real_valued_function','hazard_free_extension'])
    parser.add_argument('--totality', choices=['total','partial'])
    parser.add_argument('--class', dest='class_name', action='append', help='Intersect class restrictions; use unrestricted for general claims only')
    parser.add_argument('--historical', action='store_true')
    args = parser.parse_args()
    d = json.loads(DATA.read_text())
    report = validate(d)
    if args.command == 'validate':
        print(report)
    elif args.command == 'export':
        export(d)
    else:
        if args.command == 'pair' and (not args.A or not args.B):
            parser.error('pair requires ordered measure IDs A B')
        for key in ['A','B']:
            value = getattr(args,key)
            if value and value not in {m['id'] for m in d['measures']}:
                parser.error(f'unknown measure ID: {value}')
        selected = [c for c in d['claims'] if matches(c,args)]
        print(json.dumps(dict(coverage='incomplete; missing record does not mean no known bound',claims=selected),ensure_ascii=False,indent=2))

if __name__ == '__main__':
    main()
