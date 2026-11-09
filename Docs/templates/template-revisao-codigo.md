# Template de Revisão de Código, Boas Práticas e QA (`template-revisao-codigo.md`)

Utilizado pelo **`agente-desenvolvimento`** para revisar o código Python criado pelo aluno sob a ótica de **PEP 8, Clean Code e Engenharia de Qualidade (QA)**.

---

## Identificação da Revisão

- **ID do Exercício:** `PYZ-<MODULO>-<NIVEL>-<ID>`
- **Arquivo Analisado:** `modulos/<modulo>/exercicios/<arquivo>.py`
- **Raciocínio Lógico Associado:** `modulos/<modulo>/raciocinio/PYZ-<MODULO>-<NIVEL>-<ID>.md`

## 1. Pontos Fortes do Código do Aluno

- Destaque o que o aluno fez bem (lógica correta, uso adequado de tipos, nomes claros, clareza na estrutura e proteção contra entradas inválidas).

## 2. Checklist de Boas Práticas (PEP 8, Clean Code & QA)

| Critério | Status (`OK` / `Ajustar`) | Observação Pedagógica |
| :--- | :--- | :--- |
| Correspondência com o Algoritmo / Teste de Mesa | | |
| Nomes semânticos em `snake_case` (sem `x`, `a`, `aux`) | | |
| Ausência de números mágicos (uso de constantes `UPPER_SNAKE_CASE`) | | |
| Formatação PEP 8 (indentação de 4 espaços, espaços em operadores, `ruff`) | | |
| Uso adequado de `f-strings` na saída | | |
| **QA — Valores Limite (BVA):** Condições `<` vs `<=` e `>` vs `>=` corretas | | |
| **QA — Programação Defensiva:** Tratamento de entradas (vírgula/ponto, limites) | | |

## 3. Perguntas ou Sugestões de Refatoração Guiada

- Caso haja algo para melhorar, faça perguntas socráticas ou mostre como deixar o código mais *Pythonico*, resiliente e limpo.

## 4. Parecer Final

- **Status:** `[ ] Aprovado` | `[ ] Requer pequenos ajustes`
- **Próximo Passo:** Acionar o **`responsavel-repositorio`** para registrar a conclusão em `Docs/progresso-aluno.md`.
