# Actor Critic

Os Actor Critics são algoritmos de estado da arte que combinam estimadores de função de valor, como a DQN, com estimadores de política ótima, como o Policy Gradient. Dessa forma, esses algoritmos tendem a ser bem mais robustos do que modelos individuais.

## [Advantage Actor Critic (A2C)](A2C)

Uma das versões mais simples do modelo de Actor Critic. Combina um modelo que estima a Vantagem (A(s, a)) de uma ação com um modelo de Policy Gradient.

## [Deep Deterministic Policy Gradient (DDPG)](DDPG)

Deep Deterministic Policy Gradient (DDPG) é um algoritmo off-policy que aprende simultaneamente uma função Q-valor e uma política. Com a equação de Bellman, aprende a função Q e, com esta, aprende a política.