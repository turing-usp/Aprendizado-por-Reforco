# Policy Gradient (PG)

###### Veja a implementação do algoritmo no [notebook](PG.ipynb)!

## Conceito

Em todos os métodos que vimos até agora (Monte Carlo, TD/Q-Learning, ...), o agente aprende uma função de valor <img src="https://latex.codecogs.com/svg.latex?V(s&space;|&space;\theta)" title="V(s | \theta)" /> ou <img src="https://latex.codecogs.com/svg.latex?Q(s,a&space;|&space;\theta)" title="Q(s,a | \theta)" />, onde 𝜃 são os parâmetros/pesos do modelo. O agente então segue uma política (𝜀-)gulosa, (quase-)deterministica, derivada da função de valor. Esses métodos são todos aproximações de programação dinâmica e encontram a política ótima de maneira indireta.

Um método alternativo é estimar as políticas ótimas diretamente, ou seja, estimar os parâmetros ótimos 𝜃 para a política <img src="https://latex.codecogs.com/svg.latex?\pi(a&space;|&space;s,&space;\theta)" title="\pi(a | s, \theta)" />.
Os métodos que utilizam gradientes para realizar essa tarefa são chamados de Policy Gradient.

No caso de DQN, nós estimávamos a qualidade de uma ação usando bootstrap e minizávamos o erro entre o agente e esse <img src="https://latex.codecogs.com/svg.latex?Q_{\mathrm{bootstrap}}" title="Q_{\mathrm{bootstrap}}" />. Em PG, a situação é um pouco diferente, porque não é tão simples estimar diretamente algum "<img src="https://latex.codecogs.com/svg.latex?\pi_{\mathrm{bootstrap}}" title="\pi_{\mathrm{bootstrap}}" />". Ao invés disso, utilizamos _gradient ascent_ para maximizar alguma função objetivo, como:

- <img src="https://latex.codecogs.com/svg.latex?J_0(\theta)&space;=&space;V^{\pi_\theta}(s_0)" title="J_0(\theta) = V^{\pi_\theta}(s_0)" /> (valor do estado inicial)
- <img src="https://latex.codecogs.com/svg.latex?J_{\mathrm{mean}V}(\theta)&space;=&space;E_{s|\theta}\left[V^{\pi_\theta}(s)\right]" title="J_{\mathrm{mean}V}(\theta) = E_{s|\theta}\left[V^{\pi_\theta}(s)\right]" /> (valor médio)
- <img src="https://latex.codecogs.com/svg.latex?J_{\mathrm{mean}\mathcal{R}}(\theta)&space;=&space;E_{s,a|\theta}\left[\mathcal{R}_s^a\right]" title="J_{\mathrm{mean}\mathcal{R}}(\theta) = E_{s,a|\theta}\left[\mathcal{R}_s^a\right]" /> (recompensa média)
- <img src="https://latex.codecogs.com/svg.latex?J_{\mathrm{mean}G}(\theta)&space;=&space;E_{\tau|\theta}\left[G_\tau\right]" title="J_{\mathrm{mean}G}(\theta) = E_{\tau|\theta}\left[G_\tau\right]" /> (retorno médio por episódio)

O algoritmo de PG então se reduz a:
<img src="https://latex.codecogs.com/svg.latex?\theta_{k&plus;1}&space;=&space;\theta_k&space;&plus;&space;\alpha&space;\nabla_\theta&space;J(\theta_k)" title="\theta_{k+1} = \theta_k + \alpha \nabla_\theta J(\theta_k)" />,
onde 𝛼 é a taxa de aprendizado. Só falta um detalhe bem importante nessa equação: como calcular o gradiente de J.

Obs: O resto dessa explicação, assim como a tese de referência, assume que a função objetivo é <img src="https://latex.codecogs.com/svg.latex?J(\theta)&space;=&space;J_{\mathrm{mean}G}(\theta)" title="J(\theta) = J_{\mathrm{mean}G}(\theta)" />, ou seja, queremos maximizar o retorno médio por episódio.

## Teorema de Policy Gradient

