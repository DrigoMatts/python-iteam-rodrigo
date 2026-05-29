# Desafio 10 — Projeto Final — Urna Eletrônica
# Aluno: RodrigoMatosGomes
# Data:  27/05/2026

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
### R:
# --- Configuração Inicial (Pré-carregamento) ---
candidatos = {
    10: {"nome": "Candidato A", "partido": "XPTO", "votos": 0},
    20: {"nome": "Candidato B", "partido": "ABCD", "votos": 0},
    30: {"nome": "Candidato C", "partido": "ZYXW", "votos": 0}
}

eleitores = {
    "111": {"nome": "Ana", "votou": False},
    "222": {"nome": "Beto", "votou": False},
    "333": {"nome": "Caio", "votou": False},
    "444": {"nome": "Duda", "votou": False},
    "555": {"nome": "Edu", "votou": False}
}

votos_totais = 0

# --- Funções do Sistema ---
def listar_candidatos():
    print("\n--- Candidatos Disponíveis ---")
    for num, dados in candidatos.items():
        print(f"Número: {num} | Nome: {dados['nome']} | Partido: {dados['partido']}")

def registrar_voto(id_eleitor, num_candidato):
    global votos_totais
    
    # Validações
    if id_eleitor not in eleitores:
        return "Erro: Eleitor não encontrado."
    if eleitores[id_eleitor]["votou"]:
        return "Erro: Eleitor já votou."
    if num_candidato not in candidatos:
        return "Erro: Candidato não existe."
    
    # Processamento/casting
    candidatos[num_candidato]["votos"] += 1
    eleitores[id_eleitor]["votou"] = True
    votos_totais += 1
    return f"Voto registrado com sucesso para {candidatos[num_candidato]['nome']}!"

def gerar_relatorio():
    print("\n--- Relatório de Apuração ---")
    total_eleitores = len(eleitores)
    participacao = (votos_totais / total_eleitores) * 100 if total_eleitores > 0 else 0
    
    print(f"Eleitores habilitados: {total_eleitores}")
    print(f"Votos registrados: {votos_totais}")
    print(f"Percentual de participação: {participacao:.2f}%")
    
    print("\nDetalhamento por Candidato:")
    # Ordena candidatos por votos (decrescente)
    ordenados = sorted(candidatos.values(), key=lambda x: x['votos'], reverse=True)
    for c in ordenados:
        percent = (c['votos'] / votos_totais * 100) if votos_totais > 0 else 0
        print(f"{c['nome']}: {c['votos']} votos ({percent:.2f}%)")

# --- Loop Principal ---
def menu():
    while True:
        print("\n=== URNA ELETRÔNICA ===")
        print("1. Votar")
        print("2. Encerrar votação e ver relatório")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            try:
                id_e = input("Digite seu ID de eleitor: ")
                listar_candidatos()
                voto = int(input("Digite o número do candidato: "))
                print(registrar_voto(id_e, voto))
            except ValueError:
                print("Entrada inválida! Digite números para o candidato.")
        elif opcao == "2":
            gerar_relatorio()
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
