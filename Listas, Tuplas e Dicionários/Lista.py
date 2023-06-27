#Lista é uma coleção de valores indexada, em que cada valor é identificado
# por um índice. O primeiro item na lista está no índice 0,
# o segundo no índice 1 e assim por diante.

programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']

print(type(programadores)) # type ‘list’
print(len(programadores)) # 5
print(programadores[4]) # Luana

#Alterando valores da lista
programadores[1] = "Matheus"
print(programadores)

#Adicionando novos valores na lista

programadores.append("Mikaela")
print(programadores)

programadores.insert(1,"Isabela") # Insere através do indice e valor.
print(programadores)

#Removendo valores da lista

programadores.remove("Victor")
print(programadores)

programadores.pop(5) # Remove baseado no indice
print(programadores)


#Criação de uma lista dinâmica com vários tipos de valores

aluno = ['Murilo', 19, 1.79] # Nome, idade e altura

print(type(aluno)) # type 'list'
print(aluno) # ['Murilo', 19, 1.79]

