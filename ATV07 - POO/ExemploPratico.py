class Forma:
    def area(self):
        pass

    def perimetro(self):
        pass

class Retangulo(Forma):
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def area(self):
        return self.comprimento * self.largura

    def perimetro(self):
        return 2 * (self.comprimento + self.largura)

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio * self.raio

    def perimetro(self):
        return 2 * 3.14 * self.raio

# Criar objetos de forma
retangulo = Retangulo(5, 4)
circulo = Circulo(3)

# Processar diferentes formas usando os mesmos métodos
formas = [retangulo, circulo]
for forma in formas:
    print(f"Área: {forma.area()}")
    print(f"Perímetro: {forma.perimetro()}")

# Neste exemplo, tanto RETANGULO e CIRCULO herdam de FORMA e substituem seus métodos.
# Podemos processar diferentes formas com o mesmo código, demonstrando o polimorfismo.