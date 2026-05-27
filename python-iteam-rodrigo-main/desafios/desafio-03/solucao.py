# Desafio 03 — Sistema de Multas
# Aluno: RodrigoMatosGomes
# Data:  20/05/2026

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
# Solicita a velocidade atual do carro
velocidade = float(input("Qual a velocidade atual do carro em km/h? "))

# Verifica se a velocidade ultrapassa o limite
if velocidade > 80:
    print("Multado! Você excedeu o limite de 80km/h")
# Calcula o valor da multa (R$ 7,00 por km acima do limite)
    excesso = velocidade - 80
    multa = excesso * 7
    print(f"O valor da multa é de: R$ {multa:.2f}")
else:
# Caso a velocidade esteja dentro do limite
    print("Boa viagem! Dirija com segurança")
