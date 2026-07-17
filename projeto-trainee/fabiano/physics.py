import numpy as np
import pandas as pd

def calcular_aceleracao(theta_rad, mu_s, mu_k, v, g=9.81):
    """
    Calcula a aceleração de um bloco em um plano inclinado.
    """
    sin_theta = np.sin(theta_rad)
    cos_theta = np.cos(theta_rad)
    
    # Componentes da gravidade (divididas pela massa para obter a aceleração)
    g_x = g * sin_theta
    g_y = g * cos_theta
    
    # Acelerações relacionadas ao atrito
    a_s_max = mu_s * g_y  # Atrito estático máximo
    a_k = mu_k * g_y      # Atrito cinético
    
    # Tomada de decisão física com base na velocidade
    if v == 0.0:
        # Se a força da gravidade vencer o atrito estático, o bloco entra em movimento
        if g_x > a_s_max:
            return g_x - a_k
        else:
            return 0.0
    elif v > 0.0:
        # Bloco em movimento rampa abaixo
        return g_x - a_k
    else:
        return 0.0

def simular_movimento_rampa(massa, theta_graus, mu_s, mu_k, comprimento, dt=0.01, g=9.81):
    """
    Executa a evolução temporal da posição e velocidade utilizando o método numérico.
    """
    theta_rad = np.deg2rad(theta_graus)
    
    # Condições iniciais
    t = 0.0
    x = 0.0
    v = 0.0
    
    tempos = [t]
    posicoes = [x]
    velocidades = [v]
    aceleracoes = [calcular_aceleracao(theta_rad, mu_s, mu_k, v, g)]
    
    # O laço para assim que o bloco atingir o final da rampa
    while x < comprimento:
        a = calcular_aceleracao(theta_rad, mu_s, mu_k, v, g)
        
        # Se a aceleração e a velocidade forem nulas, o bloco permanece parado
        if a == 0.0 and v == 0.0:
            tempos.append(t + dt)
            posicoes.append(x)
            velocidades.append(0.0)
            aceleracoes.append(0.0)
            break
            
        # Atualização pelo método de Euler-Cromer
        v = v + a * dt
        x = x + v * dt
        t = t + dt
        
        tempos.append(t)
        posicoes.append(x)
        velocidades.append(v)
        aceleracoes.append(a)
        
    # Organizando os resultados com Pandas
    dados = pd.DataFrame({
        "tempo (s)": tempos,
        "posicao (m)": posicoes,
        "velocidade (m/s)": velocidades,
        "aceleracao (m/s^2)": aceleracoes
    })
    
    return dados