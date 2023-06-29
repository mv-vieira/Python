from calculo import Calculo

def main():
    print(
        """
        Esta aplicação tem como finalidade demonstrar os valores que serão gastos
        com combustível durante uma viagem, com base no consumo do seu veículo, e
        com a distância determinada por você!
        """
    )

    print("""
Os combustíveis disponíveis para este cáculo são:
    
   ° Álcool
   ° Díesel
   ° Gasolina
        
    """)

    try:
        distancia = float(input("Informe a distância que será percorrida em km: \n"))
        consumo = float(input("Informe o consumo de seu veículo (km/L): \n "))
        calculo = Calculo()
        print(calculo.calcular_gasto(distancia,consumo))

    except ValueError as erro:
        print("O valor recebido não é válido")


if __name__ == "__main__":
    main()