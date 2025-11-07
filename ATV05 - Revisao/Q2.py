# Faça um programa que simule um caixa de supermercado.

valor = 0

while True:
    preco = float(input("Digite o preço do produto: "))
    if preco == 0:
        break
    elif preco < 0:
        print("Preço inválido! Digite um valor positivo ou 0 para finalizar.")
    else:
        valor += preco

print(f"Valor total da compra: R$ {valor}")
