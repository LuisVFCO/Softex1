from classes import livro
from funcoes import loja
from banco import livros, estoques


loja = loja()

livro1 = livro(1, "O Pequeno Principe", "A. Saint-Exupéry", "21/04/1943")
livro2 = livro(2, "Sobrevivendo no inferno", "Racionais Mc's", "31/10/2018")

# Teste para o livro 1
loja.cadastrar(livro1, 10)

loja.saida(1, 2)
loja.saida(1, 2)
loja.saida(1, 2) 

loja.entrada(1, 5) 

# Teste para o livro 2
loja.cadastrar(livro2, 5)
loja.entrada(2, 7) 
loja.saida(2, 13) 

# Teste para o livro 3 (Caso tenha apresentacao)