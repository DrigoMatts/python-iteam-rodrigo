class Candidato:
    """Representa um candidato na urna."""
    
    def __init__(self, nome, numero, partido):
        """Inicializa um candidato com nome, número, partido e votos zerados."""
        self._nome = nome
        self._numero = numero
        self._partido = partido
        self._votos = 0

    @property
    def nome(self): 
        """Retorna o nome do candidato."""
        return self._nome

    @property
    def votos(self): 
        """Retorna a quantidade atual de votos do candidato."""
        return self._votos

    @property
    def numero(self): 
        """Retorna o número do candidato."""
        return self._numero

    def receber_voto(self):
        """Incrementa o contador de votos."""
        self._votos += 1