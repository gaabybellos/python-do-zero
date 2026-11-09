# Explicação Detalhada — Sistema de Boletim Acadêmico (`PYZ-FAC-001`)

## Identificação da Tarefa

- **ID:** `PYZ-FAC-001`
- **Disciplina / Tema:** Estruturas Condicionais Encadeadas (`if/elif/else`), Laços (`for`/`while`), Contadores e Validação Defensiva (QA)
- **Pasta da Tarefa:** `faculdade/01-sistema-boletim-academico/`
- **Subpasta de Estudo:** `faculdade/01-sistema-boletim-academico/02-estudo-e-explicacao/`
- **Subpasta de Entrega:** `faculdade/01-sistema-boletim-academico/03-entrega-professor/`

---

## 1. Entendendo o Problema (Decomposição E-P-S)

- **Entradas:** Para cada um dos 5 estudantes:
  - `nota_pp1` (`[0.0, 2.0]`), `nota_pp2` (`[0.0, 3.0]`), `nota_teorica` (`[0.0, 5.0]`) e `frequencia` (`[0.0, 100.0]`).
  - Condicionalmente: `nota_exame` (`[0.0, 10.0]`) apenas se `frequencia >= 75.0` e `4.0 <= nota_semestral < 7.0`.
- **Processamento:**
  - `nota_semestral = nota_pp1 + nota_pp2 + nota_teorica`
  - Prioridade de avaliação: primeiro checamos a **frequência** (`< 75%` reprova direto por falta). Depois avaliamos as faixas de nota (`>= 7.0` aprova direto; `< 4.0` reprova direto por nota; entre `4.0` e `6.99` pede exame e calcula `media_final = (nota_semestral + nota_exame) / 2`).
- **Saídas:**
  - Boletim individual de cada estudante e estatísticas finais (quantidade e `%` de aprovados, reprovados por nota e reprovados por falta).

---

## 2. Teste de Mesa com Análise de Valor Limite (QA — Boundary Value Analysis)

| Caso de Teste (QA) | `PP1`, `PP2`, `AT` | `nota_semestral` | `frequencia` | `nota_exame` | `media_final` | Resultado Esperado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Reprovado por Falta (Mesmo com nota 10)** | `2.0`, `3.0`, `5.0` | `10.00` | `74.9%` *(Borda < 75)* | *Não pede* | - | `Reprovado por Falta` |
| **2. Aprovado Direto (No limite exato)** | `1.5`, `2.5`, `3.0` | `7.00` *(Borda >= 7)* | `75.0%` *(Borda >= 75)* | *Não pede* | - | `Aprovado (Direto)` |
| **3. Reprovado Direto por Nota** | `1.0`, `1.0`, `1.9` | `3.90` *(Borda < 4)* | `80.0%` | *Não pede* | - | `Reprovado por Nota (Direto)` |
| **4. Exame -> Aprovado no Limite** | `1.0`, `1.0`, `2.0` | `4.00` *(Borda >= 4)* | `85.0%` | `6.0` | `5.00` *(Borda >= 5)* | `Aprovado (Apos Exame)` |
| **5. Exame -> Reprovado** | `1.5`, `1.5`, `2.0` | `5.00` | `90.0%` | `4.0` | `4.50` *(Borda < 5)* | `Reprovado por Nota (Apos Exame)` |

---

## 3. Pontos-Chave para Explicar na Prova

1. **Por que testamos `if frequencia < 75.0` antes de testar se a nota é `>= 7.0`?**
   Porque um estudante que tirou nota `9.0` mas teve apenas `60%` de presença está reprovado por falta! Se testássemos a nota primeiro sem olhar a frequência, ele seria aprovado indevidamente.
2. **Como a função `ler_valor_valido` evita que o programa quebre?**
   Ela higieniza a string com `.strip().replace(",", ".")` (permitindo digitar `1,5` ou `1.5`) e usa `try / except ValueError` para capturar textos inválidos antes de comparar os limites `limite_minimo <= valor <= limite_maximo`.
