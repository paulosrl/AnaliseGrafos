import tkinter as tk
from tkinter import filedialog
import pandas as pd

def selecionar_arquivo():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    caminho_arquivo = filedialog.askopenfilename()
    return caminho_arquivo

def exibir_mensagem(mensagem):
    janela = tk.Tk()
    janela.title("Mensagem")
    tk.Label(janela, text=mensagem).pack()
    tk.Button(janela, text="OK", command=janela.destroy).pack()
    janela.mainloop()

# Exibir a mensagem
exibir_mensagem("Esta é a sua mensagem")

# Solicitar o local do arquivo
caminho_arquivo = selecionar_arquivo()

# Ler o conteúdo do arquivo em um DataFrame
df = pd.read_csv(caminho_arquivo)

print(df.head())
