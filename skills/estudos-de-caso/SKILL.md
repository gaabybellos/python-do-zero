---
name: estudos-de-caso
description: Estruturar estudos de caso autorais e fictícios em pastas unificadas contendo README, 01-enunciado, 02-estudo-e-explicacao e 04-solucao-referencia com testes automatizados pytest.
---

# Estudos de Caso Autorais e Fictícios (`estudos-de-caso`)

## Propósito

Oferecer problemas integradores autorais e fictícios que conectam **Lógica de Programação, Clean Code (PEP 8) e Engenharia de Qualidade (QA-First)**.

> **Regra de Integridade:** Todos os estudos de caso são fictícios, autorais e criados exclusivamente para aprendizado. Não correspondem a avaliações acadêmicas reais e não devem ser submetidos como trabalhos escolares ou universitários.

---

## Estrutura Obrigatória de Pastas (`estudos-de-caso/<NN-nome-do-caso>/`)

Todo estudo de caso recebe um identificador `PYZ-CASE-<NUMERO>` e sua própria pasta dentro de `estudos-de-caso/`:

```text
estudos-de-caso/
├── README.md                                      # Índice geral dos estudos de caso
└── <NN-nome-do-caso>/                             # Pasta única do estudo de caso
    ├── README.md                                  # Objetivo, mapa de subpastas e como executar
    ├── 01-enunciado/                              # Requisitos fictícios e critérios de aceite
    │   └── enunciado.md
    ├── 02-estudo-e-explicacao/                    # Decomposição E-P-S, BVA e versão comentada
    │   ├── explicacao-detalhada-logica.md
    │   └── codigo_comentado_aula.py
    └── 04-solucao-referencia/                     # Implementação de referência e suíte pytest
        ├── <nome_do_script>.py
        └── test_<nome_do_script>.py
```
