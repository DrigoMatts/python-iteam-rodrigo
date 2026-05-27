# Explicação — Desafio 10 — Projeto Final — Urna Eletrônica

**Aluno:** _(RodrigoMatosGomes)_
**Data:** _(27/05/2026)_

---

## O que meu programa faz

_(Descreva em suas palavras o que cada parte do código faz.)_

### R: Urna Eletrônica. Ele permite registrar votos para candidatos pré-definidos e, ao final, exibe um relatório com a apuração dos resultados. O programa já começa com candidatos configurados (Candidato A, Candidato B e Voto em Branco) associados a números específicos (13, 22 e 00). O programa ele:Exibe a lista de candidatos na tela,Pede para o usuário digitar o número do candidato,Se o número for válido, o voto é computado. O ciclo de votação continua até que alguém digite a palavra 'fim'. E ele também Calcula a quantidade de votos que cada candidato recebeu e o percentual de votos de cada um em relação ao total no final Exibe o total geral de votos registrados.

---

## Resposta à Pergunta Obrigatória

> Responda às três perguntas abaixo (cada uma em um parágrafo):
1. Como a herança ou dicionários facilitaram o cadastro de candidatos na sua solução?
2. Como você garantiu que o voto permanecesse anônimo e seguro?
3. Qual foi o maior obstáculo técnico que você superou e como resolveu?

_(Sua resposta aqui — use suas próprias palavras.)_

### R: 1* Os dicionários facilitam a busca direta pelo número do candidato(Chave), permitindo acesso instantâneo aos dados sem percorrer listas e a herança permite criar uma classe base do candidato com atributos gerais(nome,partidos e etc) e especializá-la para prefeito ou vereador,evitando a repetição de código e organizando a hierarquia do sistemas. || 2* O anonimato é garantido ao desvincular o registro do eleitor do voto computado, pois o sistemas apenas contabiliza o incremento numérico em uma variável ou banco de dados sem armazenar quem o gerou. A segurança pode ser reforçada através da validação de integridade dos dados e garantindo que o estado da votação só seja alterado por funções. || 3* O maior desafio foi gerenciar o fluxo de telas e a validação de entradas por trás da lógica como (votos nulos ou brancos.) Resolvi isso implementando a estrutura de controle (switch/case e if/else robustos) e tratando exceções para garantir que o sistemas não trave caso o usuário digite um caractere inválido.


---

## Dificuldades encontradas

_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_

### R:
