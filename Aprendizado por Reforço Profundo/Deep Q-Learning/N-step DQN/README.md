# N-Step DQN
###### Veja a implementação do algoritmo no [notebook](N-Step%20DQN.ipynb)!

A **N-Step DQN** é uma extensão da DQN que utiliza a informação de uma sequência de várias transições para o cálculo da função de valor, gerando targets mais estáveis.

# Conceito
Em algoritmos de Monte Carlo, o nosso modelo ¨aprende¨ em cada transição com base em **toda** a sequência de recompensas em um episódio, ou seja, o retorno completo (<img src="https://latex.codecogs.com/svg.latex?G_t" title="G_t" />). Já em one-step Temporal Diference, o aprendizado é feito observando apenas uma recompensa no futuro (<img src="https://latex.codecogs.com/svg.latex?R_{t&space;&plus;&space;1}" title="R_{t + 1}" />) e aproximamos o restante do retorno (<img src="https://latex.codecogs.com/svg.latex?G_{t&plus;1}" title="G_{t+1}" />) como sendo o valor do próximo estado (<img src="https://latex.codecogs.com/svg.latex?V(S_{t&space;&plus;&space;1})" title="V(S_{t + 1})" />).


Agora, em N-step, tomamos uma abordagem intermediária a esses dois algoritmos. Não chegamos a utilizar a totalidade do retorno (<img src="https://latex.codecogs.com/svg.latex?G_t" title="G_t" />), mas **n** passos a frente do presente (**t**). Dessa forma, obtemos a seguinte expressão:

<img src="https://latex.codecogs.com/svg.latex?G_t&space;=&space;R_{t&plus;1}&space;&plus;&space;\gamma&space;R_{t&space;&plus;&space;2}&space;&plus;&space;\gamma^2&space;R_{t&space;&plus;&space;3}&space;&plus;&space;\dots&space;&plus;&space;\gamma^{T&space;-t&space;-1}&space;R_{T}" title="G_t = R_{t+1} + \gamma R_{t + 2} + \gamma^2 R_{t + 3} + \dots + \gamma^{T -t -1} R_{T}" />

<img src="https://latex.codecogs.com/svg.latex?G_{t:t&space;&plus;&space;n}&space;=&space;R_{t&plus;1}&space;&plus;&space;\gamma&space;R_{t&space;&plus;&space;2}&space;&plus;&space;\gamma^2&space;R_{t&space;&plus;&space;3}&space;&plus;&space;\dots&space;&plus;&space;\gamma^{n&space;-1}&space;R_{t&space;&plus;&space;n}&space;&plus;&space;\gamma^n&space;V_{t&space;&plus;n&space;-1}(S_{t&space;&plus;&space;n})" title="G_{t:t + n} = R_{t+1} + \gamma R_{t + 2} + \gamma^2 R_{t + 3} + \dots + \gamma^{n -1} R_{t + n} + \gamma^n V_{t +n -1}(S_{t + n})" />

onde <img src="https://latex.codecogs.com/svg.latex?G_t" title="G_t" /> representa o retorno completo (usado em Monte Carlo) e <img src="https://latex.codecogs.com/svg.latex?G_{t:t&space;&plus;&space;n}" title="G_{t:t + n}" /> a aproximação do retorno com n-step, utilizando bootstraping do Valor do estado no instante t + n (<img src="https://latex.codecogs.com/svg.latex?V_{t&space;&plus;n&space;-1}(S_{t&space;&plus;&space;n})" title="V_{t +n -1}(S_{t + n})" />).

