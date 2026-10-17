import {notationTex,exponentTex} from './notation.mjs';
export const CORE=['D','R0','R','C','RC','bs','s','lambda','QE','deg','Q','adeg'];
export const DEFAULT=['D','R0','R','Q','C','bs','deg','adeg'];
export const COMPLETION=['D','R0','R','R1','Q','QE','Q0','C','C0','C1','RC','QC','FC','fbs','UC','UC0','UC1','bs','s','lambda','deg','adeg','nRelevant'].map(x=>'completion_'+x);
export const PROFILES={'product':'Products','permutation':'Symmetric group','perfect-matching':'Perfect matchings','hypermatching':'Partite hypermatchings','multislice':'Multislices','slice':'Slices','uniform-hypermatching':'Uniform hypermatchings'};
export const CONTEXTS={total:'Total Boolean functions',partial:'Partial Boolean functions',completion:'Minimum completions','search-total':'Total search problems','search-partial':'Partial search problems',symmetric:'Symmetric Boolean functions',permutation:'Symmetric group: original measures',...Object.fromEntries(Object.entries(PROFILES).map(([k,v])=>['profile-'+k,v+': query-domain measures']))};
export function group(m){
 const id=m.id,n=m.name.toLowerCase();
 if(id.startsWith('completion_'))return 'Minimum completions';
 if(id.startsWith('perm')||id.startsWith('domain'))return 'Other domains';
 if(id.endsWith('_cert'))return 'Certification transforms';
 if(id.startsWith('rel_')||/^(ps|input1|V$)/.test(id))return 'Search & pseudodeterminism';
 if(/certificate|adversary|sabotage|certificate game/.test(n))return 'Certificates & adversaries';
 if(/sensitivity|influence|variance|relevant|block number|brick number/.test(n))return 'Sensitivity & variables';
 if(/degree|polynomial|sparsity|monomial|coefficient weight/.test(n))return 'Polynomials & Fourier analysis';
 if(/rank|leaf|node|guessing/.test(n))return 'Tree size & structure';
 return 'Query algorithms & other models';
}
export function defaultSelection(context){
 if(context==='completion')return DEFAULT.map(x=>'completion_'+x);
 if(context.startsWith('profile-'))return ['domainD','domainR','domainQ','domainC','domainBS','domainS','domainDegree','domainAdeg'];
 if(context==='permutation')return ['permD','permR','permQ','permC','permBS','permS','permDegree','permAdeg'];
 if(context.startsWith('search-'))return ['D','R0','R','Q','psR','psQ','rel_bs','rel_adeg'];
 return [...DEFAULT];
}
export function belongs(c,context,{history=false}={}){
 const s=c.scope||{};
 if(!history&&c.historical)return false;
 if(context==='completion')return c.A?.startsWith('completion_')&&c.B?.startsWith('completion_');
 if(context==='permutation')return c.A?.startsWith('perm')&&c.B?.startsWith('perm');
 if(context.startsWith('profile-'))return c.A?.startsWith('domain')&&c.B?.startsWith('domain');
 if(context.startsWith('search-'))return s.object_kind==='search_relation'&&(s.totality==='partial_or_total'||s.totality===(context==='search-total'?'total':'partial'));
 if(s.object_kind!=='decision_function')return false;
 if(context==='symmetric')return (s.totality==='total'||s.totality==='partial_or_total')&&((s.classes||[]).includes('symmetric')||(!(s.classes||[]).length&&c.kind==='upper_bound'));
 return (s.totality==='partial_or_total'||s.totality===(context==='total'?'total':'partial'))&&!(s.classes||[]).length;
}
export function directClaims(data,a,b,context,history=true){return data.catalog.claims.filter(c=>c.A===a&&c.B===b&&belongs(c,context,{history}));}
export function tableRecord(data,a,b,context){
 let cells;
 if(['total','partial','completion'].includes(context))cells=data.datasets[context]?.cells;
 if(context==='permutation')cells=data.datasets.permutation.cells;
 if(context.startsWith('profile-'))cells=data.datasets.profiles.profiles.find(p=>p.profile===context.slice(8))?.cells;
 const exact=cells?.find(c=>c.A===a&&c.B===b);
 if(exact)return exact;
 const records=directClaims(data,a,b,context,false);
 const eligible=records.filter(c=>c.scalar_inference_allowed!==false&&!(c.scope?.assumptions||[]).length&&!['secondary_checked','statement_checked_proof_pending','survey_checked'].includes(c.status));
 const unbounded=eligible.filter(c=>c.kind==='no_polynomial_bound');
 if(unbounded.length)return {A:a,B:b,status:'no_finite_power',claim_ids:unbounded.map(c=>c.id),direct_only:true};
 const numeric=eligible.filter(c=>Number.isFinite(c.exponent_numeric));
 const uppers=numeric.filter(c=>['upper_bound','identity','theta_bound'].includes(c.kind)&&['none','polylog','subpolynomial'].includes(c.loss||'none')).sort((a,b)=>a.exponent_numeric-b.exponent_numeric);
 const lowers=numeric.filter(c=>['separation','theta_bound','identity'].includes(c.kind)).sort((a,b)=>b.exponent_numeric-a.exponent_numeric);
 if(uppers.length||lowers.length)return {A:a,B:b,status:'direct_evidence',direct_only:true,upper:uppers[0]?{exponent:uppers[0].exponent_label,endpoint_without_log:!(uppers[0].loss&&uppers[0].loss!=='none'),claim_ids:[uppers[0].id]}:null,lower:lowers[0]?{expression_label:lowers[0].exponent_label,exponent:lowers[0].exponent_label,claim_ids:[lowers[0].id]}:null};
 return {A:a,B:b,status:records.length?'records_only':'not_yet_indexed',claim_ids:records.map(c=>c.id)};
}
export function cellSummary(r,a,b){
 if(a===b)return {text:'1',kind:'identity',description:'Identity comparison; measure conventions still apply.'};
 if(r.status==='no_finite_power'||r.status==='no_polynomial_bound')return {text:'∞',kind:'unbounded',description:'A recorded family excludes every finite power; inspect scope and witnesses.'};
 const upper=r.upper||((r.exponent||r.upper_exponent)?{exponent:r.exponent||r.upper_exponent,endpoint_without_log:true}:null);
 const lo=r.lower?.expression_label??r.lower?.exponent_expression??r.lower?.exponent;
 const up=upper?.exponent;
 const numeric=r.lower?.numeric_for_ranking;
 const shortLo=Number.isFinite(numeric)?(Number.isInteger(numeric)?String(numeric):(String(lo).length>11?String(Math.floor(numeric*1000)/1000)+'…':String(lo))):lo;
 const loss=upper&&(upper.endpoint_without_log===false||Number(upper.log_power)>0);
 const matched=r.matching_exponent??r.matched_recorded_exponents??(lo!=null&&up!=null&&String(lo)===String(up));
 if(up!=null&&lo!=null)return {text:matched?String(up):`${shortLo} – ${up}`,kind:matched?'matched':'gap',loss,description:`Recorded lower exponent ${lo}; upper exponent ${up}${loss?'; upper endpoint has a logarithmic or subpolynomial loss':''}.`};
 if(up!=null)return {text:`≤ ${up}`,kind:'upper',loss,description:`Recorded upper exponent ${up}; no matching lower exponent indexed here.`};
 if(lo!=null)return {text:`≥ ${lo}`,kind:'lower',description:`Recorded lower exponent ${lo}; no upper exponent indexed here.`};
 return {text:r.status==='records_only'?'⋯':'—',kind:'unknown',description:r.status==='records_only'?'Results indexed, but no scalar exponent summarized.':'No comparable scalar exponent indexed; this is not a claim of openness.'};
}
export function recordClaimIds(r){return [...new Set([...(r.claim_ids||[]),...(r.upper?.claim_ids||[]),...(r.pure_upper?.claim_ids||[]),...(r.lower?.claim_ids||[]),...(r.records||[]).map(c=>c.claim_id)])];}
export function comparisonClaims(data,a,b,context){
 const r=tableRecord(data,a,b,context),ids=new Set(recordClaimIds(r));
 return data.catalog.claims.filter(c=>ids.has(c.id)||(c.A===a&&c.B===b&&belongs(c,context,{history:true}))).sort((a,b)=>claimYear(data,a)-claimYear(data,b)||a.id.localeCompare(b.id));
}
export function claimYear(data,c){const s=data.catalog.sources.find(s=>s.id===c.source);return s?Math.min(s.year,...(s.versions||[]).map(v=>v.year).filter(Number.isFinite)):9999;}
export function selectionCSV(data,selected,context){return [['A (row)','B (column)','lower exponent','upper exponent','upper endpoint loss','status','claim IDs'],...selected.flatMap(a=>selected.map(b=>{const r=tableRecord(data,a,b,context),s=cellSummary(r,a,b);return [a,b,r.lower?.expression_label??r.lower?.exponent??'',r.upper?.exponent??r.exponent??r.upper_exponent??'',s.loss?'yes':'',s.kind,recordClaimIds(r).join(';')]}))].map(row=>row.map(v=>'"'+String(v).replaceAll('"','""')+'"').join(',')).join('\n');}
export function parseLocation(hash,measures){const [page='explorer',query='']=hash.replace(/^#/,'').split('?');const q=new URLSearchParams(query);const context=CONTEXTS[q.get('scope')]?q.get('scope'):'total';const ids=new Set(measures.map(m=>m.id));const raw=q.get('m');return {page:['explorer','bibliography','measures','conjectures','about'].includes(page)?page:'explorer',context,selected:raw===null?defaultSelection(context):[...new Set(raw.split(',').filter(x=>ids.has(x)))],a:q.get('a'),b:q.get('b'),q:q.get('q')||''};}
export function shareHash(context,selected,a,b){const q=new URLSearchParams({scope:context,m:selected.join(',')});if(a&&b){q.set('a',a);q.set('b',b)}return '#explorer?'+q;}

export function selectionLatex(data,selected,context){
 const names=new Map(data.catalog.measures.map(m=>[m.id,m.symbol]));
 const label=id=>'$'+notationTex(names.get(id)||id)+'$';
 const end=' '+String.fromCharCode(92,92);
 const lines=['% Rows A, columns B. Recorded exponents; dagger retains upper endpoint loss.','% Scope: '+CONTEXTS[context]+'. Not certified current best.','% Requires amsmath. Exact expressions and provenance are in the JSON dossier.','\\begin{tabular}{l'+'c'.repeat(selected.length)+'}', ' & '+selected.map(label).join(' & ')+end,'\\hline'];
 for(const a of selected){const row=[label(a),...selected.map(b=>{const s=cellSummary(tableRecord(data,a,b,context),a,b);return '$'+exponentTex(s.text)+(s.loss?'^{\\dagger}':'')+'$'})];lines.push(row.join(' & ')+end)}
 lines.push('\\end{tabular}');return lines.join('\n')+'\n';
}
