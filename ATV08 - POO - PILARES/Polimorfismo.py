class ExportadorDeDados:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo

    def exportar(self, dados):
        raise NotImplementedError("Esse método deve ser implementado nas subclasses")


class ExportadorParaCSV(ExportadorDeDados):
    def exportar(self, dados):
        with open(self.caminho_arquivo, "w", encoding="utf-8") as arquivo:
            for item in dados:
                linha = ",".join(str(valor) for valor in item.values())
                arquivo.write(linha + "\n")
        print("Arquivo CSV criado!")


class ExportadorParaTXT(ExportadorDeDados):
    def exportar(self, dados):
        with open(self.caminho_arquivo, "w", encoding="utf-8") as arquivo:
            for item in dados:
                for chave, valor in item.items():
                    arquivo.write(f"{chave}: {valor} ")
                arquivo.write("\n")
        print("Arquivo TXT criado!")


def gerar_relatorios(exportadores, dados):
    for exportador in exportadores:
        exportador.exportar(dados)


usuarios = [
    {"nome": "Ana", "idade": 25, "email": "ana@email.com"},
    {"nome": "Bruno", "idade": 30, "email": "bruno@email.com"}]

exportadores = [
    ExportadorParaCSV("usuarios.csv"),
    ExportadorParaTXT("usuarios.txt")]

gerar_relatorios(exportadores, usuarios)

