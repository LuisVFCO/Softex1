class usuario:
    def __init__(self, id_usuario, nome, cpf):
        self.id_usuario = id_usuario
        self.nome = nome
        self.cpf = cpf

class livro:
    def __init__(self, id_livro, titulo, autor, data_lanc):
        self.id_livro = id_livro
        self.titulo = titulo
        self.autor = autor
        self.data_lanc = data_lanc

class estoque:
    def __init__(self, id_livro, quantidade):
        self.id_livro = id_livro
        self.quantidade = quantidade

    def add_livro(self, qtd):
        self.quantidade += qtd

    def rmv_livro(self, qtd):
        if qtd <= self.quantidade:
            self.quantidade -= qtd
            return True
        return False