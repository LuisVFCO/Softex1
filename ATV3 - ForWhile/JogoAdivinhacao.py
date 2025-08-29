# 2. Jogo de Adivinhação

"""
Crie um "jogo de adivinhação". Defina um número secreto no código (por
exemplo, 42). Peça para o usuário adivinhar o número. O laço deve continuar
até que o usuário acerte. A cada tentativa errada, dê uma dica se o palpite foi
"muito alto" ou "muito baixo".
"""

numSecr = 55

print("Bem vindo ao Jogo da Adivinhação! Descubra o número secreto!!")

usu = int(input("Adivinhe o número: "))

while numSecr != usu:
    if usu > 55 and usu <= 65:
        print("Boa tentativa, você esta quase la! Tente outra vez.")
    elif usu > 65:
        print("Muito ALTO jogador(a), tente outra vez")
    elif usu < 55 and usu >= 45:
        print("Boa tentativa, mas foi muito baixo jogador(a), tente outra vez!")
    elif usu < 45:
        print("Muito BAIXO jogador(a), tente outra vez")
    
    usu = int(input("Adivinhe o número novamente: "))

    if usu == numSecr:
        print("PARABÉNS JOGADOR(A), ERA 55!!!")
