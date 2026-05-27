# Desafio 09 — Sistema de Frota
# Aluno: RodrigoMatosGomes
# Data:  27/05/2026

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano
        self.__quilometragem = 0  # Atributo protegido (encapsulado)

    def rodar(self, km):
        if km > 0:
            self.__quilometragem += km
        else:
            print("A quilometragem deve ser positiva.")

    def exibir_dados(self):
        return f"Marca: {self.marca}, Ano: {self.ano}, KM: {self.__quilometragem}"


class Caminhao(Veiculo):
    def __init__(self, marca, ano, capacidade_carga):
        super().__init__(marca, ano)
        self.capacidade_carga = capacidade_carga

    def exibir_dados(self):
        # Uso do super() para reaproveitar a lógica da classe pai
        dados_base = super().exibir_dados()
        return f"{dados_base}, Carga: {self.capacidade_carga}t"


class Moto(Veiculo):
    def __init__(self, marca, ano, cilindradas):
        super().__init__(marca, ano)
        self.cilindradas = cilindradas

    def exibir_dados(self):
        dados_base = super().exibir_dados()
        return f"{dados_base}, Cilindradas: {self.cilindradas}cc"
