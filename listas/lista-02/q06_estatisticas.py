# Lista 02 — Questão 06: Módulo de Estatísticas (módulo estatísticas)
# Aluno: (RodrigoMatosGomes)
# Data:  (27/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# q06_estatisticas.py: crie o módulo com as funções:
#   media(dados), mediana(dados), moda(dados), desvio_padrao(dados)
# Todas devem: receber lista de floats, validar que não está vazia
# (lançar ValueError se estiver), retornar resultado arredondado (2 casas).
# Use apenas stdlib (math permitido, não use statistics).
# 
# q06_main.py: importe o módulo e aplique as 4 funções sobre 10 notas
# digitadas pelo usuário.

# ── Sua solução abaixo ──────────────────────────────────────────────────────
## R:

import math

def validar_dados(dados):
    if not dados:
        raise ValueError("A lista de dados não pode estar vazia.")

def media(dados):
    validar_dados(dados)
    res = sum(dados) / len(dados)
    return round(res, 2)

def mediana(dados):
    validar_dados(dados)
    ordenados = sorted(dados)
    n = len(ordenados)
    meio = n // 2
    
    if n % 2 == 0:
        res = (ordenados[meio - 1] + ordenados[meio]) / 2
    else:
        res = ordenados[meio]
    return round(res, 2)

def moda(dados):
    validar_dados(dados)
    contagem = {}
    for item in dados:
        contagem[item] = contagem.get(item, 0) + 1
    
    max_frequencia = max(contagem.values())
    modas = [k for k, v in contagem.items() if v == max_frequencia]
    
    # Retorna a primeira moda encontrada arredondada
    return round(modas[0], 2)

def desvio_padrao(dados):
    validar_dados(dados)
    m = sum(dados) / len(dados)
    variancia = sum((x - m) ** 2 for x in dados) / len(dados)
    res = math.sqrt(variancia)
    return round(res, 2)

