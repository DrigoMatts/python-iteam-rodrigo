# Desafio 06 — Bio-Cadastro
# Aluno: RodrigoMatosGomes
# Data:  25/05/2026

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
equipe = []

while True:
    nome = input("Digite o nome do colaborador (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    
    cargo = input("Digite o cargo do colaborador: ")
    
    # Cria o dicionário e adiciona à lista
    colaborador = {"nome": nome, "cargo": cargo}
    equipe.append(colaborador)

# Percorre a lista e imprime os dados formatados
for funcionario in equipe:
    print(f"Funcionário: {funcionario['nome']} | Cargo: {funcionario['cargo']}")
