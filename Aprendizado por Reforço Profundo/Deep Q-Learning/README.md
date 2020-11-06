# Deep Q-Learning

Um dos algoritmos mais comuns em aprendizado por reforço, quando se trata de aprendizado profundo, é o **Deep Q-Learning**, ou DQN na forma abreviada. DQN é a versão profunda do algoritmo clássico de Q-Learning, em que agora utilizamos uma rede neural que recebe nosso estado e devolve os Q-Valores para cada possível ação do nosso agente.

DQNs são alternativas muito boas ao Q-Learning quando precisamos lidar com problemas que contém diversos estados, tornando a computação mais leve e o aprendizado mais eficaz.

## [Deep Q-Network (DQN)](Deep%20Q-Network)

A versão profunda do Q-Learning, utilizando uma rede neural para aproximar a função de valor Q.

## [Experience Replay](Experience%20Replay)

Buffer que guarda as experiências amostradas em um ambiente para serem utilizadas no treinamento de algoritmos off-policy, de modo a aumentar sua eficiência.

## [Prioritized Experience Replay](Experience%20Replay)

Versão alternativa do Replay Buffer. Ao invés de amostrar experiências aleatoriamente, o buffer de PER dá peso maior às experiências que são mais importantes para o agente.

## [N-step DQN](N-step%20DQN)

A **N-Step DQN** é uma extensão da DQN que utiliza a informação de uma sequência de várias transições para o cálculo da função de valor, gerando targets mais estáveis.
