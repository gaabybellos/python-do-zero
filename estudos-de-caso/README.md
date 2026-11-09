# Estudos de Caso Autorais e Fictícios (`estudos-de-caso/`)

> **Aviso de Integridade:** Todos os estudos de caso desta pasta são **fictícios, autorais e criados exclusivamente para aprendizado**. Não correspondem a avaliações acadêmicas reais e não devem ser submetidos como trabalhos escolares ou universitários.

Esta pasta reúne **4 estudos de caso progressivos** que demonstram como aplicar Lógica de Programação, PEP 8, Programação Defensiva e Testes Automatizados (`pytest`) em problemas completos de console.

---

## 📂 Estrutura Padrão de Cada Estudo de Caso

```text
estudos-de-caso/
├── README.md                                  # Este catálogo geral dos estudos de caso
└── <NN-nome-do-caso>/                         # Pasta única do estudo de caso
    ├── README.md                              # Explica o que há em cada subpasta e como executar
    ├── 01-enunciado/
    │   └── enunciado.md                       # Requisitos fictícios e critérios de aceite
    ├── 02-estudo-e-explicacao/                # Material didático detalhado
    │   ├── explicacao-detalhada-logica.md     # Decomposição E-P-S, passo a passo e Teste de Mesa (QA/BVA)
    │   └── codigo_comentado_aula.py           # Código comentado bloco a bloco para estudo
    └── 04-solucao-referencia/                 # Implementação de referência e testes automatizados
        ├── <arquivo_final>.py                 # Código limpo, com validação defensiva e PEP 8
        └── test_<arquivo_final>.py            # Suíte de testes automatizados (pytest)
```

---

## 📋 Catálogo de Estudos de Caso (`PYZ-CASE`)

| ID | Pasta do Estudo de Caso | Tópicos de Python & Engenharia de Qualidade (QA) | Comando de Execução / Testes |
| :--- | :--- | :--- | :--- |
| `PYZ-CASE-001` | [`01-sistema-boletim-academico/`](./01-sistema-boletim-academico/README.md) | `for`, `while`, `if/elif/else`, contadores, porcentagens e validação defensiva de decimais (vírgula/ponto). | `pytest estudos-de-caso/01-sistema-boletim-academico/04-solucao-referencia/` |
| `PYZ-CASE-002` | [`02-analisador-consumo-energia/`](./02-analisador-consumo-energia/README.md) | Acumuladores, descoberta de `maior` e `menor` valor, tarifação fictícia por faixas e higienização de strings (`.upper()`). | `pytest estudos-de-caso/02-analisador-consumo-energia/04-solucao-referencia/` |
| `PYZ-CASE-003` | [`03-controle-estoque-farmacia/`](./03-controle-estoque-farmacia/README.md) | Menu interativo (`while True`), listas de dicionários (`list[dict]`), unicidade de código e proteção contra estoque negativo. | `pytest estudos-de-caso/03-controle-estoque-farmacia/04-solucao-referencia/` |
| `PYZ-CASE-004` | [`04-calculadora-folha-pagamento/`](./04-calculadora-folha-pagamento/README.md) | Modularização em funções puras (`def`), *Type Hints*, separação de I/O e suíte de testes automatizados com `pytest`. | `pytest estudos-de-caso/04-calculadora-folha-pagamento/04-solucao-referencia/` |
