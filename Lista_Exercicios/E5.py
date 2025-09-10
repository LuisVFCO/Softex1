anos = 0

while True:
    cidadeA = float(input("Digite a população inicial da cidade A: "))
    if cidadeA > 0:
        break
    else:
        print("Digite um valor positivo!")

while True:
    taxaA = float(input("Digite a taxa inicial da cidade A: "))
    if taxaA > 0:
        break
    else:
        print("Digite um valor positivo!")

while True:
    cidadeB = float(input("Digite a população inicial da cidade B: "))
    if cidadeB > 0:
        break
    else:
        print("Digite um valor positivo!")

while True:
    taxaB = float(input("Digite a taxa inicial da cidade B: "))
    if taxaB > 0:
        break
    else:
        print("Digite um valor positivo!")

while cidadeA <= cidadeB:
    cidadeA = cidadeA * (1 + taxaA)
    cidadeB = cidadeB * (1 + taxaB)
    anos = anos + 1

print(f"Levará {anos} anos para a população da cidade A ultrapassar a da cidade B.")