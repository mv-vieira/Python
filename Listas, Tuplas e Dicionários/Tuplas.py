#Tupla é uma estrutura de dados semelhante a lista.
# Porém, ela tem a característica de ser imutável, ou seja, após uma tupla ser criada,
# ela não pode ser alterada.

times_rj = ('Botafogo', 'Flamengo', 'Fluminense', 'Vasco')

print(type(times_rj)) # class=’tuple’
print(times_rj) # ('Botafogo', 'Flamengo', 'Fluminense', 'Vasco')


#As tuplas devem ser usadas em situações em que não haverá necessidade de adicionar, remover
# ou alterar elementos de um grupo de itens.
# Exemplos bons seriam os meses do ano, os dias da semana, as estações do ano etc.
# Nesses casos, não haverá mudança nesses itens (pelo menos isso é muito improvável).