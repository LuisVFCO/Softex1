def calcular_imposto(valor):
    if valor < 1000:
        imposto = valor * 0.1
    elif valor < 2000:
        imposto = valor * 0.13
    else:
        imposto = valor * 0.2
    return imposto

preco_produto = 1500

imposto_produto = calcular_imposto(preco_produto)

print(f"O imposto do produto e de: {imposto_produto}")