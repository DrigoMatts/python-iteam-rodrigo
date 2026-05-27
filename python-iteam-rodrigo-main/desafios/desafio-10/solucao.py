# Desafio 10 — Projeto Final — Urna Eletrônica
# Aluno: RodrigoMatosGomes
# Data:  27/05/2026

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
# class UrnaEletronica:
#     def __init__(self):
#         # Dicionário facilita a busca: {número: nome}
#         self.candidatos = {
#             "13": "Candidato A",
#             "22": "Candidato B",
#             "00": "Voto em Branco"
#         }
#         self.votos = {numero: 0 for numero in self.candidatos}
#         self.total_votos = 0

#     def exibir_candidatos(self):
#         print("\n--- Candidatos Disponíveis ---")
#         for num, nome in self.candidatos.items():
#             print(f"[{num}] {nome}")

#     def votar(self):
#         while True:
#             self.exibir_candidatos()
#             voto = input("\nDigite o número do candidato (ou 'fim' para encerrar): ").strip()

#             if voto.lower() == 'fim':
#                 break

#             if voto in self.votos:
#                 self.votos[voto] += 1
#                 self.total_votos += 1
#                 print("VOTO CONFIRMADO!")
#             else:
#                 print("NÚMERO INVÁLIDO! Voto não computado.")

#     def apurar_resultados(self):
#         print("\n--- Resultado da Apuração ---")
#         for num, qtd in self.votos.items():
#             percentual = (qtd / self.total_votos * 100) if self.total_votos > 0 else 0
#             print(f"{self.candidatos[num]}: {qtd} votos ({percentual:.2f}%)")
#         print(f"Total de votos: {self.total_votos}")

# if __name__ == "__main__":
#     urna = UrnaEletronica()
#     urna.votar()
#     urna.apurar_resultados()
