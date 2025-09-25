# Faça um programa "Controle de Despesas". 

despesas = []

while True:
    valor = float(input("Digite o valor da despesa (0 para encerrar): "))
    if valor == 0:
        break
    elif valor < 0:
        print("Valor inválido!")
    else:
        despesas.append(valor)

total = sum(despesas)
quantidade = len(despesas)
media = total / quantidade if quantidade > 0 else 0

print(f"Total gasto: R$ {total}")
print(f"Despesas: {quantidade}")
print(f"Média de despesas: R$ {media}")
