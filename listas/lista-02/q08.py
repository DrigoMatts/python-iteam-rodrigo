# Lista 02 — Questão 08: Herança e Polimorfismo
# Aluno: (RodrigoMatosGomes)
# Data:  (28/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Implemente:
#   - Funcionario(nome, salario): calcular_bonus() → 10% do salário
#   - Gerente(departamento): bônus = 20%
#   - Estagiario(curso): bônus = 5%
# Crie lista com objetos dos 3 tipos, itere exibindo nome e bônus.
# Explique em comentário: por que o Python chama a versão correta de
# calcular_bonus() sem você verificar o tipo do objeto?

# ── Sua solução abaixo ──────────────────────────────────────────────────────
### R: O Python chama a versão correta de calcular_bonus() devido ao POLIMORFISMO, o interpretador verifica a instância real do objeto.
# Como as subclasses (Gerente e Estagiario) sobrescrevem o método da classe pai, 
# o Python decide em tempo de execução (Dynamic Dispatch) qual método executar 
# baseando-se na classe real do objeto, e não no tipo da variável que o contém.
# E mesmo que ele esteja dentro de uma lista genérica de funcionários. Isso permite tratar objetos diferentes de maneira uniforme.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.10

class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def calcular_bonus(self):
        return self.salario * 0.20

class Estagiario(Funcionario):
    def __init__(self, nome, salario, curso):
        super().__init__(nome, salario)
        self.curso = curso

    def calcular_bonus(self):
        return self.salario * 0.05

# Criando a lista com os objetos
funcionarios = [
    Gerente("Alice", 5000, "TI"),
    Estagiario("Bruno", 1500, "Engenharia"),
    Funcionario("Carlos", 3000)
]

# Iterando e exibindo nome e bônus
for f in funcionarios:
    print(f"Nome: {f.nome} | Bônus: R$ {f.calcular_bonus():.2f}")


