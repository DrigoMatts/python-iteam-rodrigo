# Explicação — Desafio 07 — Bio-Calculadora

**Aluno:** _(RodrigoMatosGomes)_
**Data:** _(26/05/2026)_

---

## O que meu programa faz

_(Descreva em suas palavras o que cada parte do código faz.)_

### R: E um sistema modularizado de cálculos matemáticos. O arquivo (funcoes_mat.py)ele funciona como uma biblioteca pessoal. Ele contém a lógica matemática para três cálculos específicos: Área do círculo,volume da esfera e hipotenusa cada função deve ter uma "docstring".(solucao.py) ele é a interface ele exibe um menu para o user escolher qual cálculo deseja realizar,ele solicita os dados ao usuário,processa e exibe o resultado.
---

## Resposta à Pergunta Obrigatória

> Por que separar as funções em um arquivo diferente do `solucao.py`? O que muda no projeto quando você tem 50 funções em vez de 3?

_(Sua resposta aqui — use suas próprias palavras.)_

### R: Porque separação "modularização" serve para organizar o código, facilitando a manutenção e a leitura. Ao isolar a lógica matemática em funcoes_mat.py, o arquivo principal solucao.py foca apenas na interação com o usuário.1-Escalabilidade, com muitas funções em um único arquivo, a navegação e a busca por erros se tornariam caóticas. Outros projetos poderiam importar funcoes_mat.py sem carregar a interface de usuário do solucao.py.

---

## Dificuldades encontradas

_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_

### R: Foi passar os valores capturados no input() (main) como argumentos para os parâmetros das funções para o outro arquivo. E a outra foi diferenciar quando usar import funcoes_mat (exige o prefixo funcoes_mat.area_circulo) ou from funcoes_mat import area_circulo.
