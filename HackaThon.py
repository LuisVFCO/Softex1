caixa = str(input("Deseja registrar um novo cliente (s/n)?: ")).lower()

totalingresso = []

while caixa == "s":
    totalingresso.append(caixa)
    estu = input("Você é estudante? (s/n)?: ")

    if estu == "s":
        print("Preço estudante: R$ 15,00")
    else:
        idade = int(input("Digite sua idade: "))
        if idade < 12:
            print("Preço infantil: R$ 15,00")
        else:
            print("Preço normal: R$ 30,00")
    caixa = str(input("Deseja registrar um novo cliente (s/n)?: ")).lower()

print("Total de ingressos vendidos: ", len(totalingresso))