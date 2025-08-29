# 4. Cadastro e Análise de Idades

"""
Crie um programa que peça ao usuário para digitar idades continuamente. Cada
idade digitada deve ser armazenada em uma lista. O laço deve parar quando o
usuário digitar -1. No final, percorra a lista e diga quantas pessoas são maiores
de idade (idade >= 18).
"""

idade = int(input("Digite a sua idade: "))

listaIdade = []
maiorIdade = 0

while idade != -1:
    listaIdade.append(idade)
    idade = int(input("Digite a sua idade: "))

for idades in listaIdade:
    if idades >= 18:
        maiorIdade = maiorIdade + 1

if maiorIdade == 0:
    print("Não tem maiores de idade aqui!")
else:
    print(maiorIdade, "pessoas são maiores de idade!")

