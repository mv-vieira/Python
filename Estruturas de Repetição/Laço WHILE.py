# O comando while, por sua vez, faz com que um conjunto de instruções seja executado
# enquanto uma condição for atendida. Quando o resultado passa a ser falso, a execução
# é interrompida, saindo do loop, e passa para o próximo bloco.

contador = 0
while contador < 5:
    print(contador)
    contador = contador +1

print("\n")

# Imprimindo a tabuada de 5
cont = 0
while cont <=10:
    print(f"5 * {cont} = {cont * 5}")
    cont += 1
else:
    print("Tabuada de 5 calculada com sucesso!")

print("\n")

# Se dentro da repetição for executado um break,
# o loop será encerrado sem executar o conjunto da cláusula else.

x = 0
while x < 10:
    print(x)
    x += 1
    if x == 6:
        print("x é igual a 6")
        break
else:
    print("fim while")