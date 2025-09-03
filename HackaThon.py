print("CINEMA - PREÇOS")
print("Preço infantil: R$ 15,00")
print("Preço estudante: R$ 15,00")
print("Preço normal: R$ 30,00")
print("Segunta tem promoção!! Ingresso por R$12,50")

dia = input("Que dia da semana é hoje (segunda): ").lower()
caixa = input("Deseja registrar um novo cliente (s/n)?: ").lower()

totalingresso = []

while caixa == "s":
    totalingresso.append(caixa)

    if dia == "segunda":
        print("Preço promocional: R$ 12,50")
    else:
        estu = input("Você é estudante? (s/n)?: ").lower()
        if estu == "s":
            print("Preço estudante: R$ 15,00")
        else:
            idade = int(input("Digite sua idade: "))
            if idade < 12:
                print("Preço infantil: R$ 15,00")
            else:
                print("Preço normal: R$ 30,00")

    caixa = input("Deseja registrar um novo cliente (s/n)?: ").lower()

print("Total de ingressos vendidos:", len(totalingresso))