# 🎰 Aprendizado por Reforço Clássico

## [🎰 Multi-armed Bandits](Bandits)

Um dos problemas mais clássicos e simples em aprendizado por reforço é o problema do *k*-armed Bandit (em português, Roleta de *k*-alavancas). Nele uma inteligência artificial iria para um cassino e encontraria uma roleta com *k* alavancas, lá ela teria que aprender - por meio de aprendizado por reforço - a escolher a alavanca que lhe da mais dinheiro.

## [🏔 Métodos de Monte Carlo](Monte%20Carlo)

Os métodos de **Monte Carlo** são algoritmos de Aprendizado por Reforço que estimam as funções de valor com base em suas *experiências*, obtidas através da interação com o ambiente. Nesses métodos, os valores são obtidos a partir do cálculo da média dos retornos de cada episódio.

## [📅 Temporal-Difference Learning](Temporal-Difference)
Métodos de **Temporal-Difference** são algoritmos de Aprendizado por Reforço que aprendem utilizando principalmente técnicas de *bootstrapping* (uma estimativa a base de amostragem) da sua função de valor. Esses métodos amostram do ambiente (assim como métodos de Monte Carlo), mas fazem atualizações com base em estimativas atuais. Ou seja, enquanto métodos de Monte Carlo atualizam apenas quando a saída final já é sabida, **Temporal-Difference** atualiza as predições para representarem valores mais tardios sobre o futuro antes do resultado final já ser conhecido.