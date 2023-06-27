nota1 = 5
nota2 = 10
nota3 = 8

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"Aprovado com média {media:.1f}")
elif (media < 7) and (media >= 6):
    print(f"Recuperação com média {media:.1f}")
else:
    print(f"Reprovado com média {media:.1f} ")


