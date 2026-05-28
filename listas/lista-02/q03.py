# Lista 02 — Questão 03: Sistema de Inventário
# Aluno: (RodrigoMatosGomes)
# Data:  (27/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Implemente com lista de dicionários:
#   1. adicionar_produto(inventario, nome, codigo, quantidade, preco)
#   2. buscar_por_codigo(inventario, codigo)  → produto ou None
#   3. listar_abaixo_do_minimo(inventario, minimo)
#   4. valor_total(inventario)  → soma de quantidade × preço
# Use funções para cada operação. Demonstre as 4 no código principal.

# ── Sua solução abaixo ──────────────────────────────────────────────────────

### R:
# Função para adicionar produto
def adicionar_produto(inventario, nome, codigo, quantidade, preco):
    produto = {
        "nome": nome,
        "codigo": codigo,
        "quantidade": quantidade,
        "preco": preco
    }
    inventario.append(produto)

# Função para buscar por código
def buscar_por_codigo(inventario, codigo):
    for produto in inventario:
        if produto["codigo"] == codigo:
            return produto
    return None

# Função para listar produtos abaixo do estoque mínimo
def listar_abaixo_do_minimo(inventario, minimo):
    abaixo = [p for p in inventario if p["quantidade"] < minimo]
    return abaixo

# Função para calcular o valor total do inventário
def valor_total(inventario):
    total = sum(p["quantidade"] * p["preco"] for p in inventario)
    return total

# --- Demonstração no código principal ---

meu_inventario = []

# Demonstrando 1: Adicionar
adicionar_produto(meu_inventario, "Teclado", 101, 5, 150.0)
adicionar_produto(meu_inventario, "Mouse", 102, 2, 80.0)
adicionar_produto(meu_inventario, "Monitor", 103, 10, 900.0)

# Demonstrando 2: Buscar
print(f"Busca código 102: {buscar_por_codigo(meu_inventario, 102)}")

# Demonstrando 3: Listar abaixo do mínimo (ex: 4 unidades)
print(f"Produtos abaixo de 4 unidades: {listar_abaixo_do_minimo(meu_inventario, 4)}")

# Demonstrando 4: Valor Total
print(f"Valor total em estoque: R$ {valor_total(meu_inventario):.2f}")
