# Desafio 07 — Bio-Calculadora
# Aluno: RodrigoMatosGomes
# Data:  26/05/2026

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
from funcoes_mat import area_circulo, volume_esfera, hipotenusa

def menu():
    print("\n--- Calculadora Modular ---")
    print("1. Área do Círculo")
    print("2. Volume da Esfera")
    print("3. Hipotenusa")
    print("0. Sair")
    return input("Escolha uma opção: ")

while True:
    opcao = menu()
    
    if opcao == '1':
        r = float(input("Digite o raio: "))
        print(f"Resultado: {area_circulo(r):.2 f}")
    elif opcao == '2':
        r = float(input("Digite o raio: "))
        print(f"Resultado: {volume_esfera(r):.2 f}")
    elif opcao == '3':
        a = float(input("Cateto A: "))
        b = float(input("Cateto B: "))
        print(f"Resultado: {hipotenusa(a, b):.2 f}")
    elif opcao == '0':
        break
    else:
        print("Opção inválida.")
