# Módulo 02 — Estruturas Condicionais (`PYZ-CND`)

## Objetivos de Aprendizado

1. Compreender operadores relacionais (`==`, `!=`, `>`, `<`, `>=`, `<=`).
2. Compreender operadores lógicos (`and`, `or`, `not`) e tabela-verdade aplicada ao dia a dia.
3. Tomar decisões no fluxo do programa usando `if`, `elif` e `else`.
4. Aplicar **Análise de Valor Limite (QA — Boundary Value Analysis)** para evitar bugs em fronteiras (`>` vs `>=`).

---

## Exercícios do Módulo

### Nível 1 (Fixação): `PYZ-CND-N1-001` — Verificador de Maioridade e Par ou Ímpar
- **Enunciado:** Leia a idade de uma pessoa e um número inteiro. Informe se ela já atingiu a maioridade (`>= 18` anos, usando a constante `MAIORIDADE = 18`) e se o número informado é par ou ímpar (usando o operador `%`).
- **Arquivo de Raciocínio Lógico:** `raciocinio/PYZ-CND-N1-001.md`
- **Arquivo de Código:** `exercicios/ex001_maioridade_par_impar.py`

### Nível 2 (Prática): `PYZ-CND-N2-002` — Sistema de Aprovação Escolar com Fronteiras (BVA)
- **Enunciado:** Leia a média de um estudante (`0.0` a `10.0`). Exiba `Aprovado` (`>= 7.0`), `Em Recuperação` (`>= 4.0` e `< 7.0`) ou `Reprovado` (`< 4.0`). Rejeite notas fora do intervalo `[0.0, 10.0]`.
- **Arquivo de Raciocínio Lógico:** `raciocinio/PYZ-CND-N2-002.md`
- **Arquivo de Código:** `exercicios/ex002_aprovacao_escolar.py`

### Nível 3 (Desafio): `PYZ-CND-N3-003` — Calculadora de Frete e Desconto Progressivo
- **Enunciado:** Leia o valor de uma compra e a região de entrega (`SUL`, `SUDESTE`, `OUTRAS`). Aplique frete grátis para compras `>= R$ 200.00` e desconto progressivo conforme a faixa de valor.
- **Arquivo de Raciocínio Lógico:** `raciocinio/PYZ-CND-N3-003.md`
- **Arquivo de Código:** `exercicios/ex003_frete_desconto.py`
