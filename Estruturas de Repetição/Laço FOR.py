# O laço for nos permite percorrer os itens de uma coleção e,
# para cada um deles, executar um bloco de código.

# interação em um array
nomes = ['Pedro', 'João', 'Leticia']
for n in nomes:
    print(n)
# Pode ser usado com else também
else:
    print("Todos os nomes da lista já foram listados")

print("\n")

# utilizando o metódo range, que limita uma quantidade de interações.

for i in range(0,5):
    print(f"Está é a {i}º interação ")
# Pode ser usado com else também
else:
    print("Todas as interações foram concluídas")