import random
import string
import tkinter as tk

def gerar_senha():
    tamanho = int(entry_tamanho.get())
    usar_maiusculas = var_maiusculas.get()
    usar_numeros = var_numeros.get()
    usar_especiais = var_especiais.get()
    
    caracteres = string.ascii_lowercase 

    if usar_maiusculas:
        caracteres += string.ascii_uppercase 

    if usar_numeros:
        caracteres += string.digits  

    if usar_especiais:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    entry_senha.delete(0, tk.END)
    entry_senha.insert(0, senha)

root = tk.Tk()
root.title("Gerador de Senhas")

label_tamanho = tk.Label(root, text="Tamanho da Senha:")
label_tamanho.pack(pady=5)
entry_tamanho = tk.Entry(root)
entry_tamanho.pack(pady=5)
entry_tamanho.insert(0, "12")

var_maiusculas = tk.BooleanVar()
check_maiusculas = tk.Checkbutton(root, text="Incluir Letras Maiúsculas", variable=var_maiusculas)
check_maiusculas.pack(pady=5)

var_numeros = tk.BooleanVar()
check_numeros = tk.Checkbutton(root, text="Incluir Números", variable=var_numeros)
check_numeros.pack(pady=5)

var_especiais = tk.BooleanVar()
check_especiais = tk.Checkbutton(root, text="Incluir Caracteres Especiais", variable=var_especiais)
check_especiais.pack(pady=5)

button_gerar = tk.Button(root, text="Gerar Senha", command=gerar_senha)
button_gerar.pack(pady=20)

entry_senha = tk.Entry(root, width=50)
entry_senha.pack(pady=5)

root.mainloop()
