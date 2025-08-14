# Olá mundo personalisado
nome = input("Informe seu nome: ")
print("Olá!", nome ,"^^ Bem-vindo!(a) ao mundo do Python :D")

# Calculadora simples
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um segundo número: "))

som = num1 + num2
sub = num1 - num2
multi = num1 * num2
div = num1 / num2

print("A soma de", num1, "e", num2, "é: ", som)
print("A subtração de", num1, "e" ,num2, "é: ", sub)
print("A multiplicação de", num1, "e" ,num2, "é: ", multi)
print("A divisão de", num1, "e" ,num2, "é: ", div)

# Informacoes do produto
nome_produto = str
preco_produto = float
quantidade_estoque = int

np = input("Informe um produto: ")
pp = float(input("Informe o preco do produto: "))
qp = int(input("informe a quantidade em estoque do produto: "))

print("Produto:", np)
print("preco:", pp)
print("quantidade em estoque:", qp)

# Calculadora de Área de retângulo
alt = float(input("Informe a altura em metros (m): "))
larg = float(input("Informe a largura em metros (m): "))
are = alt * larg

print("Um retângulo com altura de", alt, "(m) e largura de", larg, "(m) possui uma área de", are, "metros quadrados!")

# Conversor de Moedas (Simples)
dol = 5.25
conv = float(input("Insira o valor em reais (R$): "))
resul = conv * dol

print("O valor de R$", conv, "equivale a US$", resul)
