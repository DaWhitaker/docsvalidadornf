import tkinter as tk
import webbrowser
import subprocess

# Função para abrir o site MkDocs localmente
def open_mkdocs():
    # Comando para compilar e servir o site MkDocs localmente
    command = "mkdocs serve"
    # Inicia o servidor MkDocs em um processo separado
    process = subprocess.Popen(command, shell=True)
    # Abre o navegador padrão para visualizar o site local
    webbrowser.open("http://localhost:8000")

# Cria a janela tkinter
root = tk.Tk()
root.title("Validação de Impostos")

# Adiciona um botão "Informação" para abrir o site MkDocs
info_button = tk.Button(root, text="Informação", command=open_mkdocs)
info_button.pack()

# Inicia o loop principal da interface gráfica
root.mainloop()
