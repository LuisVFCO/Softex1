preco_pao = 0.75
preco_broa = 1.25
preco_sonho = 2.99
preco_bolo = 1.50
preco_suco = 3.50

total = 0

qtd_pao = int(input("informe quantos pães você quer? "))
total = total + qtd_pao * preco_pao

qtd_broa = int(input("informe quantas broas você quer? "))
total = total + qtd_broa * preco_broa

qtd_sonho = int(input("informe quantos sonhos você quer? "))
total = total + qtd_sonho * preco_sonho

qtd_bolo = int(input("informe quantos bolos você quer? "))
total = total + qtd_bolo * preco_bolo

qtd_suco = int(input("informe quantos sucos naturais você quer? "))
total = total + qtd_suco * preco_suco

print(f"Você deve pagar: R$ {total:.2f}")