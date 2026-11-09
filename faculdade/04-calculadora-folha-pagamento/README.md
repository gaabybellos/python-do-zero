# Tarefa 04 — Calculadora Modular de Folha de Pagamento com Testes (`PYZ-FAC-004`)

Esta pasta reúne **todo o material da Tarefa 04 da faculdade**, focada em **Funções Puras (`def` + `return`), Type Hints, Separação de Responsabilidades (Clean Code) e Testes Automatizados com `pytest` (QA)**.

---

## 📂 O que tem em cada subpasta?

```text
04-calculadora-folha-pagamento/
├── README.md                                      # Este guia da tarefa (estrutura e como executar)
├── 01-enunciado/
│   └── enunciado.md                               # Enunciado original e faixas de desconto
├── 02-estudo-e-explicacao/                        # MATERIAL DE ESTUDO (Não enviar ao professor)
│   ├── explicacao-detalhada-logica.md             # Explicação de funções puras e testes BVA
│   └── codigo_comentado_aula.py                   # Código comentado linha por linha
└── 03-entrega-professor/                          # PASTA LIMPA PRONTA PARA ENVIAR AO PROFESSOR
    ├── calculadora_folha_pagamento.py             # Código principal modularizado
    └── test_calculadora_folha_pagamento.py        # Suíte de testes automatizados (pytest)
```

---

## ▶️ Como Executar o Código e os Testes

Abra o terminal na raiz do repositório (`python-do-zero`):

### 1. Executar o programa interativo no terminal:
```powershell
python faculdade/04-calculadora-folha-pagamento/03-entrega-professor/calculadora_folha_pagamento.py
```

### 2. Executar a suíte de testes automatizados (`pytest`):
```powershell
pytest faculdade/04-calculadora-folha-pagamento/03-entrega-professor/test_calculadora_folha_pagamento.py -v
```
