# Crie um menu interativo que simula a frente de um caixa de banco.

print("Caixa Eletrônico")
print("1. Ver Saldo")
print("2. Fazer Depósito")
print("3. Fazer Saque")
print("4. Sair")
print("0. Encerrar Programa")

while True:
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Você escolheu - Ver Saldo.")
    elif opcao == "2":
        print("Você escolheu - Fazer Depósito.")
    elif opcao == "3":
        print("Você escolheu - Fazer Saque.")
    elif opcao == "4":
        print("Você escolheu - Sair.")
    elif opcao == "0":
        print("Encerrando o sistema!")
        break
    else:
        print("Opção inválida! Tente novamente.")
