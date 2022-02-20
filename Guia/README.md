# 🗺️ Guia de Aprendizado

Boas vindas ao **🗺️ Guia de Aprendizado** do Repositório de Aprendizado por Reforço! Aqui, você encontra sugestões de como seguir os tópicos do repositório de modo a organizar melhor seu aprendizado.

## 💯 Tópicos Introdutórios

- **[Introdução ao Aprendizado por Reforço](../Introdução)**
  - Explica os conceitos básicos da área de Aprendizado por Reforço.
  - Pré-requisitos: Nenhum.
  
## 👨‍🏭 Introduções Práticas

- **[Gym](../Bibliotecas/Gym)**
  - Aprenda como funciona um ambiente na biblioteca do Gym.
  - Pré-requisitos: [Introdução ao Aprendizado por Reforço](../Introdução).

- **[Stable Baselines](../Bibliotecas/Stable%20Baselines)**
  - Aprenda na prática a programar um agente de Aprendizado por Reforço Profundo.
  - Pré-requisitos: [Gym](../Bibliotecas/Gym).

## 🎰 Aprendizado por Reforço Clássico

_adicionar taxonomia aqui_

- **[Bandits](../Aprendizado%20por%20Reforço%20Clássico/Bandits)**
  - O problema mais clássico da área! Aprender a escolher a melhor ação em uma situação simples.
  - Pré-requisitos: [Introdução ao Aprendizado por Reforço](../Introdução).

- **[Monte Carlo](../Aprendizado%20por%20Reforço%20Clássico/Monte%20Carlo)**
  - Um simples método de Aprendizado por Reforço para resolver problemas com mais estados que os Bandits.
  - Pré-requisitos: [Bandits](../Aprendizado%20por%20Reforço%20Clássico/Bandits).
  
- **[Q-Learning](../Aprendizado%20por%20Reforço%20Clássico/Temporal-Difference/Q-Learning)**
  - Um dos algoritmo mais importantes de Aprendizado por Reforço! Mais aplicável que Monte Carlo e Bandits.
  - Pré-requisitos: [Bandits](../Aprendizado%20por%20Reforço%20Clássico/Bandits).
  
## 🧠 Aprendizado por Reforço Profundo

_adicionar taxonomia aqui_

- **[Deep Q-Learning](../Aprendizado%20por%20Reforço%20Profundo/Deep%20Q-Learning)**
  - O algoritmo mais popular de Aprendizado por Reforço Profundo. Um aprimoramento de Q-Learning com redes neurais.
  - Pré-requisitos: [Q-Learning](../Aprendizado%20por%20Reforço%20Clássico/Temporal-Difference/Q-Learning).

- **[Policy Gradient](../Aprendizado%20por%20Reforço%20Profundo/Policy%20Gradient)**
  - Um importante algoritmo de Aprendizado por Reforço profundo que aproxima diretamente a política ótima, sem estimar função de valor.
  - Pré-requisitos: [Monte Carlo](../Aprendizado%20por%20Reforço%20Clássico/Monte%20Carlo).
  
- **[Actor-Critic](../Aprendizado%20por%20Reforço%20Profundo/Actor-Critic)**
  - Algoritmo resultante da poderosa combinação entre Policy Gradient e uma rede neural para estimar a função de valor.
  - Pré-requisitos: [Deep Q-Learning](../Aprendizado%20por%20Reforço%20Clássico/Temporal-Difference/Q-Learning) e [Policy Gradient](../Aprendizado%20por%20Reforço%20Profundo/Policy%20Gradient).
