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


#2. Par ou Ímpar
# Desenvolva um programa que determine se um número inserido pelo usuário é par ou ímpar.

escolha = int(input("digite um numero inteiro: "))
var = 2
calc = escolha % var

if calc == 0:
    print(escolha, "É UM NUMERO PAR")
else:
    print(escolha, "É UM NUMERO IMPAR")


#3. Jogo de Pedra, Papel e Tesoura
# Crie um jogo de Pedra, Papel e Tesoura onde o usuário joga contra o computador.

import random

op = ["pedra", "papel", "tesoura"]
jogador = input("Derrote o Computador!!! Escolha pedra, papel ou tesoura e tente a sorte :D : ")
pc = random.choice(op)

print("O jogador escolheu: ", jogador)
print("O Computador escolheu: ", pc)

if jogador not in op:
    print("Esta opção não existe, Jogador...")
elif jogador == pc:
    print("Round Empatado!!!")
elif ((jogador == "pedra" and pc == "tesoura") or 
     (jogador == "tesoura" and pc == "papel") or 
     (jogador == "papel" and pc == "pedra")):
    print("Você derrotou o computador! Parabéns :D")
else:
    print("Ele venceu... Mas a batalha ainda não acabou!! Tente novamente e derrote-o.")

# .lower() = transforma tudo em minusculo
# elif or \ = Separar grandes linhas de código, pode ser substituida por () no elif inteiro (ex: 3.)