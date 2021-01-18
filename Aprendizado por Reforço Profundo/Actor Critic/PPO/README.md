# Proximal Policy Optimization (PPO)

Como vimos na aula de A2C, uma função objetivo muito utilizada é:

<img src="https://latex.codecogs.com/svg.latex?J(\theta)&space;=&space;\mathbb{E}_{s,a\sim\pi_\theta}&space;[A^{\pi_\theta}_w(s,a)],&space;\qquad&space;\nabla_\theta&space;J(\theta)&space;=&space;\mathbb{E}_{s,a\sim\pi_\theta}&space;[\nabla_\theta&space;\log&space;\pi_\theta(a|s)\cdot&space;A^{\pi_\theta}_w(s,a)]." title="J(\theta) = \mathbb{E}_{s,a\sim\pi_\theta} [A^{\pi_\theta}_w(s,a)], \qquad \nabla_\theta J(\theta) = \mathbb{E}_{s,a\sim\pi_\theta} [\nabla_\theta \log \pi_\theta(a|s)\cdot A^{\pi_\theta}_w(s,a)]." />

Os índices na função _advantage_ **A** indicam que **A** depende tanto dos pesos **w** utilizados para calcular o estimar de cada estado, quanto da política **&pi;<sub>&theta;</sub>**, que determina quais trajetórias o agente vai seguir dentro do ambiente.

> Obs: pode-se mostrar que essa formulação é equivalente à formulação que utiliza somatórias no tempo:

<img src="https://latex.codecogs.com/svg.latex?J(\theta)&space;=&space;\mathbb{E}_{(s_0,a_0,\dots)\sim\pi_\theta}&space;\left[\sum_{t=0}^\infty&space;\gamma^t&space;A^{\pi_\theta}_w(s_t,a_t)\right],&space;\qquad&space;\nabla_\theta&space;J(\theta)&space;=&space;\mathbb{E}_{(s_0,a_0,\dots)\sim\pi_\theta}&space;\left[\sum_{t=0}^\infty&space;\nabla_\theta&space;\log&space;\pi_\theta(a_t|s_t)\cdot&space;A^{\pi_\theta}_w(s_t,a_t)\right]." title="J(\theta) = \mathbb{E}_{(s_0,a_0,\dots)\sim\pi_\theta} \left[\sum_{t=0}^\infty \gamma^t A^{\pi_\theta}_w(s_t,a_t)\right], \qquad \nabla_\theta J(\theta) = \mathbb{E}_{(s_0,a_0,\dots)\sim\pi_\theta} \left[\sum_{t=0}^\infty \nabla_\theta \log \pi_\theta(a_t|s_t)\cdot A^{\pi_\theta}_w(s_t,a_t)\right]." />


Note que uma pequena variação no espaço de parâmetros (&Delta;<sub>&theta;</sub> = &alpha;&nabla;<sub>&theta;</sub>J) pode causar uma grande variação no espaço de políticas. Isso significa que, em geral, a taxa de aprendizado **&alpha;** não pode ser muito alta; caso contrário, corremos o risco de obter uma nova política que não funcione. Consequentemente, a eficiência amostral de A2C também é limitada.


## Trust Region Policy Optimization (TRPO)

Uma maneira de resolver esse problema é limitar as variações na política. Para isso, vamos utilizar a divergência KL **KL(&pi;<sub>1</sub> || &pi;<sub>2</sub>)**, que pode ser, simplificadamente, encarada como uma medida da diferença entre duas políticas (ou, em geral, duas distribuições de probabilidade).

TRPO define uma região de confiança (trust region) para garantir que a política nova não se distancie demais da política antiga:

<img src="https://latex.codecogs.com/svg.latex?E_{s\sim\pi_{\theta_{\mathrm{old}}}}\bigl[KL\bigl(\pi_{\mathrm{old}}(\cdot|s)\,||\,\pi(\cdot|s)\bigr)\bigr]&space;\le&space;\delta." title="E_{s\sim\pi_{\theta_{\mathrm{old}}}}\bigl[KL\bigl(\pi_{\mathrm{old}}(\cdot|s)\,||\,\pi(\cdot|s)\bigr)\bigr] \le \delta." />

No entanto, maximizar a função objetivo de A2C sujeito a essas restrições é um pouco complicado. Então, vamos utilizar uma aproximação da função objetivo de A2C:

