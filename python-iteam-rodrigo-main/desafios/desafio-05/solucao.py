# Desafio 05 — Gerenciador de Compras
# Aluno: RodrigoMatosGomes
# Data:  22/05/2026

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
# Começa com uma lista vazia
compras = []

# while para pedir nomes de produtos
while True:
    produto = input("Digite o nome do produto (ou 'fim' para encerrar): ")
    
# Pare quando o usuário digitar "fim"
    if produto.lower() == "fim":
        break
        
# adicione cada produto com append
    compras.append(produto)

# Exibe a lista organizada (alfabética) e o total de itens
compras.sort()
print(f"\nLista de Compras: {compras}")
print(f"Total de itens: {len(compras)}")
