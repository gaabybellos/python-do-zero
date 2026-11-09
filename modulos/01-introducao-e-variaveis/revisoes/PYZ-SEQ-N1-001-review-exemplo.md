# Exemplo de Revisão de Código, Boas Práticas e QA (`PYZ-SEQ-N1-001-review-exemplo.md`)

> **Nota:** Este arquivo é um **exemplo demonstrativo** de como o **`agente-desenvolvimento`** documenta a revisão de código após o estudante concluir um exercício.

---

## Identificação da Revisão

- **ID do Exercício:** `PYZ-SEQ-N1-001` — Boas-vindas e Soma Simples
- **Arquivo Analisado:** `modulos/01-introducao-e-variaveis/exercicios/ex001_boas_vindas_soma.py`
- **Raciocínio Lógico Associado:** `modulos/01-introducao-e-variaveis/raciocinio/PYZ-SEQ-N1-001.md`

## 1. Pontos Fortes do Código Esperado

- Separação clara entre os blocos de **Entrada**, **Processamento** e **Saída** dentro da função `main()`.
- Uso de nomes semânticos em `snake_case` (`nome_aluno`, `primeiro_numero`, `segundo_numero`, `resultado_soma`).
- Aplicação de `.strip()` na leitura do nome para evitar espaços indesejados na mensagem final.

## 2. Checklist de Boas Práticas (PEP 8, Clean Code & QA)

| Critério | Status (`OK` / `Ajustar`) | Observação Pedagógica |
| :--- | :--- | :--- |
| Correspondência com o Algoritmo / Teste de Mesa | `OK` | Segue os 5 passos planejados na decomposição E-P-S. |
| Nomes semânticos em `snake_case` (sem `x`, `a`, `aux`) | `OK` | Variáveis autoexplicativas e alinhadas ao domínio. |
| Ausência de números mágicos (uso de constantes `UPPER_SNAKE_CASE`) | `OK` | Não há constantes mágicas neste exercício. |
| Formatação PEP 8 (indentação de 4 espaços, até 88 colunas, `ruff`) | `OK` | Zero alertas no `ruff check`. |
| Uso adequado de `f-strings` na saída | `OK` | Mensagem formatada de forma limpa e legível. |
| **QA — Valores Limite (BVA):** Soma com `0` e números negativos | `OK` | Testado com `-5 + 5 = 0` e `0 + 0 = 0`. |
| **QA — Programação Defensiva:** Conversão explícita com `int()` | `OK` | Evita o bug clássico de concatenação de strings (`"10" + "25"` $\rightarrow$ `"1025"`). |

## 3. Parecer Final (Exemplo)

- **Status:** `[x] Modelo de Referência Aprovado`
- **Próximo Passo:** Ao concluir sua implementação em `exercicios/ex001_boas_vindas_soma.py`, acione o `agente-desenvolvimento` para receber sua revisão personalizada!
