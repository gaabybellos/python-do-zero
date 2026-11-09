# Tarefa de Faculdade 02 — Analisador de Consumo de Energia Elétrica (`PYZ-FAC-002`)

## Enunciado do Problema

**DESCRIÇÃO: SIMULADOR DE FATURAMENTO DE ENERGIA POR FAIXAS DE CONSUMO**

Construa um programa em Python para analisar as leituras de consumo elétrico (em kWh) de uma rua. O usuário deverá informar a quantidade de imóveis a serem analisados (mínimo `1` e máximo `50`).

Para cada imóvel, leia:
- **Consumo mensal em kWh:** valor decimal `>= 0.0`.
- **Tipo de instalação:** `'R'` (Residencial) ou `'C'` (Comercial) — aceitando letras maiúsculas ou minúsculas.

### Regras de Tarifação por Faixa de Consumo

1. **Consumo Social (Isento de Bandeira):** Até `100.0 kWh` $\rightarrow$ Tarifa base de **R\$ 0,50 por kWh** (sem taxa extra).
2. **Consumo Moderado:** Acima de `100.0 kWh` até `300.0 kWh` $\rightarrow$ Tarifa base de **R\$ 0,75 por kWh** + **Taxa de Bandeira Amarela de R\$ 15,00**.
3. **Consumo Elevado:** Acima de `300.0 kWh` $\rightarrow$ Tarifa base de **R\$ 0,95 por kWh** + **Taxa de Bandeira Vermelha de R\$ 35,00**.
4. **Desconto de Incentivo Residencial:** Imóveis do tipo `'R'` com consumo até `100.0 kWh` recebem **10% de desconto** sobre o valor da conta.

### Saídas Exigidas

- Para cada imóvel: mostrar o consumo em kWh, a faixa tarifária aplicada e o valor final da fatura em `R$`.
- Ao final de todos os imóveis:
  - A **média de consumo (kWh)** dos imóveis avaliados;
  - O **maior** e o **menor** consumo (kWh) registrados;
  - O **faturamento total (`R$`)** arrecadado pela concessionária.
