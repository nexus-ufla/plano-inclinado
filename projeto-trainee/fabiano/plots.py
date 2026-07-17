import matplotlib.pyplot as plt

def plotar_comparacao(lista_dfs, labels, titulo_sufixo=""):
    """
    Gera gráficos científicos comparando a posição e a velocidade em função do tempo.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    for df, label in zip(lista_dfs, labels):
        ax1.plot(df['tempo (s)'], df['posicao (m)'], label=label)
        ax2.plot(df['tempo (s)'], df['velocidade (m/s)'], label=label)
        
    # Configurações do gráfico de posição
    ax1.set_xlabel("Tempo (s)")
    ax1.set_ylabel("Posição (m)")
    ax1.set_title(f"Posição x Tempo\n{titulo_sufixo}")
    ax1.grid(True)
    ax1.legend()
    
    # Configurações do gráfico de velocidade
    ax2.set_xlabel("Tempo (s)")
    ax2.set_ylabel("Velocidade (m/s)")
    ax2.set_title(f"Velocidade x Tempo\n{titulo_sufixo}")
    ax2.grid(True)
    ax2.legend()
    
    plt.tight_layout()
    plt.show()