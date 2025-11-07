# Desenvolva uma função chamada eh_par que receba um número como parâmetro e retorne True se o número for par e False caso contrário.

def eh_par(x):
    if x % 2 == 0:
        return True
    else:
        return False
resultado = eh_par(11)
print(resultado)


def eh_par2(x):
    return x % 2 == 0

print(eh_par2(19))
