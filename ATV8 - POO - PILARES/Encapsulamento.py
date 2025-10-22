class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado!")
        else:
            print("O depósito deve ser positivo.")

    def sacar(self, valor):
        if valor <= 0:
            print("O saque deve ser positivo.")
        elif valor > self.__saldo:
            print("Saldo insuficiente.")
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado!")

    def get_saldo(self):
        return self.__saldo


conta = ContaBancaria(900)

conta.depositar(600)
conta.sacar(200)
print(f"Saldo atual: R${conta.get_saldo():.2f}")

conta.sacar(2000)
conta.depositar(-50)
