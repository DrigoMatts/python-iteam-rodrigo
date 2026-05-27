# Desafio 08 — Banco Digital
# Aluno: RodrigoMatosGomes
# Data:  27/05/2026

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado.")
        else:
            print("Saldo insuficiente para o saque.")

    def exibir_extrato(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo atual: R${self.saldo:.2f}")
