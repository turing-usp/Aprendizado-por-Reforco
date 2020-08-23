# 🧭🥄 Algoritmo &epsilon;-Guloso (&epsilon;-Greedy Algorithm)

## Ideia do Algoritmo
A ideia deste algoritmo é ser uma evolução natural do **Algoritmo Guloso** com a adição de um parâmetro &epsilon; que controla um probabilidade do agente, ao invés de executar apenas ações de **explotação**, realizar uma ação aleatória de **exploração**.

## Psuedo Código do Algoritmo
```
inicialize de a = 1 até k:
  Q(a) <- 0 
  N(a) <- 0 
Percorra para sempre:
  x <- Um número escolhido aleatóriamente entre [0, 1)
  Se x < ϵ:
    A <- Uma ação aleatória
  Caso contário:
    A <- argmax(Q)
  R <- bandit(A) #puxa a alavanca A
  N(A) <- N(A) + 1
  Q(A) <- Q(A) + [R - Q(A)]/N(A) 
 ```

## Problema do Algoritmo
Esse algoritmo é uma boa solução para a questão de **exploração vs explotação** conseguindo equilibrar ambos, e mostra-se ser um algoritmo poderoso. O único problema é que cabe ao usuário escolher o parâmetro &epsilon;. Caso seja escolhido um &epsilon; muito alto, o agente apenas fará ações aleatórias, enquanto que se for um escolhido muito baixo, ele não explorará, ou demorará muito para explorar.
