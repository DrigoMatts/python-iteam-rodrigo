# Desafio 01 — Seu Primeiro Script
# Aluno: Rodrigo Matos Gomes
# Data: 18/05/2026

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
 
nome = input("Digite o seu nome: ")
ano_nascimento_str = input("Digite o seu ano de nascimento: ")

# Conversão
ano_nascimento = int(ano_nascimento_str)
ano_atual = 2026

# Calcula a idade
idade = ano_atual - ano_nascimento

# Solicita os hobbies para o item 3
hobbies = input("Quais são os seus hobbies principais? (Separe por vírgulas): ")

print("\n--- Resultado ---")
# Exibe o nome e a idade calculada
print(f"Olá, {nome}! Você tem (ou vai completar) {idade} anos em {ano_atual}.")
# Exibe os hobbies principais
print(f"Seus hobbies principais são: {hobbies}")