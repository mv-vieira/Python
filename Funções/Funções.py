#A sintaxe de uma função é definida por três partes: nome, parâmetros e corpo,
# o qual agrupa uma sequência de linhas que representa algum comportamento.
# No código abaixo, temos um exemplo de declaração de função em Python:


#Função para imprimir um nome
def olá(meu_nome: str) -> str:
    return print(f"Olá {meu_nome}")

olá("Matheus")

#Função para calcular um salário implementando uma lógica

def calcular_pagamento(quantidade_horas, valor_hora):
    horas = float(quantidade_horas)
    taxa = float(valor_hora)

    if horas <= 40:
        salario = horas * taxa

    else:
        horas_excedentes = horas - 40
        salario = 40 * taxa + (horas_excedentes * (1.5 * taxa))

    return salario


hora = input("Digite quantidade de horas trabalhadas: ")
valor_hora = input("Digite o valor de cada hora trabalhada: ")

total_recebido = calcular_pagamento(hora,valor_hora)

print("O total dos seus rendimentos é de R$:" ,total_recebido)


# Função para calcular IMC

def calcular_imc(peso, altura):
    print(peso / altura ** 2)

calcular_imc(130, 1.77)

# importando um funções de um módulo

import math

exponencial = math.exp(5)
print(exponencial)



