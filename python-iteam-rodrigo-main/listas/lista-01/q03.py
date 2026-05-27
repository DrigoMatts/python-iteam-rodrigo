# Lista 01 — Questão 03: Ficha de Cadastro
# Aluno: (RodrigoMatosGomes)
# Data:  (23/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Solicite: nome completo, CPF (str), ano de nascimento (int), altura (float).
# O programa deve:
#   1. Calcular e exibir a idade em 2026.
#   2. Exibir todos os dados com f-string e tipos corretos.
#   3. Tratar com try/except o caso em que o ano não seja um número.
# Explique em comentário: por que float para altura e não int?

# ── Sua solução abaixo ──────────────────────────────────────────────────────
nome = input("Digite seu nome completo: ")
cpf = input("Digite seu CPF: ")

# Tratamento de erro para o ano de nascimento
try:
    ano_nascimento = int(input("Digite seu ano de nascimento (ex: 1990): "))
    idade = 2026 - ano_nascimento
except ValueError:
    print("Erro: O ano de nascimento deve ser um número inteiro.")
# Define valores padrão ou interrompe o fluxo dependendo da necessidade
    ano_nascimento = 0
    idade = 0

altura = float(input("Digite sua altura (ex: 1.75): "))

# Exibição dos dados
print(f"\n--- Ficha de Cadastro ---")
print(f"Nome: {nome}")
print(f"CPF: {cpf}")
print(f"Ano de Nascimento: {ano_nascimento}")
print(f"Idade em 2026: {idade} anos")
print(f"Altura: {altura:.2f} m")

# O tipo 'int' (inteiro) é utilizado apenas para números sem casas decimais
# A altura de uma pessoa quase sempre envolve uma medida fracionária
# (ex: 1.75m), o que requer o tipo 'float' (ponto flutuante) para representar valores decimais
