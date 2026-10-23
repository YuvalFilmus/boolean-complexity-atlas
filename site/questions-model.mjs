export const QUESTION_SORTS={centrality:'Measure centrality',recurrence:'Question recurrence',implications:'Implication reach',gap:'Exponent gap',recent:'Recent activity',longevity:'Historical longevity'};
export function questionOptions(hash){const p=new URLSearchParams(hash.split('?')[1]||'');return {sort:QUESTION_SORTS[p.get('sort')]?p.get('sort'):'centrality',type:['all','published','gap','endpoint','archive'].includes(p.get('type'))?p.get('type'):'published',domain:p.get('domain')||'',group:p.get('group')||'',repeated:p.get('repeat')==='1',q:p.get('q')||''};}
export function questionScore(q,sort){return {centrality:q.centrality,recurrence:q.recurrence?.count,implications:q.implication_reach?.count,gap:q.gap?.score,recent:q.latest_activity_year,longevity:q.first_formulation_year}[sort]??null;}
export function rankedQuestions(rows,options,{measureGroups={},searchText=()=>''}={}){return rows.filter(q=>{
 if(options.type==='archive'?!q.archived:q.archived)return false;
 if(options.type==='gap'){if(q.gap?.score==null)return false;}else if(options.type!=='all'&&options.type!=='archive'&&q.origin!==options.type)return false;
 if(options.domain&&q.context!==options.domain)return false;
 if(options.group&&!q.measure_ids.some(m=>measureGroups[m]===options.group))return false;
 if(options.repeated&&(q.recurrence?.count||0)<2)return false;
 const needle=(options.q||'').trim().toLowerCase();return !needle||[q.id,q.statement,q.mapping_note,...q.measure_ids,searchText(q)].join(' ').toLowerCase().includes(needle);
 }).sort((a,b)=>{const x=questionScore(a,options.sort),y=questionScore(b,options.sort);if(x===null||y===null)return x===y?a.id.localeCompare(b.id):x===null?1:-1;return (options.sort==='longevity'?x-y:y-x)||a.id.localeCompare(b.id);});}
export function questionHash(o){const p=new URLSearchParams();for(const k of ['sort','type','domain','group','q'])if(o[k])p.set(k,o[k]);if(o.repeated)p.set('repeat','1');return '#questions?'+p;}
