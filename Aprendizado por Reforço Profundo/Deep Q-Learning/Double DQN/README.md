# Double DQN
> Uma extensão do algoritmo de DQN com correção de viés que estabiliza a performance do treinamento do agente


## Relembrando alguns conceitos

**Algoritmo de Q-Learning:** 

<img src="https://latex.codecogs.com/svg.latex?Q(s,a)&space;\leftarrow&space;Q(s,a)&space;&plus;&space;\alpha&space;[R(s,a)&space;&plus;&space;\gamma&space;\cdot&space;max_{a'}&space;Q'(s',&space;a')&space;-&space;Q(s,a)]" title="Q(s,a) \leftarrow Q(s,a) + \alpha [R(s,a) + \gamma \cdot max_{a'} Q'(s', a') - Q(s,a)]" />

Esse algoritmo, como sabemos, tem como objetivo atualizar as estimativas dos Q valores para os pares estado-ação do ambiente. O valor de Q é atualizado por meio de uma "parcela de correção de erro" (parcela de atualização), com uma taxa de aprendizado α.

A atualização é composta pela recompensa imediata pela última ação tomada **R(s,a)**, o fator de desconto γ multiplicando o o maior valor possível esperado de retorno naquele novo estado (após a última ação) menos o valor atual de Q.

**DQN:**

Para problemas em que o método tabular não dá conta, como visto no [notebook de DQN](../Deep%20Q-Network), utilizamos uma rede neural para estimar os valores Q. Porém, ao utilizar somente uma rede neural, os valores de Q tendem a ser superestimados, gerando treinamento menos eficiente e podendo levar a políticas sub-ótimas. Para tentar estabilizar o treinamento, utilizaremos então uma segunda rede neural, chegando no algoritmo DDQN.

## Teoria
Talvez você tenha notado que no algoritmo de Q-learning nós utilizamos uma estimativa do q-valor para fazer uma estimativa do nosso q-valor, as DDQN's surgiram como o objetivo de lidar com este problema.

Nossa equação para o Target (bootstrap) é a seguinte:

<img src="https://latex.codecogs.com/svg.latex?Q_{bootstrap}(s,a)&space;=&space;r(s,a)&space;&plus;&space;\gamma&space;\cdot&space;max_a&space;Q(s',a)" title="Q_{bootstrap}(s,a) = r(s,a) + \gamma \cdot max_a Q(s',a)" />

O Q target vira a soma da recompensa ao tomar a ação a no estado s, mais o valor máximo de **Q** dentre todas as possíveis ações no estado seguinte descontado do Q anterior.

A função de custo (J) que usaremos para os pesos da rede é dado pela fórmula:

<img src="https://latex.codecogs.com/svg.latex?J(w)&space;=&space;\mathbf{E}&space;[(q(s,a)&space;-&space;Q_w(s,a))^2]" title="J(w) = \mathbf{E} [(q(s,a) - Q_w(s,a))^2]" />

Em que **q(s,a)** é a função valor-ação real do nosso problema, e **Q<sub>w</sub>(s,a)** é o valor estimado a partir dos pesos da rede neural.

Mas o problema enfrentado é que não temos o **q(s,a)**.

O que fazemos então é aproximar nosso **q(s,a)**, obtendo também um **J(w)** aproximado:

<img src="https://latex.codecogs.com/svg.latex?J(w)_{bootstrap}&space;=&space;\mathbf{E}&space;[(Q_{bootstrap}(s,a)&space;-&space;Q_w(s,a))^2]" title="J(w)_{bootstrap} = \mathbf{E} [(Q_{bootstrap}(s,a) - Q_w(s,a))^2]" />

Mas o que pode acontecer a partir disso é que estaremos escolhendo ações que possuem o maior q-valor sem ter tanta certeza de que isso não é um falso positivo, de que não estamos obtendo um q-valor maior para ações não ótimas do que para ações ótimas.

### Solução:

Quando calcularemos o <img src="https://latex.codecogs.com/svg.latex?Q_{bootstrap}" title="Q_{bootstrap}" /> nós usaremos duas redes idênticas para separar a escolha de melhor ação do cálculo do q-valor. 

  - Usamos uma rede DQN para selecionar qual é a melhor ação a ser tomada no próximo estado. (Ação com maior q-valor.)

  -  Usamos uma rede <img src="https://latex.codecogs.com/svg.latex?Q_{bootstrap}" title="Q_{bootstrap}" /> para calcular o q-valor de tomar essa ação no próximo estado.

Ou seja:

  - Rede DQN para escolher melhor ação para o próximo estado:  
    <img src="https://latex.codecogs.com/svg.latex? argmax_a&space;Q(s',a))" title="Q(s', argmax_a Q(s',a))" />

  - Rede <img src="https://latex.codecogs.com/svg.latex?Q_{bootstrap}" title="Q_{bootstrap}" /> calculando **Q** valor da escolha acima:
  
    <img src="https://latex.codecogs.com/svg.latex?Q(s',&space;argmax_a&space;Q(s',a))" title="Q(s', argmax_a Q(s',a))" />


  E seguimos com nossa expressão do TD Target:
  <img src="https://latex.codecogs.com/svg.latex?Q(s,a)&space;=&space;r(s,a)&space;&plus;&space;\gamma&space;\cdot&space;Q(s',&space;argmax_a&space;Q(s',a))" title="Q(s,a) = r(s,a) + \gamma \cdot Q(s', argmax_a Q(s',a))" />

  A Double DQN ajuda assim a reduzir uma estimativa elevada dos q-valores e portando o algoritmo fica mais preciso e mais rápido de treinar. 

