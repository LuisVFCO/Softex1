# 3. Média de Notas em uma Lista

"""
Você recebeu uma lista de notas: notas = [8.5, 9.0, 6.5, 10.0, 7.5]. Use um laço
for para calcular a soma total das notas. Após o laço, calcule e imprima a
média da turma.
"""

notas = [8.5, 9.0, 6.5, 10.0, 7.5]

soma = 0

for nota in notas:
    soma = soma + nota

med = soma / len(notas)

print("A soma das notas foi de: ", soma)
print("A média da turma é: ", med )