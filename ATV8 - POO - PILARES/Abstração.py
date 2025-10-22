class Carro:
    def __init__ (self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False
        self.velo = 0
    
    def ligar(self):
        print(f"O carro da marca {self.marca} está ligando!")
        self.ligado = True
        print(f"O carro está ligado.")
    
    def desligar(self):
        print(f"O carro da marca {self.marca} está desligando!")
        self.ligado = False
        print(f"O carro está desligado.")
        
    def acelerar(self):
        if self.ligado:
            self.velo += 10
            print(f"O carro da marca {self.marca} acelerou!")
        else:
            print("Ligue o carro para poder acelerar!")
        
    def frear(self):
        if self.ligado and self.velo > 0:
            self.velo -= 10
            print(f"O carro da marca {self.marca} desacelerou!")
        elif self.ligado and self.velo <= 0:
            print("O veículo está parado!")
        else:
            print("Ligue o carro para poder acelerar!")

    def exibir_informacoes(self):
        print("-" * 30)
        print("Aqui Estão as Informações do seu Veículo")
        print("-" * 30)
        print(f"Marca : {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano   : {self.ano}")

        if self.ligado == True:
            print(f"O carro de marca {self.marca} está atualmente   : Ligado ")
        else:
            print(f"O carro de marca {self.marca} está atualmente   : Desligado ")    
        print(f"A velocidade atual do carro é de   : {self.velo}km/h")

        print("-" * 30)

# Criação do objeto
meu_carro = Carro("Toyota", "Corolla", 2022)

# Teste 1: Exibir informações iniciais
meu_carro.exibir_informacoes()

# Teste 2: Tentar acelerar com o carro desligado
meu_carro.acelerar()

# Teste 3: Ligar o carro
meu_carro.ligar()

# Teste 4: Acelerar duas vezes
meu_carro.acelerar()
meu_carro.acelerar()

# Teste 5: Frear uma vez
meu_carro.frear()

# Teste 6: Exibir informações novamente
meu_carro.exibir_informacoes()

# Teste 7: Desligar o carro
meu_carro.desligar()
