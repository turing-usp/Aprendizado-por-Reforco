# Deep Q-Learning

Um dos algoritmos mais comuns em aprendizado por reforço, quando se trata de aprendizado profundo, é o **Deep Q-Learning**, ou DQN na forma abreviada. DQN é a versão profunda do algoritmo clássico de Q-Learning, em que agora utilizamos uma rede neural que recebe nosso estado e devolve os Q-Valores para cada possível ação do nosso agente.

DQNs são alternativas muito boas ao Q-Learning quando precisamos lidar com problemas que contém diversos estados, tornando a computação mais leve e o aprendizado mais eficaz.

## [Experience Replay](Experience%20Replay)

Buffer que guarda as experiências amostradas em um ambiente para serem utilizadas no treinamento de algoritmos off-policy, de modo a aumentar sua eficiência.

## [Deep Q-Network (DQN)](Deep%20Q-Network)

A versão profunda do Q-Learning, utilizando uma rede neural para aproximar a função de valor Q.

## [Double DQN](Double%20DQN)

Uma extensão do algoritmo de DQN com correção de viés que estabiliza a performance do treinamento do agente

## [N-step DQN](N-step%20DQN)

A **N-Step DQN** é uma extensão da DQN que utiliza a informação de uma sequência de várias transições para o cálculo da função de valor, gerando targets mais estáveis.
