#2. Par ou Ímpar
# Desenvolva um programa que determine se um número inserido pelo usuário é par ou ímpar.

escolha = int(input("digite um numero inteiro: "))
var = 2
calc = escolha % var

if calc == 0:
    print(escolha, "É UM NUMERO PAR")
else:
    print(escolha, "É UM NUMERO IMPAR")