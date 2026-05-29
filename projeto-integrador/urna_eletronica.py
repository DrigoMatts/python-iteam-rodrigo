# Projeto Integrador — Urna Eletrônica
# Aluno: (RodrigoMatosGomes)

# ── Escreva sua solução abaixo ──────────────────────────────────────

from urna import Urna
from candidatos import Candidato
from excecoes import CandidatoNaoEncontradoError

def main():
    urna = Urna()
    urna.adicionar_candidato(Candidato("João Silva", 10, "Partido A"))
    
    while True:
        entrada = input("Digite o número (ou 'fim'): ")
        if entrada.lower() == 'fim': break
        
        try:
            urna.computar_voto(int(entrada))
        except ValueError:
            print("Entrada inválida!")
        except CandidatoNaoEncontradoError as e:
            print(e)
            
    urna.exibir_resultado()

if __name__ == "__main__":
    main()