# Explicação Detalhada — Calculadora de Folha de Pagamento (`PYZ-CASE-004`)

> **Aviso de Integridade:** Estudo de caso fictício e autoral criado exclusivamente para aprendizado. Não corresponde a uma avaliação acadêmica real e não deve ser submetido como trabalho escolar ou universitário.

## Identificação do Caso

- **ID:** `PYZ-CASE-004`
- **Tema:** Modularização em Funções Puras, Tratamento de Exceções (`ValueError`) e Testes Automatizados (`pytest`)
- **Pasta do Caso:** `estudos-de-caso/04-calculadora-folha-pagamento/`

---

## 1. Por que Separar Funções de Cálculo do `input()` e `print()`?

Quando isolamos a matemática em funções puras (`calcular_valor_horas_extras`, `calcular_desconto_previdenciario`, `calcular_auxilio_dependentes`), conseguimos criar o arquivo `test_calculadora_folha_pagamento.py` e testar automaticamente dezenas de cenários em milissegundos usando o **`pytest`**, sem precisar digitar nada manualmente no teclado.

---

## 2. Casos de Teste Automatizados (QA — BVA e Testes Negativos)

| Função Testada | Entrada | Saída Esperada | Técnica de QA |
| :--- | :--- | :--- | :--- |
| `calcular_valor_horas_extras` | `salario=2200.0`, `horas=10.0` | `R$ 150.00` | Partição de Equivalência Válida |
| `calcular_desconto_previdenciario` | `bruto=2000.00` / `4500.00` / `5000.00` | `160.00` / `495.00` / `700.00` | Análise de Valor Limite (BVA) |
| `calcular_auxilio_dependentes` | `salario=3500.00` vs `3500.01` (`2 dep`) | `300.00` vs `0.00` | Análise de Valor Limite (BVA) |
| `calcular_valor_horas_extras` | `salario=0.0` ou `horas=-1.0` | `raises ValueError` | Teste Negativo (Exceção Esperada) |
