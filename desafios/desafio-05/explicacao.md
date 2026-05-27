# Explicação — Desafio 05 — Gerenciador de Compras

**Aluno:** _(RodrigoMatosGomes)_
**Data:** _(22/05/2026)_

---

## O que meu programa faz

_(Descreva em suas palavras o que cada parte do código faz.)_

### R: a variável compras ela armazena os itens que você digita/escreve, o whle true faz com que o programa continue repetindo infinitamente até que você de o comando para parar. A cada rodada ele coleta os dados e pergunta o nome de um produto. Se você digitar "Fim" o comando break encerra o laço. Se não for "fim",ele adiciona o nome à lista (Compras) usando o .append(). Quando o loop termina o comando compras.sort() coloca os itens em ordem alfabética, e por final ele imprime a lista completa e o total de itens que foram adicionados utilizando o len.

---

## Resposta à Pergunta Obrigatória

> Por que usamos uma **lista** e não uma **tupla** para essa lista de compras? O que mudaria no comportamento do programa se tentássemos usar tupla?

_(Sua resposta aqui — use suas próprias palavras.)_

### R: Usamos uma lista porque ela é alterável, o que nos permite adicionar novos elementos dinamicamente enquanto o programa está rodando usando append()
### se eu tentasse usar uma tupla para o Gerenciador de Compras, o programa apresentaria um erro e pararia de funcionar, Tuplas são imutáveis, o que significa que não podem ser alteradas depois de criadas. Como o objetivo do desafio é construir a lista dinamicamente conforme o usuário digita os produtos, a tupla é inadequada. Uma vez criada vazia (), ela permaneceria vazia.

---

## Dificuldades encontradas

_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_

### R: Para adicionar itens a uma tupla, eu seria forçado a "recriar" a tupla inteira a cada novo produto (ex: tupla = tupla + (novo_item,)), o que é muito menos eficiente e menos intuitivo do que simplesmente usar uma lista, que foi feita para crescer dinamicamente.