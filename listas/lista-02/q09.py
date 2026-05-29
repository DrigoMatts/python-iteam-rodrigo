# Lista 02 — Questão 09: Encapsulamento e Propriedades
# Aluno: (seu nome)
# Data:  (data)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Em q09.py — classe Produto com:
#   1. __preco via @property com validação (preço > 0)
#   2. __estoque com getter, repor(qtd) e vender(qtd) — ValueError se sem estoque
#   3. __str__ informativo e __repr__ para debug
# Demonstre: criação, vendas, reposição e tentativa de venda além do estoque.
# 
# Em q09_resposta.txt: explique a diferença entre _atributo e __atributo em Python.

# ── Sua solução abaixo ──────────────────────────────────────────────────────

### R: 
class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.__estoque = estoque

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        self.__preco = valor

    @property
    def estoque(self):
        return self.__estoque

    def repor(self, qtd):
        self.__estoque += qtd

    def vender(self, qtd):
        if qtd > self.__estoque:
            raise ValueError("Saldo insuficiente em estoque.")
        self.__estoque -= qtd

    def __str__(self):
        return f"Produto: {self.nome} | Preço: R${self.preco:.2f} | Estoque: {self.estoque}"

    def __repr__(self):
        return f"Produto(nome='{self.nome}', preco={self.preco}, estoque={self.estoque})"

# --- Demonstração ---
try:
    p1 = Produto("Notebook", 3500.00, 10)
    print(f"Criação: {p1}")

    p1.vender(3)
    print(f"Venda de 3 unidades: {p1.estoque} restantes")

    p1.repor(5)
    print(f"Reposição de 5 unidades: {p1.estoque} no total")

    print("Tentativa de venda além do estoque...")
    p1.vender(20)
except ValueError as e:
    print(f"Erro: {e}")
