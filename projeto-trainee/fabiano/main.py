from physics import simular_movimento_rampa
from plots import plotar_comparacao
from animation import animar_bloco
#Para compilar e executar o código use o Anaconda Prompt, e digite os seguintes comandos:
#cd "C:\Users\Fabiano\OneDrive\Documentos\treiner nexus\plano-inclinado\projeto-trainee\fabiano"
#python main.py

def main():
    # Parâmetros base do sistema
    massa = 2.0         # kg
    comprimento = 10.0  # m
    g = 9.81            # m/s^2

    print("Iniciando Simulações Numéricas...\n")

    # ---------------------------------------------------------
    # COMPARAÇÃO 1: Com Atrito vs Sem Atrito (Mesmo ângulo: 30°)
    # ---------------------------------------------------------
    theta_1 = 30.0
    
    # Simulação sem atrito
    df_sem_atrito = simular_movimento_rampa(
        massa, theta_1, mu_s=0.0, mu_k=0.0, comprimento=comprimento, g=g
    )
    
    # Simulação com atrito
    df_com_atrito = simular_movimento_rampa(
        massa, theta_1, mu_s=0.4, mu_k=0.3, comprimento=comprimento, g=g
    )

    plotar_comparacao(
        [df_sem_atrito, df_com_atrito],
        ["Sem Atrito", r"Com Atrito ($\mu_k=0.3$)"],
        titulo_sufixo=f"Comparação de Atrito ({theta_1}°)"
    )

    # ---------------------------------------------------------
    # COMPARAÇÃO 2: Diferentes Ângulos (Com mesmo atrito)
    # ---------------------------------------------------------
    theta_2 = 20.0
    theta_3 = 45.0
    
    df_ang_20 = simular_movimento_rampa(
        massa, theta_2, mu_s=0.4, mu_k=0.3, comprimento=comprimento, g=g
    )
    df_ang_45 = simular_movimento_rampa(
        massa, theta_3, mu_s=0.4, mu_k=0.3, comprimento=comprimento, g=g
    )

    plotar_comparacao(
        [df_ang_20, df_com_atrito, df_ang_45],
        [f"{theta_2}°", f"{theta_1}°", f"{theta_3}°"],
        titulo_sufixo=r"Comparação de Ângulos ($\mu_k=0.3$)"
    )

    # ---------------------------------------------------------
    # SIMULAÇÃO VISUAL ANIMADA
    # ---------------------------------------------------------
    print("Gerando animação visual...")
    # Executa a animação para o bloco a 30° com atrito
    animar_bloco(df_com_atrito, theta_1, comprimento)

if __name__ == "__main__":
    main()