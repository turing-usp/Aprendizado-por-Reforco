
# 📈 Algoritmo de Limite de Confiança Superior (UCB)

## Ideia do Algoritmo
A ideia deste algoritmo é utilizar uma função matemática que avalia ações tomadas com menos frequência de tal maneira que incentive o agente a pegá-las, incentivando a **exploração**.
A função é dada desta maneira:

$UCB_a = Q_t(a) + c \sqrt{\frac{\ln(t)}{N_t(a)}}$ de $a=1$ até $k$.

Onde: 
$Q_t(a)$ é o valor estimado da a ação $a$ no tempo $t$
$c$ é o parâmetro que controla a **desconfiança**.
$t$ é o número de iterações que ocorreram.
$N_t(a)$ é o número de vezes que a ação $a$ foi escolhida até o tempo $t$.

Então aplica-se a função em $Q_t(a)$ de $a=1$ até $k$ e utiliza-se a função $argmax(UCB)$, assim obtendo o índice do maior valor após $UCB$ ser aplicado em $Q_t$.

## Entendo a função
A parte da função que está dentro da raiz quadrada é a **desconfiança**. Conforme $N_t(a)$ cresce - como ele está no denominador - o valor da **desconfiança** caí. Analogamente, quando $t$ cresce, o valor aumenta. Porém, como ele está dentro de um logaritmo, isso significa que seus aumentos serão bem menores com o passar do tempo. O parâmetro $c$ ajuda a definir o quão relevante essa desconfiança será.

Isso significa que nas primeiras iterações o valor de **desconfiança** será maior, principalmente para ações menos frequentes, e como essa desconfiança é somada aos $Q$ valores estimados por nosso agente, a função $argmax(Q_t)$ irá priorizar essas ações. Assim, conforme o agente faz mais ações, como $ln(t)$ crescera bem menos, enquanto $N_t(a)$ continuará crescendo normalmente, o valor de **desconfiança** caíra bastante, tornando assim os valores **conhecidos**.

## Pseudo Código do Algoritmo
```
inicialize de a = 1 até k:
  Q(a) <- 0 
  N(a) <- 0 
Percorra com t para sempre:
  Faça de a = 1 até k:
    UCB(a) = Q(a) + c * sqrt(ln(t)/N(A))
  A <- argmax(UCB)
  R <- bandit(A) #puxa a alavanca A
  N(A) <- N(A) + 1
  Q(A) <- Q(A) + [R - Q(A)]/N(A) 
 ```

## Problema do Algoritmo
Esse algoritmo é uma solução excelente para o problema de $k$-Armed Bandit, e é esse o problema; ele é muito bom apenas para esse problema. Se mudarmos o problema para algo com uma **distribuição probabilística não estacionária** (ou seja, que o valor esperado de cada ação muda) esse algoritmo se demonstra ineficaz.
