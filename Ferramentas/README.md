# Ferramentas utilizadas no repositório

## Geração de imagens com LaTeX

### Fórmulas em geral

As fórmulas _inline_ (que ficam na mesma linha que outro texto) devem ser
formatadas, se possível, com unicode e itálico, evitando o uso de imagens.
Por exemplo, o estado de um ambiente é _s_ e não <img src="https://latex.codecogs.com/svg.latex?s" title="s" />.
O uso de letras gregas, pode ser feito por meio dos escape codes
de HTML: `&epsilon;` para &epsilon;, `&Delta;` para &Delta;, `&delta;` para &delta;, etc.

As fórmulas maiores e, em particular, aquelas que não forem _inline_,
devem ser escritas em LaTeX, utilizando o [editor de equações do CodeCogs](https://www.codecogs.com/latex/eqneditor.php)
em formato SVG, com o código fonte armazenado no título da imagem. Para tanto, basta selecionar as opções "svg" e "HTML"
(não "HTML (Edit)") no CodeCogs, conforme o exemplo abaixo:

![editor do CodeCogs](codecogs.png)

```markdown
Equação: $\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$

Markdown (html):
<img src="https://latex.codecogs.com/svg.latex?\sum_{k=1}^{n}&space;k&space;=&space;\frac{n(n&plus;1)}{2}"
     title="\sum_{k=1}^{n} k = \frac{n(n+1)}{2}" />
```

Imagem:
<img src="https://latex.codecogs.com/svg.latex?\sum_{k=1}^{n}&space;k&space;=&space;\frac{n(n&plus;1)}{2}" title="\sum_{k=1}^{n} k = \frac{n(n+1)}{2}" />

### Algoritmos

As caixas de algoritmos devem seguir o template fornecido no arquivo [template_algoritmo.tex](template_algoritmo.tex).
O código que deve ser modificado está no final do arquivo:

```latex
\title{Nome do Algoritmo}
\geometry{paperwidth=17cm}

\begin{document}
\begin{algorithm}
Parâmetros: $\varepsilon > 0, \dots$
Inicializar:
    parâmetros...

Loop para cada episódio:
    ...
\end{algorithm}
```

Primeiramente, o arquivo deve ser compilado utilizando XeLaTex. Por exemplo, no terminal, com:

```bash
xelatex -shell-escape algoritmo.tex  # Compila o arquivo latex
```

ou no Overleaf com a opção `Compiler: XeLaTeX`.

Em seguida, é necessário converter o pdf gerado para svg. Recomenda-se o uso da ferramenta Poppler:

```bash
pdftocairo -svg algoritmo.pdf
```

![Template de Algoritmo](template_algoritmo.svg)

As imagens resultantes, assim como os arquivos fonte em latex devem ser salvos diretório "Imagens" do
respectivo algoritmo / grupo de algoritmos.