<img src="https://latex.codecogs.com/svg.latex?L(\theta_{\mathrm{old}},\theta)&space;=&space;E_{s,a\sim\pi_{\theta_{\mathrm{old}}}}&space;\left[\frac{\pi_\theta(a|s)}{\pi_{\theta_{\mathrm{old}}}(a|s)}&space;A^{\pi_{\theta_{\mathrm{old}}}}(s,a)\right]" title="L(\theta_{\mathrm{old}},\theta) = E_{s,a\sim\pi_{\theta_{\mathrm{old}}}} \left[\frac{\pi_\theta(a|s)}{\pi_{\theta_{\mathrm{old}}}(a|s)} A^{\pi_{\theta_{\mathrm{old}}}}(s,a)\right]" />

Ou seja, TRPO consiste em:

<img src="https://latex.codecogs.com/svg.latex?\text{maximizar&space;}&space;E_{s,a\sim\pi_{\theta_{\mathrm{old}}}}&space;\left[\frac{\pi_\theta(a|s)}{\pi_{\theta_{\mathrm{old}}}(a|s)}&space;A^{\pi_{\theta_{\mathrm{old}}}}(s,a)\right]" title="\text{maximizar } E_{s,a\sim\pi_{\theta_{\mathrm{old}}}} \left[\frac{\pi_\theta(a|s)}{\pi_{\theta_{\mathrm{old}}}(a|s)} A^{\pi_{\theta_{\mathrm{old}}}}(s,a)\right]" />

<img src="https://latex.codecogs.com/svg.latex?\text{sujeito&space;a&space;}&space;E_{s\sim\pi_{\theta_{\mathrm{old}}}}\bigl[KL\bigl(\pi_{\mathrm{old}}(\cdot|s)\,||\,\pi(\cdot|s)\bigr)\bigr]&space;\le&space;\delta" title="\text{sujeito a } E_{s\sim\pi_{\theta_{\mathrm{old}}}}\bigl[KL\bigl(\pi_{\mathrm{old}}(\cdot|s)\,||\,\pi(\cdot|s)\bigr)\bigr] \le \delta" />

> Para entender como chegamos **L(&theta;<sub>old</sub>,&theta;)** é uma aproximação de **J(&theta;)**, podemos fazer:

<img src="https://latex.codecogs.com/svg.latex?\begin{align*}&space;J(\theta)&space;&=&space;E_{\pi_\theta}[A^{\pi_\theta}(s,a)]&space;\\&space;&=&space;E_{\pi_\theta}[A^{\pi_{\theta_{\mathrm{old}}}}(s,a)]&space;\\&space;&=&space;\sum_{s,a}&space;\rho_{\pi_\theta}(s)\cdot&space;\pi_\theta(a|s)&space;\cdot&space;A^{\pi_{\theta_{\mathrm{old}}}}(s,a)&space;\\&space;&=&space;\sum_{s,a}&space;\rho_{\pi_\theta}(s)\cdot&space;\pi_{\theta_{\mathrm{old}}}(a|s)&space;\cdot&space;\frac{\pi_\theta(a|s)}{\pi_{\theta_{\mathrm{old}}}(a|s)}A^{\pi_{\theta_{\mathrm{old}}}}(s,a)&space;\\&space;&\approx&space;\sum_{s,a}&space;\rho_{\pi_{\theta_{\mathrm{old}}}}(s)\cdot&space;\pi_{\theta_{\mathrm{old}}}(a|s)&space;\cdot&space;\frac{\pi_\theta(a|s)}{\pi_{\theta_{\mathrm{old}}}(a|s)}A^{\pi_{\theta_{\mathrm{old}}}}(s,a)&space;\\&space;&=&space;E_{\pi_{\theta_{\mathrm{old}}}}&space;\left[\frac{\pi_\theta(a|s)}{\pi_{\theta_{\mathrm{old}}}(a|s)}&space;A^{\pi_\theta}(s,a)\right]&space;\end{align*}" title="\begin{align*} J(\theta) &= E_{\pi_\theta}[A^{\pi_\theta}(s,a)] \\ &= E_{\pi_\theta}[A^{\pi_{\theta_{\mathrm{old}}}}(s,a)] \\ &= \sum_{s,a} \rho_{\pi_\theta}(s)\cdot \pi_\theta(a|s) \cdot A^{\pi_{\theta_{\mathrm{old}}}}(s,a) \\ &= \sum_{s,a} \rho_{\pi_\theta}(s)\cdot \pi_{\theta_{\mathrm{old}}}(a|s) \cdot \frac{\pi_\theta(a|s)}{\pi_{\theta_{\mathrm{old}}}(a|s)}A^{\pi_{\theta_{\mathrm{old}}}}(s,a) \\ &\approx \sum_{s,a} \rho_{\pi_{\theta_{\mathrm{old}}}}(s)\cdot \pi_{\theta_{\mathrm{old}}}(a|s) \cdot \frac{\pi_\theta(a|s)}{\pi_{\theta_{\mathrm{old}}}(a|s)}A^{\pi_{\theta_{\mathrm{old}}}}(s,a) \\ &= E_{\pi_{\theta_{\mathrm{old}}}} \left[\frac{\pi_\theta(a|s)}{\pi_{\theta_{\mathrm{old}}}(a|s)} A^{\pi_\theta}(s,a)\right] \end{align*}" />


