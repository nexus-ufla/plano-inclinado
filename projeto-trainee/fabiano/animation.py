import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animar_bloco(df, theta_graus, comprimento):
    """
    Desenvolve uma visualização simples do movimento do bloco descendo a rampa.
    """
    theta_rad = np.deg2rad(theta_graus)
    posicoes = df['posicao (m)'].values
    tempos = df['tempo (s)'].values
    
    fig, ax = plt.subplots(figsize=(8, 4))
    
    # Base trigonométrica para desenhar a rampa
    x_max = comprimento * np.cos(theta_rad)
    y_max = comprimento * np.sin(theta_rad)
    
    # Linhas desenhando o plano
    ax.plot([0, x_max, x_max, 0], [y_max, 0, 0, y_max], color='black', lw=2)
    ax.set_aspect('equal')
    ax.set_xlim(-0.5, x_max + 1)
    ax.set_ylim(-0.5, y_max + 1)
    ax.axis('off')
    
    # Representação do bloco
    bloco, = ax.plot([], [], 's', markersize=15, color='blue')
    texto_tempo = ax.text(0.05, 0.9, '', transform=ax.transAxes, fontsize=12)
    
    def init():
        bloco.set_data([], [])
        texto_tempo.set_text('')
        return bloco, texto_tempo

    def update(frame):
        # Deslocamento hipotenusal
        d = posicoes[frame]
        
        # O bloco desce a partir da altura máxima
        x_pos = d * np.cos(theta_rad)
        y_pos = y_max - d * np.sin(theta_rad)
        
        bloco.set_data([x_pos], [y_pos])
        texto_tempo.set_text(f'Tempo: {tempos[frame]:.2f} s')
        return bloco, texto_tempo

    # Otimização para não sobrecarregar a memória
    step = max(1, len(posicoes) // 150)
    frames = range(0, len(posicoes), step)
    
    ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=False, interval=30)
    plt.title(f"Simulação Visual - Rampa de {theta_graus}°")
    plt.show()