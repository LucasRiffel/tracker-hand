import tkinter as tk
import random

def criar_tabuleiro(m, n, minas):
    tabuleiro = [['0' for _ in range(m)] for _ in range(n)]
    for _ in range(minas):
        x, y = random.randint(0, m - 1), random.randint(0, n - 1)
        tabuleiro[y][x] = 'X'
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if (0 <= nx < m and 0 <= ny < n and tabuleiro[ny][nx] != 'X'):
                    tabuleiro[ny][nx] = str(int(tabuleiro[ny][nx]) + 1)
    return tabuleiro

def revelar_celula(x, y, tabuleiro, revelado, botoes, fim):
    if fim or revelado[y][x]:
        return
    revelado[y][x] = True
    botoes[y][x].config(text=tabuleiro[y][x])
    if tabuleiro[y][x] == 'X':
        fim_de_jogo(tabuleiro, botoes, False)
    elif tabuleiro[y][x] == '0':
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if (0 <= nx < len(tabuleiro[0]) and 0 <= ny < len(tabuleiro)):
                    revelar_celula(nx, ny, tabuleiro, revelado, botoes)

def marcar_mina(x, y, tabuleiro, botoes, fim):
    if fim or botoes[y][x]['text'] == 'M':
        botoes[y][x].config(text=' ')
    else:
        botoes[y][x].config(text='M')

def fim_de_jogo(tabuleiro, botoes, vitoria):
    fim = True
    for y in range(len(tabuleiro)):
        for x in range(len(tabuleiro[y])):
            botoes[y][x].config(text=tabuleiro[y][x])
    if vitoria:
        print('Parabéns, você venceu!')
    else:
        print('Você revelou uma mina! Fim de jogo.')

def criar_interface(tabuleiro):
    janela = tk.Tk()
    fim = False
    revelado = [[False for _ in range(len(tabuleiro[0]))] for _ in range(len(tabuleiro))]
    botoes = [[None for _ in range(len(tabuleiro[0]))] for _ in range(len(tabuleiro))]
    for y in range(len(tabuleiro)):
        for x in range(len(tabuleiro[y])):
            botoes[y][x] = tk.Button(janela, text = ' ', command = lambda x=x, y=y: revelar_celula(x, y, tabuleiro, revelado, botoes, fim))
            botoes[y][x].bind('<Button-3>', lambda e, x=x, y=y: marcar_mina(x, y, tabuleiro, botoes, fim))
            botoes[y][x].grid(row = y, column = x)
    janela.mainloop()

def jogar():
    m, n, minas = 5, 5, 5
    tabuleiro = criar_tabuleiro(m, n, minas)
    criar_interface(tabuleiro)

jogar()