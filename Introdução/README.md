# 👩‍🏫 Introdução

> Se você se interessar por uma introdução mais prática ao assunto, temos um [**Workshop Introdutório de Aprendizado por Reforço**](https://youtu.be/FxcWqI-l29E) disponível gratuitamente no YouTube!

## O que é Aprendizado por Reforço?

O **Aprendizado por Reforço** é uma subárea do Aprendizado de Máquina que estuda programas que aprendem a realizar tarefas complexas por ***tentativa*** e ***erro***, a partir do feedback que ele recebe de suas ações.

Esse tipo de aprendizado se assemelha muito com o processo de aprendizado intuitivo dos seres humanos, no qual o indivíduo experimenta algo, e com base na resposta desse experimento, decide se ele vale a pena ou não. Quando uma criança encosta o dedo em uma superfície quente, por exemplo, ela recebe uma resposta negativa, e não repete a mesma ação novamente.

As técnicas de Aprendizado por Reforço são muito poderosas, já que conseguem gerar comportamentos extremamente complexos, muito difíceis de serem programados, como fazer um robô caminhar ou até correr sem cair.

## Conceitos Importantes

Para poder entender melhor os algoritmos de Aprendizado por Reforço, primeiro é preciso entender alguns **conceitos importantes**.

### Agente

O **Agente** é o nosso algoritmo: é a entidade que **toma as decisões** de como agir, e que **aprende** o melhor comportamento para uma determinada situação com base no feedback de ações passadas.

O papel do agente é análogo ao do nosso cérebro, é ele que processa as informações e decide as próximas ações a se tomar.

### Ambiente

No Aprendizado por Reforço, o **Ambiente** é o espaço que representa o nosso problema: o mundo com o qual o agente pode interagir, e no qual ele deve se basear para a tomada de decisões.

Em uma partida de xadrez, o Ambiente é bem simples: ele consiste no conjunto das peças e do tabuleiro.

![Xadrez](https://miro.medium.com/max/625/0*7-LOSdL2eOEAd9R7)

### Estado

O **Estado** se refere às condições do Agente e do Ambiente em um determinado instante. No xadrez, por exemplo, o Estado é a configuração atual do tabuleiro, ou seja, a posição de todas as peças naquele turno. Essa informação é repassada ao Agente, e é a partir dela que o Agente deve tomar suas decisões.

![Estado](https://miro.medium.com/max/304/0*6PVAVr2qsP3oBO6k.jpg)

Uma observação interessante acerca do Estado é que ele não precisa ser informado em sua totalidade: o Agente, em muitos casos, não possui a informação completa do Ambiente, cabendo a ele deduzir o restante do Estado. Basta pensar em jogos de estratégia como Age of Empires ou Starcraft, em que a posição dos inimigos é encoberta até eles entrarem no seu campo de visão.

![Age of Empires](https://miro.medium.com/max/575/0*VQdhNC0eeBLFykU_)

### Ação

O conceito de **Ação** é bem simples: são os **comandos** que o Agente pode escolher em um instante para interagir com o Ambiente. No xadrez, uma Ação é equivalente a um movimento.

![Ação](https://miro.medium.com/max/531/0*JoUU1spyVgWGDs0D.gif)

Já o **Espaço de Ação** é o conjunto de todos as ações possíveis. Ou seja, no xadrez, nosso Espaço de Ação é o conjunto de todas as ações possíveis.

![Espaço de Ação](https://img.itch.zone/aW1nLzEzODQ1NzQuZ2lm/original/8hWPC8.gif)

Uma observação interessante é que o Espaço de Ações pode ser discreto ou contínuo. No caso do xadrez, o Espaço de Ações é discreto, já que existe uma quantidade finita de movimentos que podem ser feitos. Entretanto, no caso de um carro autônomo, o Espaço de Ações é contínuo, visto que podemos mandar qualquer velocidade para as rodas. Lidar com espaços contínuos é consideravelmente mais complexo, e não são todos os algoritmos de RL que conseguem resolver esse tipo de problema.

### Recompensa

A cada ação tomada, o Ambiente devolve um **feedback** ao Agente relatando a **efetividade** daquela ação. Esse feedback é denominado **Recompensa**, e é representado por um número, positivo, negativo ou nulo, tal qual uma pontuação em um jogo.

No caso do Pac-Man, o agente recebe uma recompensa positiva para cada fantasma / bolota comidos, e uma recompensa negativa quando perde uma vida.

![Recompensa](https://miro.medium.com/max/875/0*cLrwq7tnLpqGDpbg.gif)

### Retorno

Como dissemos antes, o objetivo do nosso Agente é maximizar a **soma de todas as recompensas**.

O **Retorno** (<img src="https://latex.codecogs.com/svg.latex?G_t" title="G_t" />) é justamente esse conceito: ele representa o valor da recompensa total a partir de um determinado instante.

Ou seja, se a **Recompensa** era equivalente aos **Pontos** de um jogo, o **Retorno** é análogo ao **Score Total**.

![Retorno](https://miro.medium.com/max/475/0*AiSIzhhdgaVXH2BG.png)

O Retorno é obtido a partir da seguinte equação:

<img src="https://latex.codecogs.com/svg.latex?G_t&space;=&space;R_{t&plus;1}&space;&plus;&space;\gamma&space;R_{t&plus;2}&space;&plus;&space;\gamma^2&space;R_{t&plus;3}&space;&plus;&space;..." title="G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + ..." />

No cálculo do Retorno, somamos todas as recompensas multiplicadas por um  **fator de desconto** (γ) entre 0 e 1. Esse fator faz com que as recompensas mais para o futuro se tornem para vez menores, fazendo o Retorno convergir para um valor real.

Um γ próximo de 1 significa que nosso Retorno leva mais em conta as **recompensas futuras**. Um γ próximo de 0 significa que levamos mais em conta **recompensas recentes**.

### Política (π)

A **Política** se refere ao processo de decisão do Agente: é o algoritmo que ele usa para escolher uma ação para cada estado. Ou seja, é uma função que recebe o **estado atual** e retorna a probabilidade de cada ação ser escolhida.

Vamos pensar no caso do **Pedra, Papel ou Tesoura**: escolher qualquer uma das três ações aleatoriamente é um tipo de política, cuja probabilidade de cada ação é 1/3 para qualquer estado. Uma outra política possível seria escolher sempre a ação que o seu oponente jogou da última vez. Essa segunda política é chamada **determinística**, já que, para um mesmo estado, a ação do nosso agente será sempre a mesma.

![Política](https://miro.medium.com/max/625/0*q6V6Z-LdoTfDQT1y)

Nosso objetivo no Aprendizado por Reforço é descobrir a **Política Ótima** para o nosso agente, que consiste na política que escolhe sempre a melhor ação para cada estado. Essa melhor ação é definida como a ação que vai garantir o maior retorno até o final do jogo.

![Política 2](https://miro.medium.com/max/875/0*L9R23HBRbrbLgrFk.gif)

### Valor de um Estado (V)

O **Valor de um Estado** específico consiste no retorno esperado a partir daquele determinado estado.

<img src="https://latex.codecogs.com/svg.latex?v_\pi(s)&space;=&space;\mathbf{E}_\pi\left[G_t&space;|&space;S_t&space;=&space;s&space;\right]" title="v_\pi(s) = \mathbf{E}_\pi\left[G_t | S_t = s \right]" />

Basicamente o valor que representa a recompensa total que costumamos receber após passar por aquele estado, ou seja, **quão bom é estar naquele estado**.

Com o **Valor de um Estado**, podemos escolher Ações que nos levem a Estados que tenham maior Valor. Se o valor de um estado S1 é maior que o valor de um estado S2, devemos tentar chegar em S1.

![Valor de um Estado](https://miro.medium.com/max/875/0*VOBcy2zUf-1-efUm.jpg)

Esse labirinto é um ótimo exemplo de como usamos o **Valor**: se estamos no estado cujo valor é -15, nós podemos ir para os estados cujos valores são -16, -16 ou -14. Como nesse caso o estado de maior valor é o de -14, a ação que devemos tomar é ir para cima!

### Valor-Ação (q)

O **Valor de uma Ação** consiste no retorno esperado a partir do momento em que se toma aquela ação.

<img src="https://latex.codecogs.com/svg.latex?q_\pi(s,&space;a)&space;=&space;\mathbf{E}_\pi\left[G_t&space;|&space;S_t&space;=&space;s,&space;A_t&space;=&space;a&space;\right]" title="q_\pi(s, a) = \mathbf{E}_\pi\left[G_t | S_t = s, A_t = a \right]" />

Dessa forma, o valor q de uma ação representa sua **qualidade**, ou quão bom é tomar aquela ação em um determinado estado.

![Valor-Ação](https://homes.cs.washington.edu/~izadinia/images/QValueUpdate_Q-Learning_epsilonGreedy.gif)

O objetivo de muitos algoritmos de Aprendizado por Reforço é **estimar** os valores q de cada ação, para então escolher quais ações tomar escolhendo aquela de maior q.


### Diagrama

No final, o diagrama que acaba representando a Aprendizado por Reforço é o seguinte:

![Diagrama](https://miro.medium.com/max/875/0*DcAwmRiUw8shV2Kh.png)

O **Agente** interage com o **Ambiente** por meio de uma **Ação** escolhida por uma **Política** com base no **Estado** atual, recebendo uma **Recompensa** indicando sua efetividade e o Estado seguinte, assim repetindo o ciclo.