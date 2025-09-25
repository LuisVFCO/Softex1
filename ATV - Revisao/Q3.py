# Peça ao usuário um número inteiro positivo N.

while True:
    num = int(input("Digite um número: "))
    if num >= 0:
        break
    else:
        print("Número inválido!")

fatorial = 1

for i in range(1, num + 1):
    fatorial = fatorial * i

print(f"{num}! = {fatorial}")
