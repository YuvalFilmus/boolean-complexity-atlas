/* Presentation only. Original source strings stay intact in the catalogue. */
export function notationTex(raw){
 let s=String(raw??'').replace(/\\\\/g,'\\').trim();
 if(s.startsWith('overline '))return '\\overline{'+notationTex(s.slice(9))+'}';
 if(s.startsWith('tilde '))return '\\widetilde{'+notationTex(s.slice(6))+'}';
 if(s.endsWith(' prime'))return notationTex(s.slice(0,-6))+"'";
 const special={
  'max_i ||D_i p||_infinity':'\\max_i \\lVert D_i p\\rVert_\\infty',
  'Inf_i^(lambda)':'\\operatorname{Inf}_i^{(\\lambda)}',
  'Inf^(lambda)':'\\operatorname{Inf}^{(\\lambda)}',
  'Var^(lambda)':'\\operatorname{Var}^{(\\lambda)}',
  'swInf_(i,j)':'\\operatorname{swInf}_{(i,j)}',
  'C_bar0':'C_{\\bar 0}','C_bar1':'C_{\\bar 1}',
  'D^wedge-dt':'D^{\\wedge\\text{-dt}}','R^wedge-dt':'R^{\\wedge\\text{-dt}}','psD^wedge-dt':'\\mathrm{psD}^{\\wedge\\text{-dt}}',
  'D^oplus-dt':'D^{\\oplus\\text{-dt}}','R^oplus-dt':'R^{\\oplus\\text{-dt}}','psD^oplus-dt':'\\mathrm{psD}^{\\oplus\\text{-dt}}'
 };
 if(special[s])return special[s];
 s=s.replace(/_([A-Za-z0-9]+)/g,'_{$1}').replace(/\^([A-Za-z][A-Za-z0-9]*)/g,'^{$1}');
 s=s.replace(/(?<![\\A-Za-z])(lambda|epsilon|delta|beta|alpha|mu|ell|Sigma|Delta|infinity|downarrow|wedge|vee|oplus)(?![A-Za-z])/g,(_,x)=>'\\'+(x==='infinity'?'infty':x));
 s=s.replace(/(?<![\\A-Za-z])(deg|udeg|rdeg|ndeg|bs|fbs|mbs|fmbs|cbs|fcbs|cfbs|spar|gspar|wt|gwt|osdeg|rrank|Rank|Depth|Inf|Var|InstC|Conj|nonadaptive|weak|str|cert|pub|priv|ent|ns|bounded|sos|min|cri|nRelevant)(?![A-Za-z])/g,(_,x)=>'\\mathrm{'+x+'}');
 return s;
}
export function exponentTex(raw){return String(raw).replaceAll('∞','\\infty').replaceAll('≤','\\le ').replaceAll('≥','\\ge ').replaceAll(' – ',' \\text{–} ').replaceAll('—','\\text{—}').replaceAll('⋯','\\cdots').replaceAll('…','\\ldots').replace(/log\(/g,'\\log(').replace(/sqrt\((\d+)\)/g,'\\sqrt{$1}');}
