import katex from './vendor/katex/katex.mjs';
for (const node of document.querySelectorAll('[data-tex]')) {
  try {
    katex.render(node.dataset.tex,node,{displayMode:node.dataset.display==='true',throwOnError:true,trust:false,strict:'ignore',output:'htmlAndMathml',maxExpand:1000});
  } catch (error) {
    node.classList.add('math-error');
    node.title=error.message;
  }
}
