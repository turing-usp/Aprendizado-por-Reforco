# Deep Q-Network

Aqui faremos a adaptação do algoritmo de Q-Learning com a utilização de redes neurais, assim como feito na implementação da DeepMind: https://deepmind.com/research/publications/human-level-control-through-deep-reinforcement-learning

Aconselhemos a leitura da nossa implementação de Q-Learning caso você não esteja tão acostumado com o algoritmo original e os conceitos básicos, pois isso facilitará seu entendimento de uma **DQN** (abreviação de Deep Q-Network). 

## Motivação

Por que "deep"? Ou, por que aprendizado "profundo"?

Q-Learning por si só já é um algoritmo simples e relativamente eficiente para muitos ambientes, mas o que acontece se nosso ambiente for muito grande? E se precisarmos de uma tabela com milhares de estados e ações? 


Será que nosso agente consegue passar por todas as possibilidades de estados e ações para ter uma boa estimativa do Q-Learning? E mais ainda, será que nosso agente **precisa** passar por todos várias vezes?

O uso de **redes neurais** nesse algoritmo veio para que consigamos aproximar Q-Valores a partir de outros estados e ações e assim não precisamos salvar o valor específico de cada configuração.

## Teoria

Então, basicamente, vamos sintetizar a diferença do Q-Learning para DQN:
![](imgs/Tabela-NN.png)

### Q-Learning

- Criamos uma tabela-Q
- Para cada configuração de **Estado/Ação** armazenamos a estimativa do nosso agente do **Q-valor**

### DQN

- Criamos uma rede neural com **N-estados** neurônios de entrada e **N-ações** neurônios de saída
- Colocamos camadas escondidas de acordo com nossa implementação
- A rede recebe o estado e tenta predizer o **Q-valor** para cada ação disponível

A função *loss* será o **erro quadrático médio** entre Q-valor estimado pela rede e o valor real, entretando, por se tratar de um problema de aprendizado por reforço, **não temos o valor real!**. Assim, usamos outra estimativa para o valor real, o que chamamos de *bootstrap*. 

Assim temos:
- Predição: <img src="https://latex.codecogs.com/svg.latex?Q(S_t,&space;A_t)" title="Q(S_t, A_t)" />
- Target: <img src="https://latex.codecogs.com/svg.latex?max_a&space;Q(S_{t&plus;1},&space;a)" title="max_a Q(S_{t+1}, a)" />

E nossa função fica, assim como já visto em Q-Learning:

<img src="https://latex.codecogs.com/svg.latex?Q(S_t,&space;A_t)&space;\leftarrow&space;Q(S_t,&space;A_t)&space;&plus;&space;\alpha&space;[R_{t&plus;1}&space;&plus;&space;\gamma&space;max_a&space;Q(S_{t&plus;1},&space;a)&space;-&space;Q(S_t,&space;A_t)]" title="Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \alpha [R_{t+1} + \gamma max_a Q(S_{t+1}, a) - Q(S_t, A_t)]" />

### Experience Replay 

Pelo jeito que as redes neurais "aprendem", não é muito eficiente passar os dados coletados pelo agente enquanto ele explora o ambiente, é mais efetivo que nosso agente colete várias experiências e, após termos muitos dados, ir "alimentando" nossa rede. 

Esse tipo de aprendizado é chamado de **off-policy**, porque ele não acontece ao mesmo tempo em que nosso agente explora o ambiente.

Aqui nós utilizaremos o **Experience Replay**, em que armazemos as experiências do nosso agente na forma <img src="https://latex.codecogs.com/svg.latex?(s_t,&space;a_t,&space;r_t,&space;s_{t&plus;1})" title="(s_t, a_t, r_t, s_{t+1})" />, ou seja, o **estado** <img src="https://latex.codecogs.com/svg.latex?s_t" title="s_t" /> em que ele estava, a **ação** <img src="https://latex.codecogs.com/svg.latex?a_t" title="a_t" /> que ele tomou naquele estado, a **recompensa** <img src="https://latex.codecogs.com/svg.latex?r_t" title="r_t" /> que ele recebeu por tomar aquela ação naquele estado e o **próximo estado** <img src="https://latex.codecogs.com/svg.latex?s_{t&plus;1}" title="s_{t+1}" /> que o agente foi após aquela ação.

Após coletarmos um certo número dessas tuplas <img src="https://latex.codecogs.com/svg.latex?(s_t,&space;a_t,&space;r_t,&space;s_{t&plus;1})" title="(s_t, a_t, r_t, s_{t+1})" />, nós passamos aleatoriamente esses dados para a rede aprender.

### Pseudo Código do Algoritmo

![Pseudo Algoritmo](imgs/algoritmo.svg)