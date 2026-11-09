# Central de Tarefas e Trabalhos da Faculdade (`faculdade/`)

Esta pasta reúne **exemplos completos e reais de tarefas acadêmicas de programação em Python**, organizadas de forma progressiva (do básico de condicionais e laços até coleções, funções puras e testes automatizados com `pytest`).

Aqui, **cada tarefa possui a sua própria pasta única** reunindo o enunciado, a explicação passo a passo da lógica (com Análise de Valor Limite de QA), o código comentado para estudo e o código limpo de entrega.

---

## 📂 Estrutura Padrão de Cada Tarefa

```text
faculdade/
├── README.md                                  # Este catálogo geral das tarefas da faculdade
└── <NN-nome-da-tarefa>/                       # Pasta única da tarefa
    ├── README.md                              # Explica o que tem em cada pasta da tarefa e como executar
    ├── 01-enunciado/
    │   └── enunciado.md                       # O pedido original e regras de negócio
    ├── 02-estudo-e-explicacao/                # MATERIAL DE AULA E ESTUDO (Não enviar ao professor)
    │   ├── explicacao-detalhada-logica.md     # Decomposição E-P-S, passo a passo e Teste de Mesa (QA/BVA)
    │   └── codigo_comentado_aula.py           # Código comentado linha por linha
    └── 03-entrega-professor/                  # PASTA LIMPA PRONTA PARA ENVIAR AO PROFESSOR
        └── <arquivo_final>.py                 # Código limpo, com validação defensiva e PEP 8
```

---

## 📋 Catálogo de Tarefas Acadêmicas Resolvidas

| ID | Pasta da Tarefa | Tópicos de Python & Engenharia de Qualidade (QA) | Comando Rápido de Execução |
| :--- | :--- | :--- | :--- |
| `PYZ-FAC-001` | [`01-sistema-boletim-academico/`](./01-sistema-boletim-academico/README.md) | `for`, `while`, `if/elif/else`, contadores, cálculo de porcentagens e validação defensiva de decimais (vírgula/ponto). | `python faculdade/01-sistema-boletim-academico/03-entrega-professor/sistema_boletim_academico.py` |
| `PYZ-FAC-002` | [`02-analisador-consumo-energia/`](./02-analisador-consumo-energia/README.md) | Acumuladores, descoberta de `maior` e `menor` valor, tarifação progressiva por faixas e higienização de strings (`.upper()`). | `python faculdade/02-analisador-consumo-energia/03-entrega-professor/analisador_consumo_energia.py` |
| `PYZ-FAC-003` | [`03-controle-estoque-farmacia/`](./03-controle-estoque-farmacia/README.md) | Menu interativo (`while True`), listas de dicionários (`list[dict]`), unicidade de código e proteção contra estoque negativo. | `python faculdade/03-controle-estoque-farmacia/03-entrega-professor/controle_estoque_farmacia.py` |
| `PYZ-FAC-004` | [`04-calculadora-folha-pagamento/`](./04-calculadora-folha-pagamento/README.md) | Modularização em funções puras (`def`), *Type Hints*, separação de I/O e suíte de testes automatizados com `pytest`. | `pytest faculdade/04-calculadora-folha-pagamento/03-entrega-professor/test_calculadora_folha_pagamento.py` |
