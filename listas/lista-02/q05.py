# Lista 02 — Questão 05: Funções de Alta Ordem
# Aluno: (RodrigoMatosGomes)
# Data:  (27/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Em q05.py: escreva aplicar(lista, funcao) que retorna uma nova lista com a
# função aplicada a cada elemento. Demonstre com:
#   (a) função que eleva ao quadrado
#   (b) função que retorna True se o número for par
# 
# Em q05_resposta.txt: explique o que significa dizer que funções são
# 'cidadãs de primeira classe' em Python.

# ── Sua solução abaixo ──────────────────────────────────────────────────────
### R: Dizer que as funções são cidadãs em python significa que elas são tratadas como qualquer outro objeto na linguagem,para outras funções onde passamos a lógica do quadrado para a função "def aplicar" abaixo.
### Elas também podem ser retornadas por outras funções,atribuidas a variáveis e serem armazenadas em estrutura de dados como as listas e discionários.

def aplicar(lista, funcao):
    # Retorna uma nova lista com a função aplicada a cada elemento
    nova_lista = []
    for item in lista:
        nova_lista.append(funcao(item))
    return nova_lista

numeros = [1, 2, 3, 4, 5]

# (a) Função que eleva ao quadrado
quadrado = aplicar(numeros, lambda x: x ** 2)
print(f"Quadrados: {quadrado}")

# (b) Função que retorna True se o número for par
eh_par = aplicar(numeros, lambda x: x % 2 == 0)
print(f"É par? {eh_par}")
