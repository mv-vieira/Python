# min() e max() que retornam o menor e o maior da lista.

numeros = [5,6,15,9,10]
nomes = ['Matheus', 'Mikaela', 'Isabela', 'Scarlett']

print(min(numeros))
print(max(numeros))
print(min(nomes))
print(max(nomes))

# sum(), retorna a soma de todos os itens da coleção. Não funciona com string
print(sum(numeros))

# len(), retorna o tamanho do objeto.
# Quando usada com coleções, retorna o total de itens que a coleção possui.

print(len(nomes))
print(len(numeros))

# type() podemos obter o tipo do objeto passado no parâmetro

professores = ['Carla', 'Daniel', 'Ingrid', 'Roberto']
estacoes = ('Primavera', 'Verão', 'Outono', 'Inverno')
cliente = {
    'Nome': 'Fábio Garcia',
    'email' : 'fabio_garcia_9@outlook.com'
}

print(type(professores)) # list
print(type(estacoes)) # tuple
print(type(cliente)) # dict
