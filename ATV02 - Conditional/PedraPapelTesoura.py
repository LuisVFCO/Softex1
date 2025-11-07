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