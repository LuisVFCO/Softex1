# Declare uma variável global chamada contador com o valor 0.

contador = 0
def incrementar():
    global contador
    contador = contador + 1

incrementar()
print(contador)
incrementar()
print(contador)
incrementar()
print(contador)
incrementar()
print(contador)
incrementar()
print(contador)