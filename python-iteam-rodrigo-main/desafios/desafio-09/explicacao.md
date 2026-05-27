# Explicação — Desafio 09 — Sistema de Frota

**Aluno:** _(RodrigoMatosGomes)_
**Data:** _(27/05/2026)_

---

## O que meu programa faz

_(Descreva em suas palavras o que cada parte do código faz.)_

### R: E um programa que simula um sistema de gestão de frota de veículos utilizando POO. Ele organiza/agrupa diferentes tipos de transportes sob uma estrutura comum. A Herança (função Pai= veículos),cria uma base comum para evitar repetição de código. Caminhão e Moto herdam os atributos de marca e ano, cada veículo sabe exibir seus próprio dados de forma específica através do método exibir_dados(). 

---

## Resposta à Pergunta Obrigatória

> Por que `Caminhao` e `Moto` 'herdam de' `Veiculo` e não simplesmente repetem os atributos? O que você ganha e o que arrisca ao usar herança?

_(Sua resposta aqui — use suas próprias palavras.)_

### R: Porque o caminhão e Moto herdem de veículo para evitar a duplicação de código, os dois compartilham características fundamentais como (Marca,ano,quilometragem), a herança permite que você defina essa lógica apenas uma vez na classe pai. O que eu ganho?bom,se eu precisar alterar como quilomentragem é calculada,altera apenas em veículo e todas as outras subclasses são atualizadas automaticamente. E eu posso tratar diferentes objetos (ex: Moto e caminhão) sendo "veículos", facilitando a criação de listas. Agora se eu for arriscar as mudanças na classe "pai" podem quebrar ou causar erro em todas as classes de filhos. A hierarquia de herança pode se tornar confusa ou forçada.

---

## Dificuldades encontradas

_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_

### R: Eu achei esse conteúdo tanto na sala de aula,quanto aqui muito chato de fazer/entender. Eu tive que pesquisar oque,porque e até usar I.A para me ajudar na lógica de exibir os dados porque eles estavam de alguma foram se "unindo", porque o uso correto do super() dentro das classes filhas para imprimir marca eo ano que pertencem a função pai e,adicionar a impressão de atributos específicos como a capacidade_carga e cilindradas.
