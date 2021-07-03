# 🧠 Aprendizado por Reforço Profundo

O **Aprendizado por Reforço Profundo** é a combinação do Aprendizado por Reforço com o Aprendizado Profundo (Deep Learning). Nesta área, são utilizadas **redes neurais**, potentes modelos de reconhecimento de padrões, para aprender e estimar importantes funções, como a política ótima de um agente ou a função de valor de um problema.

Como todos os algoritmos serão construídos a partir de redes neurais, é recomendado utilizar algum framework de Deep Learning, como o PyTorch ou o Tensorflow. Neste repositório, todas as redes serão criadas usando o PyTorch. Caso não esteja muito familiarizado com esta biblioteca, recomendamos os seguintes materiais:

 - **[👨‍🏫 Workshop de Redes Neurais com PyTorch](https://www.youtube.com/watch?v=DVtp6TnZ-fc)**
 - **[📃 Construindo uma Rede Neural do zero | Pytorch](https://medium.com/turing-talks/construindo-uma-rede-neural-do-zero-pytorch-671ee06fbbe1)**

## [Deep Q-Learning](Deep%20Q-Learning)

Um dos algoritmos mais comuns em aprendizado por reforço, quando se trata de aprendizado profundo, é o **Deep Q-Learning**, ou DQN na forma abreviada. DQN é a versão profunda do algoritmo clássico de Q-Learning, em que agora utilizamos uma rede neural que recebe nosso estado e devolve os Q-Valores para cada possível ação do nosso agente.

DQN's são alternativas muito boas ao Q-Learning quando precisamos lidar com problemas que contêm diversos estados, tornando a computação mais leve e o aprendizado mais eficaz.

## [Policy Gradient](Policy%20Gradient)

Quase todos os métodos vistos anteriormente ([métodos tabulares](../Aprendizado%20por%20Reforço$20Clássico) e [DQN](#Deep%20Q-Learning)) estimam a função de valor ótima _Q_\*(_s_,_a_) e, a partir de de _Q_\*, obtém uma política (&epsilon;-)gulosa. Os métodos de policy gradient tem uma proposta alternativa: eles estimam diretamente a política ótima.

## [Actor Critic](Actor-Critic)

Os Actor Critics são algoritmos de estado da arte que combinam estimadores de função de valor, como a DQN, com estimadores de política ótima, como o Policy Gradient. Dessa forma, esses algoritmos tendem a ser bem mais robustos do que modelos individuais.
