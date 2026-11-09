# Estudo de Caso 02 — Analisador de Consumo de Energia Elétrica (`PYZ-CASE-002`)

> **Aviso de Integridade:** Estudo de caso fictício e autoral criado exclusivamente para aprendizado. Não corresponde a uma avaliação acadêmica real e não deve ser submetido como trabalho escolar ou universitário.

## Requisitos do Problema Fictício

Construa um programa em Python para analisar as leituras fictícias de consumo elétrico (em kWh) de um conjunto de imóveis. O usuário deverá informar a quantidade de imóveis a serem analisados (mínimo `1` e máximo `50`).

Para cada imóvel, leia:
- **Consumo mensal em kWh:** valor decimal `>= 0.0`.
- **Tipo de instalação:** `'R'` (Residencial) ou `'C'` (Comercial) — aceitando letras maiúsculas ou minúsculas.

### Regras Fictícias de Tarifação por Faixa

1. **Consumo Social (Isento de Bandeira):** Até `100.0 kWh` $\rightarrow$ Tarifa base de **R\$ 0,50 por kWh** (sem taxa extra).
2. **Consumo Moderado:** Acima de `100.0 kWh` até `300.0 kWh` $\rightarrow$ Tarifa base de **R\$ 0,75 por kWh** + **Taxa de Bandeira Amarela de R\$ 15,00**.
3. **Consumo Elevado:** Acima de `300.0 kWh` $\rightarrow$ Tarifa base de **R\$ 0,95 por kWh** + **Taxa de Bandeira Vermelha de R\$ 35,00**.
4. **Desconto de Incentivo Residencial:** Imóveis do tipo `'R'` com consumo até `100.0 kWh` recebem **10% de desconto** sobre o valor da conta.

### Saídas Esperadas

- Para cada imóvel: mostrar o consumo em kWh, a faixa tarifária aplicada e o valor final da fatura em `R$`.
- Ao final de todos os imóveis: exibir a **média de consumo (kWh)**, o **maior** e o **menor** consumo (kWh) registrados e o **faturamento total (`R$`)**.
