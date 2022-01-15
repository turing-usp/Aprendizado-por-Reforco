# OpenAI Gym

Guia de como utilizar a biblioteca e ambientes Gym para projetos de aprendizado por reforço.

Para acessar o guia completo com exemplos de código veja este notebook:

### [Notebook com o guia completo](./Gym.ipynb)

## Índice

- [OpenAI Gym](#openai-gym)
    - [Notebook com o guia completo](#notebook-com-o-guia-completo)
  - [Índice](#índice)
  - [O que é o Gym?](#o-que-é-o-gym)
  - [Como usar o Gym](#como-usar-o-gym)
  - [Instalação](#instalação)
    - [Pip (Para Python 3.5+)](#pip-para-python-35)
  - [Ambientes](#ambientes)
  - [Observações](#observações)
  - [Espaços](#espaços)
  - [Conclusão](#conclusão)

## O que é o Gym?

O Gym é um conjunto de ferramentas que ajudam no desenvolvimento e na comparação de algoritmos de aprendizado por reforço. A biblioteca é basicamente um conjunto de environments, ou ambientes de teste que o usuário pode utilizar pra testar seus algoritmos. Vale notar que esses ambientes têm uma interface compartilhada, desta forma torna-se possível escrever algoritmos gerais.

## Como usar o Gym

Com o Gym, é possível testar e comparar algoritmos de aprendizado por reforço através dos diversos environments oferecidos pela biblioteca e as ferramentas de metrificação por ela implementadas, que possibilitam analisar o desempenho dos algoritmos utilizados.

## Instalação

A instalação do Gym pode ser realizada de duas formas diferentes:

### Pip (Para Python 3.5+)

Caso não tenha o pip instalado, instruções para Linux, MacOS e Windows estão disponíveis neste [link](https://pip.pypa.io/en/stable/installation/).

Para instalar o Gym, basta rodar o seguinte comando:

     pip install gym

## Ambientes

O principal atrativo do Gym são os diversos ambientes oferecidos prontos para usar. Mas afinal, o que é um **ambiente**? O **ambiente** é o espaço que representa o nosso problema: o mundo com o qual o agente pode interagir, e no qual ele deve se basear para a tomada de decisões. Um exemplo seria numa partida de xadrez, em que o ambiente seria o conjunto de peças no tabuleiro.

Pronto, agora você já sabe o que é um ambiente, mas como eu crio um usando o gym?

Os ambientes do Gym possuem uma série de métodos simples que usamos para manipular e analisar eles. Os principais para essa etapa do tutorial são esses:
| Método               | Funcionalidade                                          |
| :------------------- |:------------------------------------------------------- |
| `make()` | Cria o ambiente |
| `reset()`              | Inicializa o ambiente e recebe a observação inicial     |
| `step(action)`         | Executa uma ação e recebe a observação e a recompensa   |
| `render()`             | Renderiza o ambiente                                    |
| `close()`              | Fecha o ambiente                                        |

## Observações

Porém, como você deve ter notado, mexer aleatoriamente pra esquerda e pra direita não é bem um **aprendizado**, então é de se esperar que eventualmente seria interessante ensinar alguma coisa pro agente, porém como fazer isso?

Primeiro, vale explicar o retorno da função `env.step()`, na verdade, ela retorna quatro valores que possibilitam implementar algoritmos de aprendizado por reforço, estes sendo:

|Nome|Tipo|Descrição|
|-|-|-|
|`observation`|objeto|Um objeto especifico por ambiente que representa a observação do ambiente.|
|`reward`|float|Quantidade de recompensa alcançada pela última ação. A escala varia com o ambiente|
|`done`|boolean|Flag que indica se é hora de chamar o `reset()`. Indica que o episódio terminou.|
|`info`|dict|Informações diagnósticas úteis para debugar. Geralmente é bom pra estudar,<br> mas o seu agente não usa isso pra aprender|


Perceba que trata-se de uma implementação do ciclo de agente-ambiente, onde a cada timestep o agente escolhe uma ação e o ambiente retorna uma observação e uma recompensa.

<img src="https://gym.openai.com/assets/docs/aeloop-138c89d44114492fd02822303e6b4b07213010bb14ca5856d2d49d6b62d88e53.svg" width="300"/>

## Espaços

No gym, todo ambiente vem com um `action_space` e um `observation_space`. Esses atributos têm o tipo `Space` e descrevem o formato das ações.

## Conclusão

Essencialmente, este é o Gym e um de seus ambientes. Se além de aprender a utilizar a biblioteca e criar um ambiente, você também tem interesse em entender como utilizar um algoritmo de aprendizado por reforço, dê uma olhada no nosso tutorial de  **[Stable Baselines](/Bibliotecas/Stable%20Baselines)**. 

Aproveite e dê uma olhada nos [outros ambientes disponíveis na biblioteca]([https://gym.openai.com/envs/#classic_control]). Eles não se limitam apenas nesses exemplos simples, a openAI disponibiliza desde emuladores de jogos de atari até modelos de ambientes tridimensionais.
