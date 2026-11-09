# Guia de Validação Defensiva e Mentalidade de QA em Python (`guia-validacao-e-qa.md`)

A maioria dos cursos para iniciantes ensina apenas o **"Caminho Feliz" (*Happy Path*)**: assume que o usuário nunca vai digitar uma letra no lugar de um número, nunca vai usar vírgula (`1,5`) em vez de ponto (`1.5`) e nunca vai digitar uma idade negativa.

No mundo real, **Qualidade de Software (QA)** não é uma etapa que acontece só no final: ela começa **antes** de escrever o código (*Shift-Left Testing*). Este guia ensina você a pensar como um Engenheiro de Qualidade desde o seu primeiro script em Python.

---

## 1. Os 3 Pilares de Testes no Seu Teste de Mesa

Sempre que você preencher o seu documento de raciocínio lógico (`template-raciocinio-logico.md`), você deve testar seu algoritmo contra **3 categorias de cenários**:

| Técnica de QA | O que significa? | Exemplo (Nota de `0.0` a `10.0`, média de aprovação `>= 7.0`) |
| :--- | :--- | :--- |
| **1. Partição de Equivalência Válida (*Happy Path*)** | Um valor comum que representa o funcionamento normal esperado. | Nota `8.5` $\rightarrow$ Aprovado; Nota `5.0` $\rightarrow$ Reprovado. |
| **2. Análise de Valor Limite (*Boundary Value Analysis - BVA*)** | A maioria dos bugs mora nas **fronteiras** das condições (`>` vs `>=`, `<` vs `<=`). Teste exatamente no limite, um décimo abaixo e um décimo acima! | Testar `0.0` (mínimo), `10.0` (máximo), `6.9` (quase aprovado) e `7.0` (exatamente no corte). |
| **3. Testes Negativos e Entradas Inválidas (*Negative Testing*)** | O que acontece quando o usuário tenta quebrar o sistema ou comete erros de digitação? | Digitar `-0.1`, `10.1`, `"8,5"` (com vírgula), `"abc"` (letras) ou apertar `Enter` vazio (`""`). |

---

## 2. Programação Defensiva no Terminal: Os 4 Problemas Clássicos e Como Resolver

### Problema 1: O usuário brasileiro digita vírgula (`1,5`) em vez de ponto (`1.5`)
- **O que acontece sem tratamento:** `float("1,5")` lança `ValueError: could not convert string to float: '1,5'` e o programa fecha.
- **Solução Defensiva:** Usar `.strip().replace(",", ".")` antes do `float()`:
  ```python
  entrada = input("Digite a nota: ").strip().replace(",", ".")
  nota = float(entrada)  # Funciona tanto para "1,5" quanto para "1.5"!
  ```

### Problema 2: O usuário aperta `Enter` vazio ou digita letras (`"abc"`)
- **O que acontece sem tratamento:** `int("")` ou `float("abc")` lança `ValueError`.
- **Solução Defensiva:** Envolver a conversão em um bloco `try / except ValueError` dentro de um laço `while True`:
  ```python
  def ler_float_no_intervalo(mensagem: str, minimo: float, maximo: float) -> float:
      while True:
          entrada = input(mensagem).strip().replace(",", ".")
          try:
              valor = float(entrada)
              if minimo <= valor <= maximo:
                  return valor
              print(f"Erro: o valor deve estar entre {minimo} e {maximo}.")
          except ValueError:
              print("Entrada invalida! Digite apenas numeros (ex: 7.5 ou 7,5).")
  ```

### Problema 3: Diferença entre letras maiúsculas e minúsculas (`"s"` vs `"S"`)
- **O que acontece sem tratamento:** Se você testar `if opcao == "S":` e o usuário digitar `"s"`, o programa rejeita.
- **Solução Defensiva:** Sempre higienizar strings de opção com `.strip().upper()`:
  ```python
  resposta = input("Deseja continuar? [S/N]: ").strip().upper()
  ```

### Problema 4: Divisão por Zero (`ZeroDivisionError`)
- **O que acontece sem tratamento:** Calcular média `soma / quantidade` quando `quantidade == 0` trava o programa com `ZeroDivisionError`.
- **Solução Defensiva:** Verificar se o divisor é maior que zero antes de dividir:
  ```python
  media = soma / quantidade if quantidade > 0 else 0.0
  ```

---

## 3. Como Escrever Código Testável para o `pytest`

Para que um código possa ser testado automaticamente pelo `pytest`:
1. **Separe a lógica matemática do `input()` e `print()`:** Crie funções puras que recebem valores por parâmetro e devolvem o resultado com `return`.
2. **Crie testes cobrindo Caminho Feliz, Bordas (BVA) e Exceções:**
   ```python
   import pytest
   from meu_modulo import calcular_desconto

   def test_desconto_caminho_feliz():
       assert calcular_desconto(100.0) == 90.0

   def test_desconto_valor_negativo_levanta_erro():
       with pytest.raises(ValueError):
           calcular_desconto(-10.0)
   ```
