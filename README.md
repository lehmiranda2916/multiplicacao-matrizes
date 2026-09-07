# Multiplicação de Matrizes em Python

Aplicativo desenvolvido em Python para a disciplina de Lógica de Programação.

## Objetivo

O programa permite informar duas matrizes, quadradas ou não, e realizar a multiplicação entre elas quando suas dimensões forem compatíveis.

## Tecnologias utilizadas

- Python
- Tkinter
- PyInstaller
- Visual Studio Code

## Como funciona

O usuário informa:

- Quantidade de linhas da Matriz A
- Quantidade de colunas da Matriz A
- Quantidade de linhas da Matriz B
- Quantidade de colunas da Matriz B

O programa cria automaticamente os campos necessários para preencher as matrizes.

Antes da multiplicação, o programa verifica se:

**Número de colunas da Matriz A = Número de linhas da Matriz B**

Caso essa condição não seja atendida, o programa informa que a multiplicação não é possível.

## Exemplo da atividade

Matriz A:

    -3   2   5
     4  -8   1
     7   3   6

Matriz B:

    -2
     3
     1

Resultado:

     17
    -31
      1

## Interface gráfica

A interface gráfica foi desenvolvida utilizando a biblioteca Tkinter do Python.

O programa possui campos para definição das dimensões das matrizes, campos para entrada dos valores, botão para realizar a multiplicação e área para exibição do resultado.

## Executável

Além do código em Python, o programa também foi transformado em um aplicativo executável para Windows utilizando o PyInstaller.

O executável foi gerado com:

    python -m PyInstaller --onefile --windowed --name MultiplicacaoMatrizes main.py

## Autor

Projeto desenvolvido para atividade acadêmica de Lógica de Programação.
