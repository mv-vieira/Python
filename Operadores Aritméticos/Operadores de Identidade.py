# Os operadores de identidade servem para a comparação de objetos.
# Nessa comparação é verificado se eles ocupam a mesma posição na memória,
# o que significará que se trata do mesmo objeto

time_carlos = 'Botafogo'
time_luciano = 'Flamengo'
time_fabricia = 'Botafogo'

if time_carlos is time_luciano:
    print("time_carlos - time_luciano = mesmo objeto")
else:
    print("time_carlos - time_luciano = objetos diferentes")

if time_carlos is time_fabricia:
    print("time_carlos - time_fabricia = mesmo objeto")
else:
    print("time_carlos - time_fabricia = objetos diferentes")