# Mapa de Módulos e Trilha de Aprendizado (`mapa-modulos.md`)

Este documento é a referência oficial de roteamento do repositório **Python do Zero**. Todos os agentes devem consultá-lo antes de criar aulas, documentos de raciocínio lógico ou arquivos de exercícios.

## Estrutura da Trilha

| Prefixo ID | Diretório do Módulo | Tópicos Principais | Referências de Base |
| :--- | :--- | :--- | :--- |
| `PYZ-SEQ` | `modulos/01-introducao-e-variaveis/` | O que é um algoritmo, variáveis, tipos primitivos (`str`, `int`, `float`, `bool`), operadores aritméticos, `input()`, `print()` e f-strings. | *RafaelFino/python-basics*, *Wiki Python Brasil (Estrutura Sequencial)* |
| `PYZ-CND` | `modulos/02-estruturas-condicionais/` | Operadores relacionais (`==`, `!=`, `>`, `<`), operadores lógicos (`and`, `or`, `not`), `if`, `elif`, `else` e condições aninhadas limpas. | *WoMakersCode/intro-ao-python*, *Wiki Python Brasil (Estrutura de Decisão)* |
| `PYZ-REP` | `modulos/03-lacos-de-repeticao/` | Repetição com condição (`while`), contadores e acumuladores, repetição contada (`for` e `range()`), `break`, `continue` e prevenção de loops infinitos. | *30-Days-Of-Python*, *Wiki Python Brasil (Estrutura de Repetição)* |
| `PYZ-COL` | `modulos/04-colecoes-listas-dicionarios/` | Listas (`list`), fatiamento (*slicing*), tuplas (`tuple`), dicionários (`dict`), conjuntos (`set`) e iteração sobre coleções. | *4GeeksAcademy/python-beginner-programming-exercises* |
| `PYZ-FUN` | `modulos/05-funcoes-e-modularizacao/` | Criação de funções (`def`), parâmetros, retorno (`return`), escopo de variáveis, *Docstrings*, *Type Hints*, tratamento de erros (`try/except`) e testes com `pytest`. | *30-Days-Of-Python*, *Clean Code Python* |
| `PYZ-PRJ` | `modulos/06-mini-projetos/` | Projetos práticos de console aplicando todos os conceitos, modularização em múltiplos arquivos e cobertura de testes. | *RafaelFino/python-basics*, *4GeeksAcademy* |
| `PYZ-CASE` | `estudos-de-caso/<NN-nome-do-caso>/` | Casos autorais e fictícios que conectam requisitos, raciocínio, implementação de referência e evidências de QA. | Requisitos originais do projeto |

---

## Convenção de Pastas Dentro de Cada Módulo

Cada diretório em `modulos/<NN-nome-do-modulo>/` segue a seguinte organização:

```text
modulos/<NN-nome-do-modulo>/
├── README.md                 # Índice, objetivos, pré-requisitos e exercícios
├── conteudo-teorico.md       # Aula escrita autossuficiente (Professor)
├── exemplos/                 # Exemplos análogos, nunca a solução do exercício
├── raciocinio/               # Decomposições e Testes de Mesa do aluno (Agente Lógica)
│   └── PYZ-XXX-N1-001.md
├── exercicios/               # Código Python desenvolvido pelo aluno (Agente Desenvolvimento)
│   └── ex001_nome_claro.py
└── revisoes/                 # Relatórios de Code Review e Boas Práticas (Agente Desenvolvimento)
    └── PYZ-XXX-N1-001-review.md
```

As pastas `conteudo-teorico.md`, `exemplos/` e `revisoes/` são publicadas
progressivamente. Um módulo só pode ser marcado como disponível quando possuir
teoria, exemplos, exercícios, testes e ao menos uma revisão completa.
