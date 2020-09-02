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

## Algoritmos

Existem várias implementações possíveis dos métodos de Monte Carlo, como:

 - [🏔 Monte Carlo Every-Visit](Monte%20Carlo%20Every-Visit)