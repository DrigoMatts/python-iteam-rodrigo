# Lista 01 — Questão 06: Validador de Senha
# Aluno: (RodrigoMatosGomes)
# Data:  (23/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Escreva um programa que solicite uma senha em loop até que atenda TODOS:
#   1. Mínimo 8 caracteres.
#   2. Pelo menos um dígito (use .isdigit() em cada caractere).
#   3. Pelo menos uma letra maiúscula.
# Para cada tentativa inválida, informe qual critério não foi atendido.
# Ao aceitar: 'Senha válida após X tentativa(s).'

# ── Sua solução abaixo ──────────────────────────────────────────────────────
tentativas = 0

while True:
    tentativas += 1
    senha = input("Digite sua senha: ")
    
    # Verificação
    tem_digito = False
    tem_maiuscula = False
    
    # Verificação
    if len(senha) < 8:
        print("Erro: A senha deve ter pelo menos 8 caracteres.")
        continue
        
    # Verificar dígito e letra maiúscula
    for char in senha:
        if char.isdigit():
            tem_digito = True
        if char.isupper():
            tem_maiuscula = True
            
    # Erros config
    if not tem_digito:
        print("Erro: A senha deve conter pelo menos um dígito.")
    elif not tem_maiuscula:
        print("Erro: A senha deve conter pelo menos uma letra maiúscula.")
    else:
        # Se passou em todas as verificações
        print(f"Senha válida após {tentativas} tentativa(s).")
        break