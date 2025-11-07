# Crie um programa que simule uma votação.

print("VOTAÇÃO ABERTA")
print("10 - Candidato A")
print("20 - Candidato B")
print("30 - Candidato C")
print("98 - Voto Nulo")
print("99 - Voto em Branco")

while True:
    voto = int(input("Digite o seu voto: "))
    if voto != 10 and voto != 20 and voto != 30 and voto != 98 and voto != 99:
        print("Valor inválido, digite novamente!")
        continue
    elif voto == 10:
        print("Você votou no Candidato A (10)")
        break
    elif voto == 20:
        print("Você votou no Candidato B (20)")
        break
    elif voto == 30:
        print("Você votou no Candidato B (30)")
        break
    elif voto == 98:
        print("Você votou nulo (98)")
        break
    elif voto == 99:
        print("Você votou em branco (99)")
        break    