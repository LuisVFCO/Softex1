# Modifique o exercício "Média da Turma".

alunos = int(input("Quantos alunos existem na sala?: "))
soma = 0

for i in range(1, alunos + 1):
    while True:
        nota = float(input(f"Digite a nota do aluno {i}: "))
        if 0 <= nota <= 10:
            break
        else:
            print("Nota inválida!")
    soma = soma + nota

media = soma / alunos
print(f"Média da turma: {media}")
