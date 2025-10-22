class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

class aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Matrícula: {self.matricula}")

class professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Disciplina: {self.disciplina}")

vitor = aluno("Vitor", 17, "0001")
carlos = professor("Carlos", 40, "Matemática")

print("Dados do Aluno")
vitor.exibir_dados()

print("Dados do Professor")
carlos.exibir_dados()