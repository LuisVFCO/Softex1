numero = int(input("Digite um número de 0 a 100: "))

listanumero = []

while True:
    listanumero.append(numero)
    numero = int(input("Digite o proximo numero: "))
    if numero == 101:
        print(min(listanumero))
        break

# usando o len
""" numero = int(input("Digite um número: "))

listanumero = []

while True:
    listanumero.append(numero)
    
    # se já tiver 7 números, para o programa
    if len(listanumero) == 7:
        print("O menor número digitado foi:", min(listanumero))
        break
    
    numero = int(input("Digite o próximo número: "))
"""
