from banco import livros, estoques
from classes import estoque

class loja:
    def cadastrar(self, livro, qtd_ini):
        livros.append(livro)
        estoques[livro.id_livro] = estoque(livro.id_livro, qtd_ini)
    
    def entrada(self, id_livro, qtd):
        if id_livro in estoques:
            estoques[id_livro].add_livro(qtd)
            print(f"Algumas unidades do livro de numero {id_livro} foram adicionadas")
            print(f"Nova Quantidade: {estoques[id_livro].quantidade}")
        else:
            print("ERRO!!")

    def saida(self, id_livro, qtd):
        if id_livro in estoques:
            if estoques[id_livro].rmv_livro(qtd):
                print(f"Algumas unidades do livro de numero {id_livro} foram retiradas")
                print(f"Nova Quantidade: {estoques[id_livro].quantidade}")
                self.alertar()
            else:
                print("Não tem mais livros!")
        else:
            print("ERRO!!")

    def alertar(self):
        for id_livro, qtd in estoques.items():
            if qtd.quantidade < 5:
                livro = self.buscar(id_livro)
                print("\nALERTA: BAIXO ESTOQUE")
                print("Um livro apresenta estoque menor do que 5 unidades")
                print(f"Livro: {livro.titulo}")
                print(f"Quantidade: {qtd.quantidade}\n")

    def buscar(self, id_livro):
        for liv in livros:
            if liv.id_livro == id_livro:
                return liv
        return None
       