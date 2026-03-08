import tkinter as tk


# =========================
# FUNÇÕES DA CALCULADORA

def clicar(valor):
    """Adiciona número ou operador no visor"""
    visor.insert(tk.END, valor)


def limpar():
    """Limpa o visor"""
    visor.delete(0, tk.END)


def calcular():
    """Calcula a expressão digitada"""
    try:
        resultado = eval(visor.get())
        visor.delete(0, tk.END)
        visor.insert(0, str(resultado))
    except:
        visor.delete(0, tk.END)
        visor.insert(0, "Erro")


# =========================
# CONFIGURAÇÃO DA JANELA

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x420")
janela.configure(bg="black")
janela.resizable(False, False)


# =========================
# VISOR DA CALCULADORA

visor = tk.Entry(
    janela,
    font=("Helvetica", 28),
    bg="black",
    fg="white",
    borderwidth=0,
    justify="right"
)

visor.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,
    pady=20,
    sticky="nsew"
)


# =========================
# CORES UTILIZADAS

cinza = "#333333"
cinza_claro = "#a5a5a5"
azul = "#007AFF"   # cor das operações


# =========================
# FUNÇÃO PARA CRIAR BOTÕES

def criar_botao(texto, linha, coluna, cor_bg, cor_fg="white", comando=None, colspan=1):
    """Cria um botão da calculadora"""

    botao = tk.Button(
        janela,
        text=texto,
        bg=cor_bg,
        fg=cor_fg,
        font=("Helvetica", 16),
        width=5,
        height=2,
        borderwidth=0,
        command=comando
    )

    botao.grid(
        row=linha,
        column=coluna,
        columnspan=colspan,
        padx=5,
        pady=5,
        sticky="nsew"
    )


# =========================
# BOTÕES DA CALCULADORA

# Primeira linha
criar_botao("AC", 1, 0, cinza_claro, "black", limpar)
criar_botao("+/-", 1, 1, cinza_claro, "black", lambda: clicar("-"))
criar_botao("%", 1, 2, cinza_claro, "black", lambda: clicar("%"))
criar_botao("÷", 1, 3, azul, comando=lambda: clicar("/"))

# Segunda linha
criar_botao("7", 2, 0, cinza, comando=lambda: clicar("7"))
criar_botao("8", 2, 1, cinza, comando=lambda: clicar("8"))
criar_botao("9", 2, 2, cinza, comando=lambda: clicar("9"))
criar_botao("×", 2, 3, azul, comando=lambda: clicar("*"))

# Terceira linha
criar_botao("4", 3, 0, cinza, comando=lambda: clicar("4"))
criar_botao("5", 3, 1, cinza, comando=lambda: clicar("5"))
criar_botao("6", 3, 2, cinza, comando=lambda: clicar("6"))
criar_botao("-", 3, 3, azul, comando=lambda: clicar("-"))

# Quarta linha
criar_botao("1", 4, 0, cinza, comando=lambda: clicar("1"))
criar_botao("2", 4, 1, cinza, comando=lambda: clicar("2"))
criar_botao("3", 4, 2, cinza, comando=lambda: clicar("3"))
criar_botao("+", 4, 3, azul, comando=lambda: clicar("+"))

# Quinta linha
criar_botao("0", 5, 0, cinza, comando=lambda: clicar("0"), colspan=2)
criar_botao(".", 5, 2, cinza, comando=lambda: clicar("."))
criar_botao("=", 5, 3, azul, comando=calcular)


# =========================
# AJUSTE DO GRID

for i in range(6):
    janela.grid_rowconfigure(i, weight=1)

for i in range(4):
    janela.grid_columnconfigure(i, weight=1)


# =========================
# INICIAR A CALCULADORA

janela.mainloop()