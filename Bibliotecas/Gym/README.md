# OpenAI Gym

Guia de como utilizar a biblioteca e ambientes Gym para projetos de aprendizado por reforço.

Para acessar o guia completo com exemplos de código veja este notebook:

### [Notebook com o guia completo](https://github.com/turing-usp/Aprendizado-por-Reforco/blob/Gym/Bibliotecas/Gym/Gym.ipynb)

## Índice

- [O que é o Gym?](#O-que-é-o-Gym?)
- [Instalação](#Instalação)
    - [Pip](#Pip-(Para-Python-3.5+))
    - [Compile from source](#Compile-from-source)
- [Ambientes](#Ambientes)
- [Observações](#Observações)
- [Espaços](#Espaços)
- [Conclusão](#Conclusão)

## O que é o Gym?

O Gym é um conjunto de ferramentas cujo objetivo é desenvolver e comparar algoritmos de aprendizado por reforço. A biblioteca trata basicamente de um conjunto de _environments_, ou ambientes de teste que o usuário pode utilizar pra treinar e testar seus algoritmos. Vale notar que esses ambientes tem uma interface compartilhada, desta forma torna-se possível escrever algoritmos gerais, agnósticos ao ambiente em que serão inseridos.

## Como usar o Gym

O Gym é utilizado para treinar, testar e comparar algoritmos de aprendizado por reforço dentro dos diversos ambientes oferecidos pela biblioteca e as ferramentas de metrificação implementadas por ela. Essas ferramentas nos oferecem uma base comum para testarmos o desempenho de diversos algoritmos.

## Instalação

A instalação do Gym pode ser realizada de duas formas diferentes:

### Pip (Para Python 3.5+)

Caso não tenha o pip instalado, instruções para Linux, MacOS e Windows estão disponíveis neste [link](https://pip.pypa.io/en/stable/installation/).

Para instalar o Gym, basta rodar o seguinte comando:

     pip install gym

### Compile from source

Caso queira modifricar alguma funcionalidade da biblioteca ou adicionar seus próprios ambientes, e possivel compilar a biblioteca direto do código fonte:

    git clone https://github.com/openai/gym
    cd gym
    pip install -e .[all]

## Ambientes

O principal atrativo do Gym é a vasta gama de ambientes prontos para usar. Mas afinal, o que é um *ambiente*? O *ambiente* é o espaço que representa o nosso problema: o mundo com o qual nosso agente pode interagir e, com base nos estímulos vindos do ambiente, o agente deve realizar a tomada de decisões.. Um exemplo seria uma partida de xadrez, onde o ambiente serio o conjunto de peças no tabuleiro.

Pronto, agora você já sabe o que é um ambiente, ams como eu crio um usando o Gym?

Os ambientes do Gym possuem uma série de métodos simples que usamos para manipular e analisar eles, os principais para essa etapa do tutorial são esses:
<center>
<br>

| Método               | Funcionalidade                                          |
| :------------------- |:------------------------------------------------------- |
| `make()` | Cria o ambiente |
| `reset()`              | Inicializa o ambiente e recebe a observação inicial     |
| `step(action)`         | Executa uma ação e recebe a observação e a recompensa   |
| `render()`             | Renderiza o ambiente                                    |
| `close()`              | Fecha o ambiente                                        |

<br>
</center>

## Observações

Porém, como você deve ter notado, mexer aleatóriamente pra esquerda e pra direita não é bem um **aprendizado**, então é de se esperar que eventualmente seria interessante ensinar alguma coisa pro agente, porém como fazer isso?

Primeiro, vale explicar o retorno da função `env.step()`, na verdade, ela retorna quatro valores que possibilitam implementar algoritmos de aprendizado por reforço, estes sendo:
<center>

|Nome|Tipo|Descrição|
|-|-|-|
|`observation`|objeto|Um objeto especifico por ambiente que representa a observação do ambiente.|
|`reward`|float|Quantidade de recompensa alcançada pela última ação. A escala varia com o ambiente|
|`done`|boolean|Flag que indica se é hora de chamar o `reset()`. Indica que o episódio terminou.|
|`info`|dict|Informações diagnósticas úteis para debugar. Geralmente é bom pra estudar,<br> mas o seu agente não usa isso pra aprender|

</center>

Perceba que trata-se de uma implementação do ciclo de agente-ambiente, onde a cada timestep o agente scolhe uma açãõ e o ambiente retorna uma observação e uma recompensa.

<center><img src="https://gym.openai.com/assets/docs/aeloop-138c89d44114492fd02822303e6b4b07213010bb14ca5856d2d49d6b62d88e53.svg" width="300"/></center>

## Espaços

No gym, todo ambiente vem com um `action_space` e um `observation_space`. Esses atributos tem o tipo `Space` e descrevem o formato das açõesk.

## Conclusão

Essencialmente, este é o Gym e um de seus ambientes. Se além de aprender a utilizar a biblioteca e criar um ambiente, você também tem interesse em entender como utilizar um algoritmo de aprendizado por reforço, dê uma olhada no nosso tutorial de **[Stable Baselines]([https://github.com/DLR-RM/stable-baselines3](https://github.com/turing-usp/Aprendizado-por-Reforco/tree/main/Bibliotecas/Stable%20Baselines))**. 

Aproveite e dê uma olhada nos [outros ambientes disponíveis na biblioteca]([https://gym.openai.com/envs/#classic_control]), eles não se limitam apenas nesses exemplos simples, a openAI disponibiliza desde emuladores de jogos de atari até modelos de ambientes tridimensionais.
