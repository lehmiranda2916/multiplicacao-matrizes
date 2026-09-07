import tkinter as tk
from tkinter import messagebox


# Listas que vão guardar os campos das matrizes
campos_a = []
campos_b = []


def criar_matrizes():
    global campos_a, campos_b

    # Limpa os campos antigos
    for item in frame_matriz_a.winfo_children():
        item.destroy()

    for item in frame_matriz_b.winfo_children():
        item.destroy()

    resultado.config(text="")

    try:
        linhas_a = int(entrada_linhas_a.get())
        colunas_a = int(entrada_colunas_a.get())

        linhas_b = int(entrada_linhas_b.get())
        colunas_b = int(entrada_colunas_b.get())

        if linhas_a <= 0 or colunas_a <= 0 or linhas_b <= 0 or colunas_b <= 0:
            messagebox.showerror("Erro", "As dimensões devem ser maiores que zero.")
            return

        # Verifica se a multiplicação é possível
        if colunas_a != linhas_b:
            messagebox.showerror(
                "Multiplicação impossível",
                "O número de colunas da Matriz A deve ser igual "
                "ao número de linhas da Matriz B."
            )
            return

        campos_a = []
        campos_b = []

        # Cria os campos da Matriz A
        for i in range(linhas_a):
            linha = []

            for j in range(colunas_a):
                campo = tk.Entry(
                    frame_matriz_a,
                    width=6,
                    justify="center"
                )

                campo.grid(row=i, column=j, padx=3, pady=3)
                linha.append(campo)

            campos_a.append(linha)

        # Cria os campos da Matriz B
        for i in range(linhas_b):
            linha = []

            for j in range(colunas_b):
                campo = tk.Entry(
                    frame_matriz_b,
                    width=6,
                    justify="center"
                )

                campo.grid(row=i, column=j, padx=3, pady=3)
                linha.append(campo)

            campos_b.append(linha)

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite números inteiros nas dimensões das matrizes."
        )


def multiplicar():
    if not campos_a or not campos_b:
        messagebox.showwarning(
            "Atenção",
            "Primeiro crie as matrizes."
        )
        return

    try:
        matriz_a = []
        matriz_b = []

        # Lê os valores da Matriz A
        for linha in campos_a:
            valores = []

            for campo in linha:
                valores.append(float(campo.get()))

            matriz_a.append(valores)

        # Lê os valores da Matriz B
        for linha in campos_b:
            valores = []

            for campo in linha:
                valores.append(float(campo.get()))

            matriz_b.append(valores)

        linhas_a = len(matriz_a)
        colunas_a = len(matriz_a[0])
        colunas_b = len(matriz_b[0])

        matriz_resultado = []

        # Multiplicação das matrizes
        for i in range(linhas_a):
            linha_resultado = []

            for j in range(colunas_b):
                soma = 0

                for k in range(colunas_a):
                    soma += matriz_a[i][k] * matriz_b[k][j]

                linha_resultado.append(soma)

            matriz_resultado.append(linha_resultado)

        # Monta o texto do resultado
        texto = ""

        for linha in matriz_resultado:
            for valor in linha:

                if valor.is_integer():
                    texto += f"{int(valor):8}"
                else:
                    texto += f"{valor:8.2f}"

            texto += "\n"

        resultado.config(text=texto)

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Preencha todos os campos das matrizes apenas com números."
        )


# -------------------------
# CORES
# -------------------------

cor_fundo = "#1E1E2E"
cor_texto = "#FFFFFF"
cor_botao = "#4CAF50"


# -------------------------
# JANELA
# -------------------------

janela = tk.Tk()

janela.title("Multiplicação de Matrizes")
janela.geometry("750x650")
janela.configure(bg=cor_fundo)


# -------------------------
# CONTEÚDO PRINCIPAL
# -------------------------

principal = tk.Frame(janela, bg=cor_fundo)
principal.pack(pady=25)


tk.Label(
    principal,
    text="MULTIPLICAÇÃO DE MATRIZES",
    font=("Arial", 20, "bold"),
    bg=cor_fundo,
    fg=cor_texto
).pack(pady=15)


# -------------------------
# DIMENSÕES
# -------------------------

dimensoes = tk.Frame(principal, bg=cor_fundo)
dimensoes.pack(pady=10)


