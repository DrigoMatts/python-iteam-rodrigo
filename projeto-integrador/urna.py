from excecoes import CandidatoNaoEncontradoError

class Urna:
    def __init__(self):
        """Esta classe gerencia a lógica de votação e armazenamento dos candidatos."""
        self._candidatos = {}
        """Adiciona um objeto Candidato ao dicionário de candidatos."""
    def adicionar_candidato(self, candidato):
        self._candidatos[candidato.numero] = candidato
        """Recebe o número, valida a existência do candidato e computa o voto."""
    def computar_voto(self, numero):
        if numero not in self._candidatos:
            raise CandidatoNaoEncontradoError(f"Candidato {numero} não encontrado.")
        self._candidatos[numero].receber_voto()
        """Percorre a lista de candidatos e imprime o total de votos de cada um."""
    def exibir_resultado(self):
        print("\n--- RESULTADO DA VOTAÇÃO ---")
        for c in self._candidatos.values():
            print(f"{c.nome} - Votos: {c.votos}")