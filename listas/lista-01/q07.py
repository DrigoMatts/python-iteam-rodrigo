# Lista 01 — Questão 07: Progressão e Análise
# Aluno: (RodrigoMatosGomes)
# Data:  (23/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Leia 10 notas (0.0–10.0) com validação (try/except + while para inválidas).
# Exiba: maior nota, menor nota, média, quantidade acima da média e
# classificação (Aprovado ≥ 7.0, Recuperação ≥ 5.0, Reprovado).
# Explique em comentários por que escolheu for ou while em cada parte.

# ── Sua solução abaixo ──────────────────────────────────────────────────────
notas = []
# Escolha do 'for': Como sabemos exatamente que precisamos de 10 notas,
# o 'for' com 'range' é a estrutura ideal para um número fixo de iterações.
  # Escolha do 'while': Como não sabemos quantas vezes o usuário vai errar
# a digitação (digitar letra ou nota fora do intervalo), o 'while' é 
# perfeito para garantir que o programa só avance após um dado válido.
for i in range(1, 11):
    
    while True:
        try:
            nota = float(input(f"Digite a {i}ª nota (0.0-10.0): "))
            if 0.0 <= nota <= 10.0:
                notas.append(nota)
                break
            else:
                print("Nota fora do intervalo permitido.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

# Processamento dos dados
media = sum(notas) / len(notas)
maior = max(notas)
menor = min(notas)
acima_da_media = [n for n in notas if n > media]

# Exibição dos Resultados
print(f"\n--- Análise das Notas ---")
print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
print(f"Média da turma: {media:.2f}")
print(f"Quantidade acima da média: {len(acima_da_media)}")

# Classificação final 
if media >= 7.0:
    print("Classificação: Aprovado")
elif media >= 5.0:
    print("Classificação: Recuperação")
else:
    print("Classificação: Reprovado")

    