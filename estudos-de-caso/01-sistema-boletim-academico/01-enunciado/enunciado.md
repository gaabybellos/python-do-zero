# Estudo de Caso 01 — Sistema de Fechamento de Boletim (`PYZ-CASE-001`)

> **Aviso de Integridade:** Estudo de caso fictício e autoral criado exclusivamente para aprendizado. Não corresponde a uma avaliação acadêmica real e não deve ser submetido como trabalho escolar ou universitário.

## Requisitos do Problema Fictício

Desenvolva um algoritmo em Python que processe o boletim de **cinco (5) estudantes** de um curso técnico fictício. Para cada estudante, o programa deve ler e validar:

1. **Nota do Projeto Prático 1 (`PP1`):** intervalo `[0.0, 2.0]` pontos;
2. **Nota do Projeto Prático 2 (`PP2`):** intervalo `[0.0, 3.0]` pontos;
3. **Nota da Avaliação Teórica (`AT`):** intervalo `[0.0, 5.0]` pontos;
4. **Percentual de Frequência (`FREQ`):** intervalo `[0.0, 100.0]` por cento;
5. **Nota do Exame Substitutivo (`EXAME`):** intervalo `[0.0, 10.0]` pontos *(solicitada **apenas** se o estudante tiver frequência suficiente e ficar em recuperação por nota)*.

### Regras de Cálculo e Situação Final

- **Nota Semestral (`NS`):**
  $$\text{NS} = \text{PP1} + \text{PP2} + \text{AT}$$
  *(Pontuação máxima = $2.0 + 3.0 + 5.0 = 10.0$ pontos).*

- **Critérios de Aprovação, Recuperação e Reprovação:**
  1. **Reprovado por Falta (Direto):** Se `FREQ < 75.0%`, o estudante está **Reprovado por Falta** independentemente da nota (não realiza Exame Substitutivo).
  2. **Aprovado Direto:** Se `FREQ >= 75.0%` e `NS >= 7.0`, o estudante está **Aprovado (Direto)**.
  3. **Reprovado por Nota (Direto):** Se `FREQ >= 75.0%` e `NS < 4.0`, o estudante está **Reprovado por Nota (Direto)** sem direito ao Exame Substitutivo.
  4. **Em Exame Substitutivo (Recuperação):** Se `FREQ >= 75.0%` e `4.0 <= NS < 7.0`, o programa lê a nota do **Exame Substitutivo `[0.0, 10.0]`** e calcula a **Média Final (`MF`)**:
     $$\text{MF} = \frac{\text{NS} + \text{EXAME}}{2}$$
     - Se `MF >= 5.0` $\rightarrow$ **Aprovado (Apos Exame)**;
     - Caso contrário (`MF < 5.0`) $\rightarrow$ **Reprovado por Nota (Apos Exame)**.

### Saídas Esperadas

- Para cada estudante: exibir a `Nota Semestral`, a `Frequência`, a `Média Final` (se fez exame) e a `Situação Final`.
- Ao final dos 5 estudantes: exibir a quantidade e o percentual (`%`) de estudantes **Aprovados**, **Reprovados por Nota** e **Reprovados por Falta**.
