"""Render the atlas's controlled Markdown proof sources as standalone static pages."""
from pathlib import Path
import html,re,hashlib,shutil
ROOT=Path(__file__).resolve().parents[1]
TOKEN=re.compile(r'\$\$([\s\S]*?)\$\$|\$([^\n$]+)\$|\[([^\]]+)\]\(([^)\s]+)\)|\*\*([^*]+)\*\*|`([^`]+)`')
PAGES=[('hypermatching','hypermatching-proof.md','Quadratic sensitivity bounds for hypermatchings'),('hypermatching-audit','hypermatching-full-source-audit.md','Full source audit of the hypermatching proof'),('hypermatching-priority','hypermatching-priority-audit.md','Hypermatching literature and priority check'),('exact-search','exact-search-proof.md','Exact two-query certificate search'),('exact-search-audit','exact-search-full-source-audit.md','Independent audit of exact two-query certificate search'),('exact-search-priority','exact-search-priority-audit.md','Exact certificate search literature and priority check')]
PAGES += [('width-three','width-three-proof.md','Four queries for the 4-MAJ certificate partition'),('width-three-audit','width-three-full-source-audit.md','Independent audit of the four-query obstruction'),('width-three-priority','width-three-priority-audit.md','Four-query obstruction literature and priority check'),('rooted-paths','rooted-paths-proof.md','Influence bounds for rooted-path Fourier supports'),('rooted-paths-audit','rooted-paths-full-source-audit.md','Independent audit of rooted-path influence bounds'),('rooted-paths-priority','rooted-paths-priority-audit.md','Rooted-path influence literature and priority check')]
LINKS={source:slug+'.html' for slug,source,title in PAGES}
FAMILIES={'hypermatching':'hypergraphical','exact-search':'exact%20quantum','width-three':'exact%20quantum','rooted-paths':'AA-bounded-polynomial-influence'}
CHECKERS=['width_three_check.py','width_three_independent_check.py','rooted_paths_independent_check.py']
def inline(s):
 out=[];pos=0
 for m in TOKEN.finditer(s):
  out.append(html.escape(s[pos:m.start()]));pos=m.end()
  display,math,label,url,bold,code=m.groups()
  if display is not None or math is not None:
   tex=display if display is not None else math
   out.append('<span class="'+('proof-equation' if display is not None else 'proof-math')+'" data-tex="'+html.escape(tex,quote=True)+'" data-display="'+str(display is not None).lower()+'">'+html.escape(tex)+'</span>')
  elif label is not None:
   if url in LINKS:url=LINKS[url]
   elif not re.match(r'^(https?://|#|\.\./|[A-Za-z0-9_-]+(?:/|\.))',url):raise ValueError('Unsupported proof link '+url)
   elif url.endswith('.md') and '/' not in url:url='../research-notes/'+url
   out.append('<a href="'+html.escape(url,quote=True)+'">'+html.escape(label)+'</a>')
  elif bold is not None:out.append('<strong>'+html.escape(bold)+'</strong>')
  else:out.append('<code>'+html.escape(code)+'</code>')
 out.append(html.escape(s[pos:]));return ''.join(out)
def markdown(s):
 blocks=[]
 for block in re.split(r'\n\s*\n',s.strip()):
  lines=block.splitlines()
  if len(lines)==1 and (m:=re.match(r'^(#{1,4}) (.+)$',block)):
   level=len(m[1]);blocks.append(f'<h{level}>'+inline(m[2])+f'</h{level}>')
  elif len(lines)>1 and re.match(r'^\|(?:\s*:?-+:?\s*\|)+$',lines[1]) and all(line.startswith('|') and line.endswith('|') for line in lines):
   rows=[[cell.strip() for cell in line.strip('|').split('|')] for line in lines]
   blocks.append('<div class="proof-table"><table><thead><tr>'+''.join('<th scope="col">'+inline(cell)+'</th>' for cell in rows[0])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+inline(cell)+'</td>' for cell in row)+'</tr>' for row in rows[2:])+'</tbody></table></div>')
  elif all(re.match(r'^[*-] ',line) for line in lines):blocks.append('<ul>'+''.join('<li>'+inline(line[2:])+'</li>' for line in lines)+'</ul>')
  elif all(re.match(r'^\d+\. ',line) for line in lines):blocks.append('<ol>'+''.join('<li>'+inline(re.sub(r'^\d+\. ','',line))+'</li>' for line in lines)+'</ol>')
  else:blocks.append('<p>'+inline(block)+'</p>')
 return '\n'.join(blocks)
def build(dst):
 out=dst/'proofs';out.mkdir(exist_ok=True)
 checks=out/'checks';checks.mkdir(exist_ok=True)
 for name in CHECKERS:shutil.copy2(ROOT/'tests'/name,checks/name)
 for slug,source,title in PAGES:
  path=ROOT/'docs'/source
  if not path.exists():raise FileNotFoundError('Missing audited proof page source '+str(path))
  raw=path.read_text();digest=hashlib.sha256(path.read_bytes()).hexdigest()
  body=markdown(raw)
  family=next(f for f in FAMILIES if slug in [f,f+'-audit',f+'-priority'])
  query=FAMILIES[family]
  doc='''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'''+html.escape(title)+''' · Boolean Complexity Atlas</title><link rel="icon" href="../icon.svg" type="image/svg+xml"><link rel="stylesheet" href="../styles.css"><link rel="stylesheet" href="../vendor/katex/katex.min.css"></head><body>
<a class="skip" href="#proof-main">Skip to proof</a><header class="site-header"><a class="brand" href="../#explorer">Boolean Complexity <strong>Atlas</strong></a><nav aria-label="Proof navigation"><a href="../#explorer">Exponent tables</a><a href="../#questions?q='''+query+'''">Open questions</a><a href="'''+family+'''.html">Proof</a><a href="'''+family+'''-audit.html">Full audit</a><a href="'''+family+'''-priority.html">Priority check</a></nav></header>
<main id="proof-main" class="proof-page"><p class="eyebrow">DERIVED RESEARCH NOTE · CHECKED 23 OCTOBER 2026</p>'''+body+'''<hr><p class="small"><a href="../research-notes/'''+html.escape(source)+'''">Plaintext Markdown source</a> · <a href="../downloads/'''+family+'''-proof-audit.json">Audit manifest</a></p><p class="small">Source SHA-256: <code>'''+digest+'''</code></p><noscript><p>JavaScript is disabled. Mathematical source is visible in TeX; enable JavaScript to render it with the bundled KaTeX.</p></noscript></main><script type="module" src="../proof-math.mjs"></script></body></html>'''
  (out/(slug+'.html')).write_text(doc)

 # A stable landing page keeps all research proofs discoverable from one tab.
 cards=''.join('<li><a href="'+slug+'.html">'+html.escape(title)+'</a> · <a href="'+slug+'-audit.html">Independent audit</a> · <a href="'+slug+'-priority.html">Priority check</a></li>' for slug,source,title in PAGES if slug in FAMILIES)
 (out/'index.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Research proofs · Boolean Complexity Atlas</title><link rel="stylesheet" href="../styles.css"></head><body><header class="site-header"><a class="brand" href="../#explorer">Boolean Complexity <strong>Atlas</strong></a></header><main class="proof-page"><h1>Audited research proofs</h1><p>Complete statements and proofs, independent assistant reviews, and bounded prior-publication searches. These records retain their model assumptions and do not certify novelty or formal verification.</p><ul>'+cards+'</ul></main></body></html>')