## Proximal Policy Optimization (PPO)

Como já foi mencionado, a restrição (**KL < &delta;**) imposta em TRPO torna o algoritmo relativamente complicado. PPO é uma tentativa de simplificar esse algoritmo. Ao invés de utilizar trust regions, PPO mexe diretamente com a função objetivo:


<img src="https://latex.codecogs.com/svg.latex?L(\theta_{\mathrm{old}},\theta)&space;=&space;E_{s,a\sim\pi_{\theta_{\mathrm{old}}}}&space;\Bigl[\min\left(r&space;A^{\pi_{\theta_{\mathrm{old}}}}(s,a),\,&space;\operatorname{clip}(r,1-\varepsilon,1&plus;\varepsilon)&space;A^{\pi_{\theta_{\mathrm{old}}}}(s,a)\right)\Bigr]," title="L(\theta_{\mathrm{old}},\theta) = E_{s,a\sim\pi_{\theta_{\mathrm{old}}}} \Bigl[\min\left(r A^{\pi_{\theta_{\mathrm{old}}}}(s,a),\, \operatorname{clip}(r,1-\varepsilon,1+\varepsilon) A^{\pi_{\theta_{\mathrm{old}}}}(s,a)\right)\Bigr]," />

<img src="https://latex.codecogs.com/svg.latex?r&space;=&space;\frac{\pi_\theta(a|s)}{\pi_{\theta_{\mathrm{old}}}(a|s)}" title="r = \frac{\pi_\theta(a|s)}{\pi_{\theta_{\mathrm{old}}}(a|s)}" />

Essa função pode ser reescrita como:

<img src="https://latex.codecogs.com/svg.latex?L(\theta_{\mathrm{old}},\theta)&space;=&space;E_{s,a\sim\pi_{\theta_{\mathrm{old}}}}&space;\Bigl[\min\left(r&space;A^{\pi_{\theta_{\mathrm{old}}}}(s,a),\,&space;g(\varepsilon,&space;A^{\pi_{\theta_{\mathrm{old}}}}(s,a))\right)\Bigr]," title="L(\theta_{\mathrm{old}},\theta) = E_{s,a\sim\pi_{\theta_{\mathrm{old}}}} \Bigl[\min\left(r A^{\pi_{\theta_{\mathrm{old}}}}(s,a),\, g(\varepsilon, A^{\pi_{\theta_{\mathrm{old}}}}(s,a))\right)\Bigr]," />

<img src="https://latex.codecogs.com/svg.latex?\quad&space;g(\varepsilon,&space;A)&space;=&space;\begin{cases}&space;(1&plus;\varepsilon)&space;A,&space;&&space;A&space;\ge&space;0&space;\\&space;(1-\varepsilon)&space;A,&space;&&space;A&space;<&space;0.&space;\end{cases}" title="\quad g(\varepsilon, A) = \begin{cases} (1+\varepsilon) A, & A \ge 0 \\ (1-\varepsilon) A, & A < 0. \end{cases}" />


Nota-se que:
- Quando a vantagem é positiva, se **r** aumentar, então **L** aumenta. No entanto, esse benefício é limitado pelo clip: se **r > 1+&epsilon;**, não há mais benefício para **r** aumentar.
- Quando a vantagem é negativa, se **r** diminuir, então **L** aumenta. No entanto, esse benefício é limitado pelo clip: se **r < 1-&epsilon;**, não há mais benefício para **r** diminuir.

A seguinte imagem pode te ajudar a visualizar o clip. Note que todos os valores fora do clip estipulado estão constantes:

![imagem ilustrando o clip](imgs/clip.png)
