# Escreva uma função chamada contar_vogais que receba uma string.

def contar_vogais(frase):
    vogais = "aeiouAEIOUáÁéÉíÍóÓúÚâÂêÊôÔãÃõÕ"
    contador = 0
    for letra in frase:
        if letra in vogais:
            contador = contador + 1
    return contador

exemplo = "Na minha época era MELHOR!"
print(contar_vogais(exemplo))