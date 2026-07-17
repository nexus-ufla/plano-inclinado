# Processo Seletivo Nexus - Projeto Trainee
**Simulação Computacional de um Bloco em um Plano Inclinado**

## Objetivo
Este projeto tem como finalidade aplicar conceitos fundamentais de modelagem física e simulação computacional em Python, resolvendo a evolução temporal da cinemática e da dinâmica de um corpo sobre um plano inclinado.

## Estrutura do Repositório
* `physics.py`: Equacionamento físico (gravidade, plano, coeficientes $\mu_s$ e $\mu_k$) e atualização da simulação por pequenos passos de tempo (Euler-Cromer).
* `plots.py`: Geração de gráficos utilizando a biblioteca `matplotlib`, para analisar $x(t)$ e $v(t)$.
* `animation.py`: Script para uma visualização animada e em duas dimensões da descida do bloco.
* `main.py`: Script principal que orquestra as comparações requeridas de cenários e os exibe.
* `requirements.txt`: Relação de bibliotecas numéricas exigidas (como `numpy` e `pandas`).

## Como Executar
1. Certifique-se de que possui as bibliotecas requeridas instaladas:
   `pip install -r requirements.txt`
2. Execute o arquivo principal via terminal:
   `python main.py`

## Conclusões Esperadas
Através deste módulo, é possível observar claramente que o ângulo da rampa e a presença/intensidade do atrito interferem de modo direto e inversamente proporcional na taxa de aceleração ($a = g \sin(\theta) - \mu_k g \cos(\theta)$), refletindo exponencialmente sobre a curva de posição e de velocidade exibidas nos gráficos.