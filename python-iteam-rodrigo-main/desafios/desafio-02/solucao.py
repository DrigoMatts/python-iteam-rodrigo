# Desafio 02 — Calculadora de IMC
# Aluno: RodrigoMatosGomes
# Data: 19/05/2026

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
# Solicita o nome do usuário
nome = input("Digite seu nome: ")

# Solicita o peso e a altura
# Utilizamos float() para permitir números decimais
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# 3. Calcula o IMC: peso ÷ altura²
valor_imc = peso / (altura ** 2)

# 4. Exibe o resultado formatado
print(f"Olá {nome}, seu IMC é {valor_imc:.2f}")