# Peça ao usuário para digitar a idade de 10 pessoas.

crianca = 0
adolescente = 0
adulto = 0
idoso = 0

for i in range(1, 11):
    idade = int(input(f"Digite a idade da {i}° pessoa: "))

    if 0 <= idade <= 12:
        crianca = crianca + 1
    elif 13 <= idade <= 17:
        adolescente = adolescente + 1
    elif 18 <= idade <= 59:
        adulto = adulto + 1
    elif idade >= 60:
        idoso = idoso + 1
    else:
        print("Idade inválida!")

print(f"Crianças: {crianca}")
print(f"Adolescentes: {adolescente}")
print(f"Adultos: {adulto}")
print(f"Idosos: {idoso}")
