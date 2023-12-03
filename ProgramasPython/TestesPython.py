import tkinter as tk
from tkinter import filedialog

# Função para abrir o diálogo de seleção de arquivo
def selecionar_arquivo():
    root = tk.Tk()
    root.withdraw()
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])
    return arquivo

# Solicitar ao usuário o nome do arquivo
arquivo_selecionado = selecionar_arquivo()

# Exibir o nome do arquivo selecionado
print("Arquivo selecionado:", arquivo_selecionado)
