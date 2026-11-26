import tkinter as tk
from tkinter import font

def exibir_mensagem(mensagem):
    def fechar_mensagem():
        rotulo.pack_forget()  # Remove o rótulo
        print("Este código continua após 3 segundos.")

    # Cria uma janela
    janela = tk.Tk()
    janela.title("Automação FGV")

    # Define o tamanho da janela
    largura_janela = 400
    altura_janela = 200
    janela.geometry(f"{largura_janela}x{altura_janela}")

    # Centraliza a janela na tela
    tela_largura = janela.winfo_screenwidth()
    tela_altura = janela.winfo_screenheight()
    x = (tela_largura // 2) - (largura_janela // 2)
    y = (tela_altura // 2) - (altura_janela // 2)
    janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

    # Define uma fonte maior
    tipo_fonte = font.Font(family="Helvetica", size=16, weight="bold")
    
    frame = tk.Frame(janela)
    frame.place(relx=0.5, rely=0.5, anchor='center')  # Centraliza o Frame

    # Cria um rótulo com a mensagem e aplica a fonte
    rotulo = tk.Label(frame, text=mensagem, font=tipo_fonte)
    
    rotulo.pack(expand=True)
    #rotulo.pack(pady=50)  # Adiciona um espaço vertical ao redor do rótulo

    # Agendar a chamada da função para fechar a mensagem após 3000 ms (3 segundos)
    #janela.after(13000, fechar_mensagem)

    # Inicia o loop da interface gráfica
    janela.mainloop()

# Chama a função com a mensagem desejada
# exibir_mensagem("Inicio da automação!")
# exibir_mensagem("Preenchendo o formulário!")
# exibir_mensagem("Coletando dados!")
# exibir_mensagem("Gerando planilha!")
# exibir_mensagem("Enviando e-mail!")
# exibir_mensagem("Fim da automação!")