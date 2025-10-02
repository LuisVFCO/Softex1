# quantidade total para padaria 
precopao = 0.75
precobroa = 1.25
precosonho = 2.99
precobolo = 1.50
precosuco = 3.50

total = 0

qtdpao = int(input("informe quantos pães você quer? "))
total = total + qtdpao * precopao

qtdbroa = int(input("informe quantas broas você quer? "))
total = total + qtdbroa * precobroa

qtdsonho = int(input("informe quantos sonhos você quer? "))
total = total + qtdsonho * precosonho

qtdbolo = int(input("informe quantos bolos você quer? "))
total = total + qtdbolo * precobolo

qtdsuco = int(input("informe quantos sucos naturais você quer? "))
total = total + qtdsuco * precosuco

print("Você deve pagar: R$", total)
# print(f"Você deve pagar: R$ {total:.2f}") para melhor vizualização.
