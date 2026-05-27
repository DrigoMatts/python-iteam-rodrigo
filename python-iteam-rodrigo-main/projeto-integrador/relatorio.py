def exibir_resultado(candidatos):
    print("\n--- RESULTADO DA VOTAÇÃO ---")
    for c in candidatos.values():
        print(f"{c.nome} ({c.partido}) - Número: {c.numero} - Votos: {c.votos}")