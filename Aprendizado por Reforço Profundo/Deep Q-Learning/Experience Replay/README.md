# 🔁 Experience Replay

Uma grande desvantagem das redes neurais é a necessidade de treinar com uma grande quantidade de dados para obter um bom aprendizado. Isso torna seu uso em algoritmos "online" como os de Temporal Difference bem difícil, já que ela recebe apenas uma transição a cada instante de tempo para o treinamento.

Entretanto, como Q-Learning é um algoritmo off-policy, nós podemos aproveitar as experiências anteriores do nosso agente para utilizar em um batch no treinamento da nossa rede. É dessa ideia que surge o conceito do **Experience Replay**, um buffer para guardar todas as experiências passadas do nosso agente.

Para entender como isso funciona, vamos relembrar da atualização do Q-Learning:

<img src="https://latex.codecogs.com/svg.latex?Q(S,&space;A)&space;\leftarrow&space;Q(S,&space;A)&space;&plus;&space;\alpha&space;[R&space;&plus;&space;\gamma&space;\max_{a}Q(S',&space;a)&space;-&space;Q(S,&space;A)]" title="Q(S, A) \leftarrow Q(S, A) + \alpha [R + \gamma \max_{a}Q(S', a) - Q(S, A)]" />

Observe que para atualizar o valor *Q* de um par estado-ação, precisamos saber apenas o estado *S*, a ação tomada *A*, a recompensa recebida *R* e o estado seguinte *S'*. Como esse update não depende da política no momento da escolha da ação, podemos usar uma experiência <img src="https://latex.codecogs.com/svg.latex?(s_t,&space;a_t,&space;r_t,&space;s_{t&plus;1})" title="(s_t, a_t, r_t, s_{t+1})" /> para treinamento a qualquer momento.

Dessa forma, o que podemos fazer é guardar esses pares <img src="https://latex.codecogs.com/svg.latex?(s_t,&space;a_t,&space;r_t,&space;s_{t&plus;1})" title="(s_t, a_t, r_t, s_{t+1})" /> em um buffer, e amostrar uma batch dessas experiências passadas para cada treinamento. Assim, conseguimos reaproveitar as experiências obtidas pelo nosso agente e aumentar a *sample efficiency* do nosso algoritmo, ou seja, sua eficiência dado uma quantidade limitada de experiências.