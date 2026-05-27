# Projeto Integrador — Urna Eletrônica
# Aluno: (RodrigoMatosGomes)

# ── Escreva sua solução abaixo ──────────────────────────────────────
from candidatos import Candidato
from relatorio import exibir_resultado

# Cadastro de candidatos em um dicionário (chave: número)
candidatos = {
    10: Candidato("João Silva", 10, "Partido A"),
    20: Candidato("Maria Souza", 20, "Partido B")
}

def iniciar_urna():
    print("Urna Eletrônica Iniciada.")
    while True:
        try:
            voto = input("Digite o número do candidato (ou 'fim' para encerrar): ")
            
            if voto.lower() == 'fim':
                break
            
            numero = int(voto)
            if numero in candidatos:
                candidatos[numero].receber_voto()
                print("Voto registrado com sucesso!")
            else:
                print("Candidato não encontrado. Voto nulo.")
        except ValueError:
            print("Entrada inválida! Digite apenas números.")

    exibir_resultado(candidatos)

if __name__ == "__main__":
    iniciar_urna()