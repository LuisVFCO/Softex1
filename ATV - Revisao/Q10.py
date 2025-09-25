alguem_reprovou = False

for i in range(1, 6):
    while True:
        nota = float(input(f"Digite a nota do {i}° aluno (0 a 10): "))
        if 0 <= nota <= 10:
            break
        else:
            print("Nota inválida!")
    if nota < 5.0:
        alguem_reprovou = True

if alguem_reprovou:
    print("Pelo menos um aluno reprovou!")
else:
    print("Todos na turma foram aprovados!")
