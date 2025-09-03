idade = int(input("Digite sua idade: "))
estu = input("Você é estudante? (s/n)?: ")

if estu == "s":
    print("Preço estudante: R$ 15,00")
else:
    if idade < 12:
        print("Preço infantil: R$ 15,00")
    elif idade >= 12:
        print("Preço normal: R$ 30,00")
    