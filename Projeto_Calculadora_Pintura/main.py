from calculadora import Calculadora
from comodo import Comodo

calc = Calculadora()

largura = (input("Digite o valor da largura da parede: "))
profundidade = (input("Digite o valor da profundidade do cômodo: "))


comodo = Comodo(largura,profundidade)

area_parede = calc.calcular_area_parede(comodo)

print(f"A área do cômodo é de {area_parede}m²")

area_teto = calc.calcular_area_teto(comodo)

print(f"A área do teto é de {area_teto}m²")

litragem_tinta = calc.calcular_litragem_necessaria()

print(f"A quantidade de tinta necessária para pintar o cômodo é de {litragem_tinta}L")