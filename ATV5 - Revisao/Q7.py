# Simule um interruptor de luz.

luz_acesa = False

while True:
    acao = input("O que fazer? (1: apertar interruptor, 0: sair): ")
    if acao == "1":
        luz_acesa = not luz_acesa
        if luz_acesa:
            print("A luz está ACESA.")
        else:
            print("A luz está APAGADA.")
    elif acao == "0":
        print("Encerrando o sistema.")
        break
    else:
        print("Erro!!! Digite 1 ou 0.")
