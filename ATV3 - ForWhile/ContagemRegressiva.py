# 1. Contagem Regressiva de Ímpares

"""
Peça ao usuário para digitar um número inteiro positivo. Em seguida, use um
laço for para fazer uma contagem regressiva a partir desse número até 1. O
programa deve imprimir apenas os números ímpares encontrados nesse
intervalo.
"""

digi = int(input("Digite um numero inteiro positivo: "))

for i in range(digi, 0, -1):
    if i % 2 != 0:
        print(i)
