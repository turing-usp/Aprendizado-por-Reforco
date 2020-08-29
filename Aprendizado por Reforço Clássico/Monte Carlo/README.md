# 🏔 Métodos de Monte Carlo

Os métodos de **Monte Carlo** são algoritmos de Aprendizado por Reforço que estimam as funções de valor com base em suas *experiências*, obtidas através da interação com o ambiente. Nesses métodos, os valores são obtidos a partir do cálculo da média dos retornos de cada episódio.

## Motivação

Apesar de muito eficazes, os algoritmos de **Programação Dinâmica** (**DP**) desenvolvidos anteriormente requerem um conhecimento prévio completo do funcionamento do nosso ambiente, que raramente é obtido em problemas reais. Dessa forma, foi necessário elaborar algoritmos de Aprendizado por Reforço que conseguissem aprender políticas ótimas apenas por meio da interação com o ambiente.

Assim surgiram os **métodos de Monte Carlo**, que se baseiam no cálculo da média de vários retornos para obter estimativas das funções de valor. Nesse sentido, esses algoritmos se aproximam bastante do cálculo dos valores no problema dos Bandits.

## Teoria

Primeiramente, para entender melhor esses métodos, precisamos relembrar de como definimos nossa função de valor ***q***:

<img src="https://latex.codecogs.com/svg.latex?q_\pi(s,a)&space;=&space;\mathop{\mathbb{E}_\pi}[{G_t}|{S_t=s,&space;A_t=a}]" title="q_\pi(s,a) = \mathop{\mathbb{E}_\pi}[{G_t}|{S_t=s, A_t=a}]" />

O **Valor Estado-Ação** para uma determinada política é definido como a esperança do retorno ***G*** quando se toma uma determinada ação *a* em um determinado estado *s* seguindo essa política. Dessa forma, é natural pensar que poderíamos estimar esse ***q*** ao tomar uma média de todos os retornos que observarmos depois de tomar uma ação *a* em um estado *s*.

E é a partir dessa intuição que nascem os métodos de Monte Carlo, nos quais são calculadas as médias dos retornos obtidos ao tomar cada ação para estimar os valores *q(s, a)*. Portanto, a ideia do algoritmo é a seguinte:

 - Rodar um episódio
 - Calcular o retorno *G* em cada instante de tempo desse episódio

   <img src="https://latex.codecogs.com/svg.latex?G_t&space;=&space;R_{t&plus;1}&space;&plus;&space;\gamma&space;R_{t&plus;2}&space;&plus;&space;\gamma^2&space;R_{t&plus;3}&space;&plus;&space;..." title="G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + ..." />
 - Atualizar as estimativas *Q* de cada par estado-ação com a média dos retornos dos episódios amostrados.
 
   <img src="https://latex.codecogs.com/svg.latex?Q(s,a)&space;\leftarrow&space;\operatorname{media}(Retornos(s,&space;a))" title="Q(s,a) \leftarrow \operatorname{media}(Retornos(s, a))" />
 - Repetir o processo para vários episódios até obter uma política ótima.

## Política ε-greedy

Para garantir que os métodos de Monte Carlo convirjam para a função de valor real, é necessário seguir uma política que explore todas as ações de todos os estados. Entretanto, também é interessante que o agente tente conseguir cada vez mais recompensas, para maximizar sua perfomance.

Assim foi desenvolvida a política *ε-greedy*, que escolhe a próxima ação com base em um parâmetro *ε*, normalmente pequeno. A cada decisão, a política tem uma probabilidade *ε* de escolher uma ação aleatória, aumentando a exploração, e uma probabilidade *1 - ε* de escolher a ação associada ao maior *Q*. Dessa forma, ela estabelece um equilíbrio entre a exploração de ações e a explotação de recompensas. Essa política é dada por:

<img src="https://latex.codecogs.com/svg.latex?\pi(a|S_t)&space;\leftarrow&space;\begin{cases}&space;1&space;-&space;\varepsilon&space;&plus;&space;\varepsilon/\left|\mathcal{A}(S_t)\right|,&space;&&space;\mbox{se&space;}&space;a&space;=&space;\underset{a}{\mathrm{argmax}}&space;\,&space;Q(S_t,a)&space;\\&space;\varepsilon/\left|\mathcal{A}(S_t)\right|,&space;&&space;\mbox{se&space;}&space;a&space;\neq&space;\underset{a}{\mathrm{argmax}}&space;\,&space;Q(S_t,a)&space;\end{cases}" title="\pi(a|S_t) \leftarrow \begin{cases} 1 - \varepsilon + \varepsilon/\left|\mathcal{A}(S_t)\right|, & \mbox{se } a = \underset{a}{\mathrm{argmax}} \, Q(S_t,a) \\ \varepsilon/\left|\mathcal{A}(S_t)\right|, & \mbox{se } a \neq \underset{a}{\mathrm{argmax}} \, Q(S_t,a) \end{cases}" />

<img src="https://latex.codecogs.com/svg.latex?\left|\mathcal{A}(S_t)\right|&space;\rightarrow&space;\textrm{quantidade&space;de&space;acoes&space;possiveis}" title="\left|\mathcal{A}(S_t)\right| \rightarrow \textrm{quantidade de acoes possiveis}" />

## Algoritmo

Primeiramente, devemos inicializar a nossa tabela *Q(s, a)* com valores arbitrários para cada par estado-ação. Nesse caso, vamos optar por superestimar os valores Q de modo a incentivar a exploração do agente.

Também inicializamos uma tabela *N(s, a)* que guarda a quantidade de retornos obtidos de cada par estado-ação, para fazer o cálculo da média móvel dos retornos.

Para cada episódio, vamos escolher ações seguindo nossa política ε-greedy e guardar os estados, ações e recompensas para cada instante *t*. Ao final, calculamos o retorno *G* de cada instante começando pelo término atualizando os valores *Q* correspondentes.

Para estimar a média dos retornos, podemos utilizar a *média móvel*, de forma a realizar os cálculos na hora sem precisar guardar uma lista com todos os retornos. Ao invés disso, precisamos guardar apenas a média anterior e a quantidade total de elementos *n*.

<img src="https://latex.codecogs.com/svg.latex?{\overline&space;{x}}_{novo}&space;=&space;\frac{(n&space;-&space;1){\overline&space;{x}}_{anterior}&space;&plus;&space;x_n}{n}" title="{\overline {x}}_{novo} = \frac{(n - 1){\overline {x}}_{anterior} + x_n}{n}" />

Por fim, podemos ver abaixo um exemplo em pseudo-código do funcionamento do algoritmo de Monte Carlo Every-Visit:

![On-policy every-visit MC control](/img/MC.png)