class Candidato:
    def __init__(self, nome, numero, partido):
        self.nome = nome
        self.numero = numero
        self.partido = partido
        self.votos = 0

    def receber_voto(self):
        self.votos += 1