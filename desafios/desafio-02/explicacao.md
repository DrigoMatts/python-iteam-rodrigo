# Explicação — Desafio 02 — Calculadora de IMC

**Aluno:** _RodrigoMatosGomes_
**Data:** _(19/05/2026)_

---

## O que meu programa faz

_(Descreva em suas palavras o que cada parte do código faz.)_

### R: Entrada de dados, O programa solicita que o usuário digite o peso e a altura através do comando input().
### Conversão de tipos: Converte os dados recebidos (que inicialmente são texto) para números decimais utilizando float().
### Cálculo: Realiza a fórmula do IMC (\(peso / altura^2\)) e armazena o resultado em uma variável.
### Saída: Exibe o valor do IMC calculado na tela.

---

## Resposta à Pergunta Obrigatória

> Por que é necessário usar `float()` ao capturar peso e altura com `input()`? O que aconteceria se usássemos `int()` para a altura `1.75`?

_(Sua resposta aqui — use suas próprias palavras.)_

### R: Uso de float(): A função input() sempre captura o dado como uma string (texto). Como peso e altura geralmente envolvem números decimais (ex: 70.5 kg, 1.75 m), preciso converter esse texto para um formato numérico que aceite casas decimais, o que o tipo float (ponto flutuante) realiza. Uso do int(): Se usássemos int() (inteiro) para a altura 1.75, o programa geraria um erro (ValueError), pois o Python não consegue converter diretamente uma string contendo um ponto decimal ("1.75") para um número inteiro. Se ele tentasse truncar o valor para 1, o cálculo do IMC ficaria incorreto, perdendo a precisão necessária para o cálculo.

---

## Dificuldades encontradas

_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_

### R: A conversão de tipos por que o input() sempre retorna um texto (string) e por que precisamos transformar isso em float() (números decimais) para fazer "cálculos matemáticos". E tive que pesquisar como eu aplico a fórmula IMC no código que foi uma parte que eu achei díficil.
