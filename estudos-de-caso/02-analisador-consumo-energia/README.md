# Estudo de Caso 02 — Analisador de Consumo e Tarifa de Energia (`PYZ-CASE-002`)

> **Aviso de Integridade:** Estudo de caso fictício e autoral criado exclusivamente para aprendizado. Não corresponde a uma avaliação acadêmica real e não deve ser submetido como trabalho escolar ou universitário.

Esta pasta reúne o material do **Estudo de Caso 02**, focado em **Laços (`while` e `for`), Tarifação Fictícia por Faixas, Variáveis Acumuladoras, Extremos (`maior`/`menor`) e Validação de Entradas (QA)**.

---

## 📂 O que há em cada subpasta?

```text
02-analisador-consumo-energia/
├── README.md                                  # Guia do caso (estrutura e como executar)
├── 01-enunciado/
│   └── enunciado.md                           # Requisitos fictícios e faixas de cálculo
├── 02-estudo-e-explicacao/                    # Material de estudo detalhado
│   ├── explicacao-detalhada-logica.md         # Explicação passo a passo e Teste de Mesa (BVA)
│   └── codigo_comentado_aula.py               # Código comentado bloco a bloco
└── 04-solucao-referencia/                     # Solução de referência e testes pytest
    ├── analisador_consumo_energia.py          # Implementação limpa seguindo a PEP 8
    └── test_analisador_consumo_energia.py     # Suíte de testes automatizados (pytest)
```

---

## ▶️ Como Executar o Código e os Testes

```powershell
# Executar o programa interativo
python estudos-de-caso/02-analisador-consumo-energia/04-solucao-referencia/analisador_consumo_energia.py

# Executar os testes automatizados (pytest)
pytest estudos-de-caso/02-analisador-consumo-energia/04-solucao-referencia/test_analisador_consumo_energia.py -v
```
