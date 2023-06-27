# Os dicionários representam coleções de dados que contém na sua estrutura
# um conjunto de pares chave/valor, nos quais cada chave individual tem um valor associado.
# Esse objeto representa a ideia de um mapa, que entendemos como uma coleção associativa
# desordenada. A associação nos dicionários é feita por meio de uma chave que faz referência
# a um valor.

dados_cliente = {
    'Nome': 'Renan',
    'Endereco': 'Rua Cruzeiro do Sul',
    'Telefone': '982503645'
}

print(dados_cliente['Nome']) # Renan

# Adicionando elementos a um dicionário

dados_cliente['Idade'] = 45
print(dados_cliente['Idade'])

# Remover um item do dicionário

# O None serve para que a mensagem de erro KeyError não apareça devido a
# remoção de uma chave inexistente.

dados_cliente.pop('Telefone', None)
print(dados_cliente)

# Removendo usando del, que remove chave e valor associado a ele no dicionário

del dados_cliente['Idade']
print(dados_cliente)