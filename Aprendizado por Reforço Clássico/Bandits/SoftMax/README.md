# 🎯 Algoritmo com Softmax
Veja a implementação do algoritmo no [notebook!](softmax.ipynb)

## Ideia do Algoritmo

Nos outros algoritmos de Bandits tivemos métodos que estipulavam o valor *Q* das ações do agente, o qual utilizava esses valores para tomar suas ações. Por mais que este seja um método bem eficaz, ele não é único. Este algoritmo tem como finalidade usar um parâmetro de *preferência H*<sub>t</sub>(&alpha;) (preferência estimada da ação &alpha; no tempo *t*). Quanto maior essa preferência maior será a probabilidade do agente tomar essa ação.

Para transformarmos esses valores de preferência em valores probabilísticos, utilizamos a função *Softmax*:

<img src="https://latex.codecogs.com/svg.latex?Pr[A_t&space;=&space;a]&space;\doteq&space;\frac{e^{H_t(a)}}{\sum^{k}_{b=1}e^{H_t(b)}}&space;\doteq&space;\pi_t(a)" title="Pr[A_t = a] \doteq \frac{e^{H_t(a)}}{\sum^{k}_{b=1}e^{H_t(b)}} \doteq \pi_t(a)" />

Aqui também vemos a utilização de uma notação bem utilizada em Aprendizado Por Reforço a *&pi;<sub>t</sub>*(&alpha;), que significa a probabilidade da ação &alpha; no tempo *t*.

## Entendendo a Função

Se você já estudou outras áreas de Aprendizado de Máquina já deve ter se deparado com a função *Softmax*. O que ela basicamente faz é receber um vetor (lista) de valores numéricos e os transforma em valores probabilísticos. Em outras palavras, quanto maior for o valor da *preferência* daquela ação, depois que essa lista de valores passar pela função *Softmax*, maior será a probabilidade do agente escolher aquela ação.

Isso se deve pois os valores de preferência *H<sub>t</sub>*(&alpha;) estão sendo elevados pela função exponencial (ou seja,  valores grandes de *H<sub>t</sub>*(&alpha;) ficam ainda mais prováveis) e sendo divididos pela soma desses exponenciais, normalizando os valores e transformando a soma deles em 1, assim, transformando-os em probabilidades.

## Atualizando as preferências *H*

Como não estamos usando mais a estimação de *Q* valores, não podemos usar a mesma função para atualizar as preferências *H*. Para essa função utilizamos a ideia de **Método do Gradiente** com um parâmetro definido pelo usuário _**&alpha;**_, que serve para controlar o quanto o algoritmo ajustara os valores das preferências *H*.

<img src="https://latex.codecogs.com/svg.latex?H_{t&plus;1}(A_t)&space;=&space;H_t(A_t)&space;&plus;&space;\alpha&space;(R_t&space;-&space;\bar{R}_t)(1-\pi_t(A_t))" title="H_{t+1}(A_t) = H_t(A_t) + \alpha (R_t - \bar{R}_t)(1-\pi_t(A_t))" />


 e para todo &alpha; ≠ *A<sub>t</sub>*

<img src="https://latex.codecogs.com/svg.latex?H_{t&plus;1}(a)&space;=&space;H_t(a)&space;&plus;&space;\alpha&space;(R_t&space;-&space;\bar{R}_t)\pi_t(a)" title="H_{t+1}(a) = H_t(a) + \alpha (R_t - \bar{R}_t)\pi_t(a)" />

<img src="https://latex.codecogs.com/svg.latex?\bar{R_t}" title="\bar{R_t}" /> é a média das recompensas até o tempo *t*.

## Pseudo Código do Algoritmo

![Pseudo Algoritmo](imgs/algoritmo.svg)
