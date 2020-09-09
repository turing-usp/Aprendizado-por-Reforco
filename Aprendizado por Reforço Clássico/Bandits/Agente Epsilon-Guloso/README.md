# 🧭🥄 Algoritmo &epsilon;-Guloso (&epsilon;-Greedy Algorithm)

Veja a implementação do algoritmo no [notebook!](eps_greedy.ipynb)

## Ideia do Algoritmo
A ideia deste algoritmo é ser uma evolução natural do **Algoritmo Guloso** com a adição de um parâmetro &epsilon; que controla um probabilidade do agente, ao invés de executar apenas ações de **explotação**, realizar uma ação aleatória de **exploração**.

## Pseudo Código do Algoritmo

![Pseudo Algoritmo](imgs/algoritmo.svg)

## Problema do Algoritmo
Esse algoritmo é uma boa solução para a questão de **exploração vs explotação** conseguindo equilibrar ambos, e mostra-se ser um algoritmo poderoso. O único problema é que cabe ao usuário escolher o parâmetro &epsilon;. Caso seja escolhido um &epsilon; muito alto, o agente apenas fará ações aleatórias, enquanto que se for um escolhido muito baixo, ele não explorará, ou demorará muito para explorar.