Definida a nossa função objetivo J, precisamos encontrar seu gradiente para então aplicar o gradiente ascendente. Para qualquer uma das funções objetivo especificadas acima, o gradiente de J é dado por:
<img src="https://latex.codecogs.com/svg.latex?\nabla_\theta&space;J(\theta)&space;=&space;E_{\tau|\theta}\left[\sum_{t=0}^\infty&space;Q(s_t,a_t|\theta)&space;\nabla_\theta&space;\log\pi(a_t|s_t,\theta)\right]" title="\nabla_\theta J(\theta) = E_{\tau|\theta}\left[\sum_{t=0}^\infty Q(s_t,a_t|\theta) \nabla_\theta \log\pi(a_t|s_t,\theta)\right]" />.

A demonstração do teorema encontra-se no [Apêndice](#apendice) deste notebook.

## REINFORCE

**REINFORCE**, o algoritmo mais simples de PG, é obtido ao utilizar a função objetivo do retorno médio por episódio (<img src="https://latex.codecogs.com/svg.latex?J_{\mathrm{mean}G}(\theta)&space;=&space;E_{\tau|\theta}\left[G_\tau\right]" title="J_{\mathrm{mean}G}(\theta) = E_{\tau|\theta}\left[G_\tau\right]" />) para avaliar nosso agente. Neste caso, o gradiente da nossa função objetivo poderia ser estimado por:

<img src="https://latex.codecogs.com/svg.latex?\begin{align*}&space;\nabla_\theta&space;J(\theta)&space;&=&space;E_{\tau|\theta}\left[\sum_{t=0}^\infty&space;Q(s_t,a_t|\theta)&space;\nabla_\theta&space;\log\pi(a_t|s_t,\theta)\right]&space;\\&space;&\approx&space;\sum_{t=0}^T&space;G_t&space;\nabla_\theta&space;\log\pi(a_t|s_t,\theta)&space;\end{align*}" title="\begin{align*} \nabla_\theta J(\theta) &= E_{\tau|\theta}\left[\sum_{t=0}^\infty Q(s_t,a_t|\theta) \nabla_\theta \log\pi(a_t|s_t,\theta)\right] \\ &\approx \sum_{t=0}^T G_t \nabla_\theta \log\pi(a_t|s_t,\theta) \end{align*}" />

Dessa forma, seu algoritmo é dado por:

![REINFORCE](imgs/reinforce.svg)

Note que esse algoritmo é on-policy, pois o cálculo do gradiente depende da distribuição de estados e ações e é válido apenas para a política que gerou essa distribuição.

## REINFORCE com Baseline

Uma extensão dessa ideia é utilizar reinforce com baselines. Nesse método, ao invés de <img src="https://latex.codecogs.com/svg.latex?G_t" title="G_t" />, utilizamos a função _advantage_ <img src="https://latex.codecogs.com/svg.latex?A&space;=&space;G_t&space;-&space;V(s_t)" title="A = G_t - V(s_t)" />, que indica a qualidade de uma ação-estado em relação à qualidade média daquele estado. Para isso, é necessário treinar uma função de valor V(s).

O algoritmo fica:

![Baseline](imgs/baseline.svg)

<a id="apendice"></a>
## Apêndice

## A probabilidade de uma trajetória

Algo que será bem útil é o cálculo da probabilidade de uma trajetória <img src="https://latex.codecogs.com/svg.latex?\tau&space;=&space;(s_0,a_0,s_1,a_1,\dots)" title="\tau = (s_0,a_0,s_1,a_1,\dots)" />. Se a distribuição inicial de estados é dada por <img src="https://latex.codecogs.com/svg.latex?\mu(s)&space;=" title="\mu(s) =" /> _prob. do estado inicial ser_ s, temos:

<img src="https://latex.codecogs.com/svg.latex?p(\tau|\theta)&space;=&space;\mu(s_0)&space;\pi(a_0|s_0,\theta)&space;p(s_1|s_0,a_0)&space;\pi(a_1|s_1,\theta)\cdots" title="p(\tau|\theta) = \mu(s_0) \pi(a_0|s_0,\theta) p(s_1|s_0,a_0) \pi(a_1|s_1,\theta)\cdots" />

Tomando o log dessa expressão, obtemos:

<img src="https://latex.codecogs.com/svg.latex?\begin{align*}&space;\log&space;p(\tau|\theta)&space;&=&space;\log&space;\mu(s_0)&space;&plus;&space;\log\pi(a_0|s_0,\theta)&space;&plus;&space;\log&space;p(s_1|s_0,a_0)&space;&plus;&space;\log&space;\pi(a_1|s_1,\theta)&space;&plus;&space;\cdots&space;=&space;\\&space;&=&space;\log&space;\mu(s_0)&space;&plus;&space;\sum_{t=0}^\infty&space;\left[\log&space;\pi(a_t|s_t,\theta)&space;&plus;&space;\log&space;p(s_{t&plus;1}&space;|&space;s_t,&space;a_t)\right]&space;\end{align*}" title="\begin{align*} \log p(\tau|\theta) &= \log \mu(s_0) + \log\pi(a_0|s_0,\theta) + \log p(s_1|s_0,a_0) + \log \pi(a_1|s_1,\theta) + \cdots = \\ &= \log \mu(s_0) + \sum_{t=0}^\infty \left[\log \pi(a_t|s_t,\theta) + \log p(s_{t+1} | s_t, a_t)\right] \end{align*}" />
Como os únicos termos que dependem de 𝜃 na última expressão são os termos da forma <img src="https://latex.codecogs.com/svg.latex?\log&space;\pi(a_t|s_t,\theta)" title="\log \pi(a_t|s_t,\theta)" />, temos por fim:

<img src="https://latex.codecogs.com/svg.latex?\nabla&space;\log&space;p(\tau|\theta)&space;=&space;\sum_{t=0}^\infty&space;\nabla&space;\log&space;\pi(a_t|s_t,\theta)" title="\nabla \log p(\tau|\theta) = \sum_{t=0}^\infty \nabla \log \pi(a_t|s_t,\theta)" />

## O gradiente de J

Do cálculo, sabemos que:

<img src="https://latex.codecogs.com/svg.latex?\frac{d}{dx}&space;\log&space;x&space;=&space;\frac1x&space;\implies&space;\frac{d}{dx}&space;\log&space;g(x)&space;=&space;\frac{1}{g(x)}&space;g'(x)" title="\frac{d}{dx} \log x = \frac1x \implies \frac{d}{dx} \log g(x) = \frac{1}{g(x)} g'(x)" />

Em cálculo multivariável, vale analogamente:

<img src="https://latex.codecogs.com/svg.latex?\nabla&space;\log&space;g(\theta)&space;=&space;\frac{1}{g(\theta)}&space;\nabla&space;g(\theta),&space;\quad&space;\text{ou&space;seja},&space;\quad&space;\nabla&space;g(\theta)&space;=&space;g(\theta)&space;\nabla&space;\log&space;g(\theta)" title="\nabla \log g(\theta) = \frac{1}{g(\theta)} \nabla g(\theta), \quad \text{ou seja}, \quad \nabla g(\theta) = g(\theta) \nabla \log g(\theta)" />

A função objetivo pode ser escrita em forma integral como:

<img src="https://latex.codecogs.com/svg.latex?J(\theta)&space;=&space;E_{\tau|\theta}\left[G_\tau\right]&space;=&space;\int_\tau&space;p(\tau|\theta)&space;G_\tau&space;d\tau" title="J(\theta) = E_{\tau|\theta}\left[G_\tau\right] = \int_\tau p(\tau|\theta) G_\tau d\tau" />

O gradiente de J fica então:

<img src="https://latex.codecogs.com/svg.latex?\begin{align*}&space;\nabla&space;J(\theta)&space;&=&space;\nabla_\theta&space;\int_\tau&space;p(\tau|\theta)&space;\cdot&space;G_\tau&space;d\tau&space;\\&space;&=&space;\int&space;G_\tau&space;\cdot&space;\nabla_\theta&space;p(\tau|\theta)&space;d\tau&space;\\&space;&=&space;\int&space;G_\tau&space;\cdot&space;p(\tau|\theta)&space;\nabla_\theta&space;\log&space;p(\tau|\theta)&space;d\tau&space;\\&space;&=&space;\int&space;p(\tau|\theta)&space;\cdot&space;G_\tau&space;\nabla_\theta&space;\log&space;p(\tau|\theta)&space;d\tau&space;\\&space;&=&space;E_{\tau|\theta}\left[G_\tau&space;\nabla_\theta&space;\log&space;p(\tau|\theta)\right]&space;\\&space;&=&space;E_{\tau|\theta}\left[G_\tau&space;\sum_{t=0}^\infty&space;\nabla_\theta&space;\log&space;\pi(a_t|s_t,\theta)\right]&space;\end{align*}" title="\begin{align*} \nabla J(\theta) &= \nabla_\theta \int_\tau p(\tau|\theta) \cdot G_\tau d\tau \\ &= \int G_\tau \cdot \nabla_\theta p(\tau|\theta) d\tau \\ &= \int G_\tau \cdot p(\tau|\theta) \nabla_\theta \log p(\tau|\theta) d\tau \\ &= \int p(\tau|\theta) \cdot G_\tau \nabla_\theta \log p(\tau|\theta) d\tau \\ &= E_{\tau|\theta}\left[G_\tau \nabla_\theta \log p(\tau|\theta)\right] \\ &= E_{\tau|\theta}\left[G_\tau \sum_{t=0}^\infty \nabla_\theta \log \pi(a_t|s_t,\theta)\right] \end{align*}" />

### Demonstração do Teorema de Policy Gradient

A demonstração completa e rigorosa pode ser vista no material de referência e, em particular, [nesse material extra](https://spinningup.openai.com/en/latest/spinningup/extra_pg_proof1.html) do Spinning Up. Aqui será passada apenas a ideia básica. Primeiramente, podemos reescrever o gradiente de J como:

<img src="https://latex.codecogs.com/svg.latex?\nabla_\theta&space;J(\theta)&space;=&space;E_{\tau|\theta}\left[\sum_{t=0}^\infty&space;G_\tau&space;\nabla_\theta&space;\log&space;\pi(a_t|s_t,\theta)\right]" title="\nabla_\theta J(\theta) = E_{\tau|\theta}\left[\sum_{t=0}^\infty G_\tau \nabla_\theta \log \pi(a_t|s_t,\theta)\right]" />

Note que para qualquer instante <img src="https://latex.codecogs.com/svg.latex?t=t_i" title="t=t_i" />, essa fórmula considera o retorno total a partir do instante <img src="https://latex.codecogs.com/svg.latex?t=0" title="t=0" />, o que é um pouco contra-intuitivo. Final, o agente deveria considerar apenas as recompensas futuras (<img src="https://latex.codecogs.com/svg.latex?t&space;\ge&space;t_i" title="t \ge t_i" />) ao decidir qual ação tomar. Essa intuição pode ser confirmada matemáticamente, de forma que:

<img src="https://latex.codecogs.com/svg.latex?\begin{align*}&space;\nabla_\theta&space;J(\theta)&space;&=&space;E_{\tau|\theta}\left[\sum_{t=0}^T&space;G_{\tau}^{t:\infty}&space;\nabla_\theta&space;\log&space;\pi(a_t|s_t,\theta)\right]&space;\\&space;&=&space;E_{\tau|\theta}\left[\sum_{t=0}^T&space;Q(s_t,a_t|\theta)&space;\nabla_\theta&space;\log&space;\pi(a_t|s_t,\theta)\right]&space;\end{align*}" title="\begin{align*} \nabla_\theta J(\theta) &= E_{\tau|\theta}\left[\sum_{t=0}^T G_{\tau}^{t:\infty} \nabla_\theta \log \pi(a_t|s_t,\theta)\right] \\ &= E_{\tau|\theta}\left[\sum_{t=0}^T Q(s_t,a_t|\theta) \nabla_\theta \log \pi(a_t|s_t,\theta)\right] \end{align*}" />

Note que assumimos que o episódio tem uma duração máxima T e que a distribuição de estados é estacionária (i.e. <img src="https://latex.codecogs.com/svg.latex?s_t,a_t" title="s_t,a_t" /> tem a mesma distribuição que <img src="https://latex.codecogs.com/svg.latex?a,t" title="a,t" />).