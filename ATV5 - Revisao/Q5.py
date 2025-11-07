#  Peça ao usuário para digitar uma frase.

frase = input("Digite uma frase: ").lower()

vogais = "aeiou"
qtdvogais = 0
qtdconso = 0

for letra in frase:
    if letra.isalpha():
        if letra in vogais:
            qtdvogais = qtdvogais + 1
        else:
            qtdconso = qtdconso + 1

print(f"Número de vogais: {qtdvogais}")
print(f"Número de consoantes: {qtdconso}")
