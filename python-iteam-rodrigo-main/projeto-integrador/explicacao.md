## Resposta à Pergunta Obrigatória

> Responda às três perguntas abaixo (cada uma em um parágrafo):
1. Como a herança ou dicionários facilitaram o cadastro de candidatos na sua solução?
2. Como você garantiu que o voto permanecesse anônimo e seguro?
3. Qual foi o maior obstáculo técnico que você superou e como resolveu?

### R: 
1. O uso de dicionários facilitou significativamente o cadastro e a contagem, pois permitiu associar diretamente o número do candidato (chave) ao seu respectivo nome e à contagem de votos (valor). Isso elimina a necessidade de percorrer listas extensas para buscar um candidato, tornando a operação de votar muito mais performática e o código mais legível.

2. O anonimato foi garantido pelo fato de o sistema processar apenas a contagem numérica dos votos dentro do dicionário, sem armazenar ou vincular qualquer identificador pessoal do eleitor à escolha feita. A segurança é mantida através da validação da entrada, que só aceita números previamente definidos no dicionário, descartando automaticamente qualquer entrada inválida.

3. O maior obstáculo foi a implementação da lógica de apuração com cálculo de percentuais, garantindo que o programa não tentasse dividir por zero caso nenhum voto fosse computado. Resolvi isso utilizando uma estrutura condicional ternária para verificar se o total_votos era maior que zero antes de realizar o cálculo, garantindo a robustez do relatório final.