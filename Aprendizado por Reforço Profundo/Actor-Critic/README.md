# Actor Critic

Os Actor Critics são algoritmos de estado da arte que combinam estimadores de função de valor, como a DQN, com estimadores de política ótima, como o Policy Gradient. Dessa forma, esses algoritmos tendem a ser bem mais robustos do que modelos individuais.

## [Advantage Actor Critic (A2C)](A2C)

Uma das versões mais simples do modelo de Actor Critic. Combina um modelo que estima a Vantagem (A(s, a)) de uma ação com um modelo de Policy Gradient.

## [Proximal Policy Optimization (PPO)](PPO)

Um algoritmo poderoso, que visa melhorar o modelo de A2C sem aumentar muito sua complexidade. Utiliza a ideia de Trust Region Policy Optimization (TRPO) para limitar variações na política.