class Gato:
    def __init__ (self, nome, raca, cor, sexo):
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.sexo = sexo
        self.acordado = False
        self.fome = 0
        
    def acordar(self):
        print(f"O {self.nome} acordou!")
        self.acordado = True

    def alimento(self):
        if self.acordado and self.fome <= 0:
            print(f"Dê de comer a {self.nome}! Ele esta faminto!")
            self.fome += 1
        elif self.acordado and self.fome == 1:
            self.fome += 1
            print(f"{self.nome} está comendo, ele parecia faminto, mas ainda está com fome!")
        elif self.acordado and self.fome == 2:
            self.fome += 1
            print(f"{self.nome} está comendo, ele parece estar gostando, mas ainda está com fome!")
        elif self.acordado and self.fome <= 3:
            self.fome += 1
            print(f"{self.nome} está comendo, ele parece quase cheio, mas ainda está com fome!")
        else:
            print(f"O {self.nome} está cheio!!")
            
    def dormir(self):
        print(f"O {self.nome} dormiu!")
        self.acordado = False
        
            
meu_gato = Gato("Cleiton", "Persa", "Preto", "Femea")

meu_gato.acordar()
meu_gato.alimento()
meu_gato.alimento()
meu_gato.alimento()
meu_gato.alimento()
meu_gato.alimento()
meu_gato.alimento()

print(f"O {meu_gato.nome} está com sono!")

meu_gato.dormir()      