numero = int(input("Digite um número: "))
soma = 0

for i in range(1, numero):
    if numero % i == 0:
        soma = soma + i
else:
    if soma == numero:
        print(f"{numero} é perfeito")
    elif soma != numero:
        print(f"{numero} é imperfeito")