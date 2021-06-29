# 📅 Temporal-Difference Learning

Métodos de **Temporal-Difference** são algoritmos de Aprendizado por Reforço que aprendem utilizando principalmente técnicas de *bootstrapping* (uma estimativa a base de amostragem) da sua função de valor. Esses métodos amostram do ambiente, assim como métodos de Monte Carlo, mas fazem atualizações com base em estimativas intermediárias. Ou seja, enquanto métodos de Monte Carlo atualizam as suas predições apenas no fim do episódio (quando todos os retornos já são conhecidos), métodos de  **Temporal-Difference** atualizam as suas predições a cada instante de tempo, utilizando *bootstrapping* para estimar o retorno do episódio.

## Algoritmos

 - [Q-Learning](Q-Learning)
