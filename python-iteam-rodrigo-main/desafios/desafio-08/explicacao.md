# Explicação — Desafio 08 — Banco Digital

**Aluno:** _(RodrigoMatosGomes)_
**Data:** _(27/05/2026)_

---

## O que meu programa faz

_(Descreva em suas palavras o que cada parte do código faz.)_

### R: O programa simula o funcionamento básico de uma conta bancária utilizando POO. Ele gerencia dados o programa inicializa uma conta com o nome do titular e um saldo inicial, utizila um atributo de instância (self.saldo) para que o valor dinheiro permaneça na conta enquanto o objeto existir. O programa permite adicionar valores ao saldo atual, permite retirar dinheiro mas possui uma regra de segurança(Obs:o programa impede a operação caso o valor do saques seja maior que o saldo disponível.) e por fim, ele exibe o status atual da conta.

---

## Resposta à Pergunta Obrigatória

> Por que `saldo` deve ser um **atributo da instância** (`self.saldo`) e não uma variável comum dentro do método? O que mudaria no comportamento do programa?

_(Sua resposta aqui — use suas próprias palavras.)_
### R: Porque ele representa o estado do objeto, atributos de instância permitem que o dado seja persistido e acessado por diferentes métodos da classe durante todo o ciclo de vida do objeto. Se o "saldo" fosse uma variável comum, o valor seria esquecido assim que o método terminasse de executar. Não seria possivel manter um historico acumulativo do saldo da conta, cada operação começaria do zero ou falharia.

---

## Dificuldades encontradas

_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_

### R: O que eu achei estopim foi criar uma lógica de saldo como limites,transações algo que é muito complexo ainda mais salvar os dados nesse bloco. Pesquisei sistemas/lógica de dados bancário no youtube.
