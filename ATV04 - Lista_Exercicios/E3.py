login = input("Digite seu login: ")

while True:
    senha = input("Digite sua senha: ")
    if senha == login:
        print("Senha invalida! A senha não deve ser igual ao login!")
    elif login in senha:
        print("Senha inválida! A senha não deve conter o login!")
    else:
        print("Senha válida!")
        break