# Matriz A

frame_dim_a = tk.Frame(dimensoes, bg=cor_fundo)
frame_dim_a.grid(row=0, column=0, padx=30)

tk.Label(
    frame_dim_a,
    text="Matriz A",
    font=("Arial", 14, "bold"),
    bg=cor_fundo,
    fg=cor_texto
).grid(row=0, column=0, columnspan=2, pady=5)

tk.Label(
    frame_dim_a,
    text="Linhas:",
    bg=cor_fundo,
    fg=cor_texto
).grid(row=1, column=0)

entrada_linhas_a = tk.Entry(frame_dim_a, width=5, justify="center")
entrada_linhas_a.grid(row=1, column=1)

tk.Label(
    frame_dim_a,
    text="Colunas:",
    bg=cor_fundo,
    fg=cor_texto
).grid(row=2, column=0)

entrada_colunas_a = tk.Entry(frame_dim_a, width=5, justify="center")
entrada_colunas_a.grid(row=2, column=1)


# Matriz B

frame_dim_b = tk.Frame(dimensoes, bg=cor_fundo)
frame_dim_b.grid(row=0, column=1, padx=30)

tk.Label(
    frame_dim_b,
    text="Matriz B",
    font=("Arial", 14, "bold"),
    bg=cor_fundo,
    fg=cor_texto
).grid(row=0, column=0, columnspan=2, pady=5)

tk.Label(
    frame_dim_b,
    text="Linhas:",
    bg=cor_fundo,
    fg=cor_texto
).grid(row=1, column=0)

entrada_linhas_b = tk.Entry(frame_dim_b, width=5, justify="center")
entrada_linhas_b.grid(row=1, column=1)

tk.Label(
    frame_dim_b,
    text="Colunas:",
    bg=cor_fundo,
    fg=cor_texto
).grid(row=2, column=0)

entrada_colunas_b = tk.Entry(frame_dim_b, width=5, justify="center")
entrada_colunas_b.grid(row=2, column=1)


# -------------------------
# BOTÃO CRIAR
# -------------------------

tk.Button(
    principal,
    text="CRIAR MATRIZES",
    command=criar_matrizes,
    bg=cor_botao,
    fg="white",
    font=("Arial", 11, "bold"),
    cursor="hand2"
).pack(pady=15)


# -------------------------
# ÁREA DAS MATRIZES
# -------------------------

area_matrizes = tk.Frame(principal, bg=cor_fundo)
area_matrizes.pack(pady=10)


# Matriz A

container_a = tk.Frame(area_matrizes, bg=cor_fundo)
container_a.grid(row=0, column=0, padx=30)

tk.Label(
    container_a,
    text="Matriz A",
    font=("Arial", 13, "bold"),
    bg=cor_fundo,
    fg=cor_texto
).pack(pady=5)

frame_matriz_a = tk.Frame(container_a, bg=cor_fundo)
frame_matriz_a.pack()


# Matriz B

container_b = tk.Frame(area_matrizes, bg=cor_fundo)
container_b.grid(row=0, column=1, padx=30)

tk.Label(
    container_b,
    text="Matriz B",
    font=("Arial", 13, "bold"),
    bg=cor_fundo,
    fg=cor_texto
).pack(pady=5)

frame_matriz_b = tk.Frame(container_b, bg=cor_fundo)
frame_matriz_b.pack()


# -------------------------
# BOTÃO MULTIPLICAR
# -------------------------

tk.Button(
    principal,
    text="MULTIPLICAR",
    command=multiplicar,
    bg=cor_botao,
    fg="white",
    font=("Arial", 12, "bold"),
    width=15,
    height=2,
    cursor="hand2"
).pack(pady=20)


# -------------------------
# RESULTADO
# -------------------------

tk.Label(
    principal,
    text="Resultado:",
    font=("Arial", 14, "bold"),
    bg=cor_fundo,
    fg=cor_texto
).pack()


resultado = tk.Label(
    principal,
    text="",
    font=("Courier New", 16, "bold"),
    bg=cor_fundo,
    fg=cor_texto
)

resultado.pack(pady=10)


# -------------------------
# INICIAR PROGRAMA
# -------------------------

janela.mainloop()