![N-Step](https://media.discordapp.net/attachments/688564171973197869/752614671974006844/unknown.png)

Vale notar que, no início do episódio, o agente não possui todas as experiências necessárias para fazer a estimativa do retorno. Para contornar isso, fazemos mudanças no replay buffer (explicadas mais a frente) para possibilitar o cálculo.

## Sarsa para n-Step
Agora que temos uma noção de como o n-step funciona, podemos nos preocupar em como nosso agente pode fazer uma escolha se baseando nesse processo. Para isso, mudamos nossa previsão para que ela preveja ações e não estados. Com esse objetivo, chegamos às seguintes expressões:

<img src="https://latex.codecogs.com/svg.latex?G_{t:t&space;&plus;&space;n}&space;=&space;R_{t&plus;1}&space;&plus;&space;\gamma&space;R_{t&space;&plus;&space;2}&space;&plus;&space;\gamma^2&space;R_{t&space;&plus;&space;3}&space;&plus;&space;\dots&space;&plus;&space;\gamma^{n&space;-1}&space;R_{t&space;&plus;&space;n}&space;&plus;&space;\gamma^n&space;Q_{t&space;&plus;n&space;-1}(S_{t&space;&plus;&space;n},&space;A_{t&space;&plus;&space;n})" title="G_{t:t + n} = R_{t+1} + \gamma R_{t + 2} + \gamma^2 R_{t + 3} + \dots + \gamma^{n -1} R_{t + n} + \gamma^n Q_{t +n -1}(S_{t + n}, A_{t + n})" />

<img src="https://latex.codecogs.com/svg.latex?Q_{t&space;&plus;n}(S_{t},&space;A_{t})&space;=&space;Q_{t&space;&plus;n&space;-1}(S_{t},&space;A_{t})&space;&plus;&space;\alpha&space;[G_{t:t&space;&plus;&space;n}&space;-&space;Q_{t&space;&plus;n&space;-1}(S_{t},&space;A_{t})]" title="Q_{t +n}(S_{t}, A_{t}) = Q_{t +n -1}(S_{t}, A_{t}) + \alpha [G_{t:t + n} - Q_{t +n -1}(S_{t}, A_{t})]" />


Tendo esse algoritmo, só precisamos de uma política 𝜋, por exemplo, 𝜀-greedy.

## *Off-policy* n-step
Para fazermos uma implementação tecnicamente ¨completa¨ de n-step *off-policy*, seria necessário implementar a funcionalidade de *importance sampling* no n-step buffer. Isso necessariamente requer que avaliemos a *importance sampling ratio* (<img src="https://latex.codecogs.com/svg.latex?\rho_{t:t&plus;n-1}" title="\rho_{t:t+n-1}" />) para cada passo a frente (n) que queremos avaliar.

No entanto, com base nos artigos:
> "Rainbow: Combining Improvements in Deep Reinforcement Learning": https://arxiv.org/pdf/1710.02298.pdf

> "Understanding Multi-Step Deep Reinforcement
Learning: A Systematic Study of the DQN Target": https://arxiv.org/pdf/1901.07510.pdf

decidimos por não integrar *importance sampling* ao modelo pois, para valores de n pequenos comumente como n=3, não aparentam existir impactos significativos da falta desse recurso. Além disso, para valores de n maiores, o treinamento seria mais demorado, sem benefícios claros.

Logo, a única alteração feita para off-policy em relação a on-policy n-step, é utilizar o <img src="https://latex.codecogs.com/svg.latex?max_{a'}&space;Q(S_{t&plus;n},&space;a')" title="max_{a'} Q(S_{t+n}, a')" /> ao invés do <img src="https://latex.codecogs.com/svg.latex?Q(S_{t&plus;n},&space;A_{t&plus;n})" title="Q(S_{t+n}, A_{t+n})" />.
<br/>
<br/>

<img src="https://latex.codecogs.com/svg.latex?G_{t:t&space;&plus;&space;n}&space;=&space;R_{t&plus;1}&space;&plus;&space;\gamma&space;R_{t&space;&plus;&space;2}&space;&plus;&space;\gamma^2&space;R_{t&space;&plus;&space;3}&space;&plus;&space;\dots&space;&plus;&space;\gamma^{n&space;-1}&space;R_{t&space;&plus;&space;n}&space;&plus;&space;\gamma^n&space;max_{a'}&space;Q_{t&space;&plus;n&space;-1}(S_{t&space;&plus;&space;n},&space;a')" title="G_{t:t + n} = R_{t+1} + \gamma R_{t + 2} + \gamma^2 R_{t + 3} + \dots + \gamma^{n -1} R_{t + n} + \gamma^n max_{a'} Q_{t +n -1}(S_{t + n}, a')" />

