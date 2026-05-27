# Desafio 04 — Tabuada Personalizada
# Aluno: RodrigoMatosGomes
# Data:  21/05/2026

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

while True:
    # Solicita ao usuário um número
    numero = int(input("Digite um número de 1 a 10 para ver a tabuada (ou 0 para sair): "))

    # Garante que o programa pare se o usuário digitar 0
    if numero == 0:
        print("Encerrando o programa...")
        break

    # Validação simples para o intervalo solicitado
    if 1 <= numero <= 10:
        print(f"\nTabuada do {numero}:")
        # Utiliza um laço for para exibir a tabuada
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
        print("-" * 20)
    else:
        print("Por favor, digite um número válido entre 1 e 10.")
