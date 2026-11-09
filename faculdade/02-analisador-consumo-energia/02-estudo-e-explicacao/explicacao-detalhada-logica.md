# Explicação Detalhada — Analisador de Consumo de Energia (`PYZ-FAC-002`)

## Identificação da Tarefa

- **ID:** `PYZ-FAC-002`
- **Disciplina / Tema:** Acumuladores, Extremos (`maior`/`menor`), Faixas Progressivas e Validação de Texto/Número
- **Pasta da Tarefa:** `faculdade/02-analisador-consumo-energia/`

---

## 1. Decomposição E-P-S e Lógica dos Extremos (`maior` e `menor`)

- **Diferença entre Contador e Acumulador:**
  - **Contador** soma sempre um valor fixo (`+ 1` a cada imóvel).
  - **Acumulador** soma um valor variável (`soma_consumo += consumo_kwh` e `faturamento_total += valor_fatura`).
- **Como descobrir o Maior e o Menor valor sem usar listas:**
  - Inicializamos `maior_consumo = None` e `menor_consumo = None`.
  - No 1º imóvel (`is None`), ambos recebem o consumo daquele primeiro imóvel.
  - Nos imóveis seguintes, comparamos se o novo `consumo_kwh > maior_consumo` ou `< menor_consumo`.

---

## 2. Teste de Mesa com Análise de Valor Limite (QA — BVA)

| Caso de Teste | Consumo (`kWh`) | Tipo | Faixa | Cálculo Esperado | Fatura (`R$`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Borda Social Residencial** | `100.0` | `'r'` $\rightarrow$ `'R'` | Social | `(100 * 0.50) * 0.90` | `R$ 45.00` |
| **2. Borda Social Comercial** | `100.0` | `'C'` | Social | `100 * 0.50` *(sem desconto)* | `R$ 50.00` |
| **3. Borda Moderada** | `200.0` | `'R'` | Moderada | `(200 * 0.75) + 15.00` | `R$ 165.00` |
| **4. Acima de 300 kWh** | `400.0` | `'C'` | Elevada | `(400 * 0.95) + 35.00` | `R$ 415.00` |
