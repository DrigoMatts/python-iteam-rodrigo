# Explicação — Desafio 06 — Bio-Cadastro

**Aluno:** _(RodrigoMatosGomes)_
**Data:** _(25/05/2026)_

---

## O que meu programa faz

_(Descreva em suas palavras o que cada parte do código faz.)_

### R:Ele é um sistema simples de cadastro de funcionários. Ele cria uma lista vazia chamada equipe. Ele entra em um laço de repetição (while) que solicita continuamente o nome e o cargo de novos colaboradores. Para cada colaborador, o programa cria um dicionário (armazenando as informações de forma estruturada) e o adiciona à lista principal. O loop para quando você digita "sair". Nesse momento, o programa percorre a lista e imprime todos os nomes e cargos cadastrados no formato: "Funcionário: {nome} | Cargo: {cargo}".

---

## Resposta à Pergunta Obrigatória

> Por que usamos um **dicionário** para cada funcionário e não uma lista com dois itens como `["Ricardo", "Dev"]`? Qual é a desvantagem de `funcionario[0]` comparado a `funcionario["nome"]`?

_(Sua resposta aqui — use suas próprias palavras.)_

### R: Porque ele atribui um significado semântico aos dados através de chaves ("nome", "Dev").Ao usar funcionario["nome"], o código é autoexplicativo. Qualquer pessoa que leia o código entende. A desvantagem é o uso de funcionario["valor"] é arriscado porque depende estritamente da ordem dos elementos. Se a estrutura da lista mudar no futuro (ex: adicionar "idade" antes do nome), todos os acessos via índice ([0], [1]) quebrariam ou retornariam dados errados.

---

## Dificuldades encontradas

_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_

### R: Para mim foi estruturar o laço while com a condição de parada correta e garantir que o dicionário seja criado e limpo a cada repetição. Porque ele cria um "objeto" novo (o dicionário) e o "pendura" na lista principal, pesquisei no youtube como estrutura o while.