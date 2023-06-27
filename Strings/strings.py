nome = "Matheus"
nome2 = "Vieira"
nome_completo = nome + " " + nome2

#Verificando o tipo da variável. Resultado = 'str'
print(type(nome))


#O comparador IS é utilizado para verificar o endereço de memória. Resultado = "Diferentes"
if nome is nome2:
    print("Iguais")
else:
    print("Diferentes")

#Compara se o conteúdo das Strings são o mesmo. Resultado = "Diferentes"
if nome == nome2:
    print("Iguais")
else:
    print("Diferentes")

#Concatenar String. Resultado = "Matheus Vieira"
print(nome + ' ' + nome2)

#Verificar tamanho da String. Resultado = 7
print(len(nome))

#Metódo substring no Python. Resultado = "Mat"
print(nome[0:3])
#De trás para frente. Resultado = "u"
print(nome[-2])

#Procurar uma substring dentro de uma string. Resultado = 8
#Caso não seja encontrada o resultado será -1

print(nome_completo.find("Vieira"))

#Substituir substrings na string. Resultado = "Matheus Vicente"
novo_nome = nome_completo.replace("Vieira", "Vicente")
print(novo_nome)

#Com o método split() desmembramos uma string em múltiplas
# strings através de um separador passado no parâmetro, retornando todas numa lista.

mensagem = 'Estou aprendendo Python na DevMedia'
nova_mensagem = mensagem.split(' ')
print(type(nova_mensagem))
print(nova_mensagem)

#Upper e Lower

print(nome_completo.upper())
print(nome_completo.lower())



