# 1. Cardápio Simples
# Crie um programa que simule um cardápio de restaurante, permitindo ao usuário escolher um item e visualizar o preço.
cardapio = {1: ("Hambúrguer", 25.00), 2: ("Batata Frita", 15.00), 3: ("Salada", 8.00), 4: ("Refrigerante", 5.00), 5: ("Sobremesa", 20.00)}

print("CARDÁPIO")
print("1 - Hambúrguer - R$25,00")
print("2 - Batata Frita - R$15,00")
print("3 - Salada - R$8,00")
print("4 - Refrigerante - R$5,00")
print("5 - Sobremesa - R$20,00")

pedido = int(input("Digite o código do seu pedido: "))

if pedido == 1:
    print("Você escolheu: Hambúrguer - R$25,00, aguarde o pedido ser entregue!")
elif pedido == 2:
    print("Você escolheu: Batata Frita - R$15,00, aguarde o pedido ser entregue!")
elif pedido == 3:
    print("Você escolheu: Salada - R$8,00, aguarde o pedido ser entregue!")
elif pedido == 4:
    print("Você escolheu: Refrigerante - R$5,00, aguarde o pedido ser entregue!")
elif pedido == 5:
    print("Você escolheu: Sobremesa - R$20,00, aguarde o pedido ser entregue!")
else:
    print("Opção inválida.")