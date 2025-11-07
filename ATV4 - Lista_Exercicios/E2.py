while True:
    nome = input("Digite seu nome: ")
    if len(nome) >= 3:
        print("nome inserido com sucesso: {nome}")
        break
    else:
        print("Nome inválido!")


while True:
    idade = int(input("Digite sua idade : "))
    if idade > 0 and idade < 100:
        print(f"idade inserida com sucesso: {idade}")
        break
    else:
        print("Idade inválida!")

while True:
    salario = float(input("Digite seu salário: "))
    if salario >= 0:
        print(f"Salário inserido com sucesso: {salario}")
        break
    else:
        print("Salário inválido!")

while True:
    genero = str(input("Digite seu gênero (f/m/outro): ")).lower()
    if genero == "f" or genero == "m" or genero == "o":
        print(f"Gênero inserido com sucesso: {genero}")
        break
    else:
        print("Gênero invalido!")

while True:
    situemp = str(input("Digite sua situação empregatícia (E,D,A): ")).upper()
    if situemp == "E" or situemp == "D" or situemp == "A":
        print(f"Situação empregaticia inserida com sucesso: {situemp}")
        break
    else:
        print("Situação empregatícia inválida!")