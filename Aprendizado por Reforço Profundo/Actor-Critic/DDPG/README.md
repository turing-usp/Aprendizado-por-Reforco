# DDPG - Deep Deterministic Policy Gradient

Deep Deterministic Policy Gradient (DDPG) é um algoritmo off-policy que aprende simultaneamente uma função Q-valor e uma política. Com a equação de Bellman, aprende a função Q e, com esta, aprende a política.

A ideia de um algoritmo com gradiente da política surgiu primeiro com [Silver (sempre ele)](http://proceedings.mlr.press/v32/silver14.pdf), mas o algoritmo DDPG em si foi estabelecido na publicação [por Lilicrap](https://arxiv.org/abs/1509.02971).

## O algoritmo de DDPG

Este algoritmo é um Actor-Critic, mas, diferentemente dos que vimos antes, é off policy. Diferente do que estamos acostumados, este algoritmo só pode ser usado em espaços de ação contínuos. Podemos pensar então no DDPG como uma "DQN para espaço de ação contínuo".

$$a^*(s) = arg max_a Q^*(s,a)$$

A equação acima, da ação ótima para um dado estado, é familiar, mas se torna problemática para ações não discretas. É fácil contabilizar o máximo de uma série finita de ações, mas ações contínuas tornam essa operação problemática.

Como sabemos que o espaço de ações é contínuo, podemos definir a política (ou função ator) $\mu_\theta(s) $, que vai nos ajudar a computar o max. Lembrando que, nesse algoritmo, a política é determinística.

Dessa forma, temos então $max_a Q(s,a) \approx Q(s, \mu(s))$, facilitando a computação do max.

### Q-Learning

$$Q^*(s,a) = E_{s \sim P} \bigg[r(s,a) + \gamma max_{a'} Q^*(s',a') \bigg] $$

A parte de Q learning, cuja equação para encontrar o valor ótimo de Q está acima, consiste em minimizar o erro quadrático médio de Bellman (MSBE), próximo do que já se era feito com a DQN.

O [post da OpenAI](https://spinningup.openai.com/en/latest/algorithms/ddpg.html) oferece duas ferramentas para facilitar o treinamento da função Q, o uso de Replay Buffers e o uso de Target Networks. Uma vantagem de DDPG ser off-policy é permitir o uso de Replay Buffers.


### Policy Gradient

O objetivo é achar a política determinística $\mu_{\theta}(s) $ que fornece a ação que maximiza $Q(s,a)$. Diferenciando a função Q em a, é possível então realizar gradiente ascendente para maximizar a política:

$$\nabla_\theta J = \mathbb{E}_{s_t} \bigg[ \nabla_a Q(s,a|\theta^Q) |_{s = s_t, a = \mu(s_t)} \nabla_\theta \mu_\theta(s|\theta^\mu)|_{s = s_t} \bigg] $$


## Exploração

Um problema para casos de ação contínua é a exploração. Por outro lado, por se tratar de um algoritmo off-policy, podemos tratar o problema da exploração independente do algoritmo de aprendizado. Dessa forma, podemos criar uma política de exploração $\mu'$ adicionando ruído na nossa política/função ator:

$$\mu'(s) = \mu_\theta(s) + \mathcal{N} $$

No paper original, o ruído foi gerado por um processo [Ornstein-Uhlenbeck](https://en.wikipedia.org/wiki/Ornstein%E2%80%93Uhlenbeck_process). Porém, a openAI recomenda o uso de um ruído gaussiano não correlacionado e de média zero, por ser mais simples e funcionar tão bem quanto.


## Pseudocódigo

![DDPG](https://i.postimg.cc/bwfJDNFb/DDPG-1.png)


## Referências
https://spinningup.openai.com/en/latest/algorithms/ddpg.html

http://proceedings.mlr.press/v32/silver14.pdf