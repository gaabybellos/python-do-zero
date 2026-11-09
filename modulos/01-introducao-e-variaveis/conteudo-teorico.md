# Aula Teórica Completa — Módulo 01: Variáveis, Tipos e Estrutura Sequencial (`conteudo-teorico.md`)

Neste módulo você vai aprender a construir seus primeiros programas completos em Python seguindo a **Estrutura Sequencial**: programas em que cada linha é executada em ordem, de cima para baixo, sem pular etapas.

---

## 1. Variáveis e Nomenclatura Semântica (`snake_case`)

Uma **variável** guarda um dado na memória do computador para usarmos nas linhas seguintes.
Em Python (segundo o guia oficial **PEP 8**), seguimos três regras para dar nomes às variáveis:

1. **Use `snake_case`:** Letras minúsculas separadas por sublinhado (`_`), sem acentos e sem espaços.
2. **Dê nomes que expliquem o significado (*Clean Code*):** Quem bater o olho no nome da variável deve saber exatamente o que ela guarda.
3. **Use `UPPER_SNAKE_CASE` para Constantes:** Valores fixos de uma regra (como uma taxa ou cotação) ficam no topo do arquivo em letras maiúsculas.

| Ruim (Evite!) | Bom (Padrão PEP 8 & Clean Code) | Por que é melhor? |
| :--- | :--- | :--- |
| `n = "Lucas"` | `nome_estudante = "Lucas"` | Deixa claro que é o nome de um estudante, não um número. |
| `v1 = 50.0` | `preco_produto = 50.0` | Evita siglas vagas (`v1`, `x`, `aux`). |
| `taxa = 0.15` | `TAXA_DESCONTO = 0.15` | Em maiúsculas indica uma constante fixa do programa. |

---

## 2. Tipos Primitivos e Como Conferir o Tipo (`type`)

Todo valor em Python possui um **tipo**:

- **`str` (*String* / Texto):** Sempre entre aspas (`"Python"`, `'123'`).
- **`int` (*Integer* / Inteiro):** Números sem casa decimal (`0`, `42`, `-10`).
- **`float` (*Floating point* / Decimal):** Números com ponto decimal (`3.14`, `10.0`, `-0.5`).
- **`bool` (*Boolean* / Lógico):** Apenas `True` (Verdadeiro) ou `False` (Falso).

---

## 3. Operadores Aritméticos e Ordem de Precedência

Para transformar as entradas no bloco de **Processamento**, usamos os operadores matemáticos do Python:

| Operador | Significado | Exemplo | Resultado | Atenção (QA) |
| :--- | :--- | :--- | :--- | :--- |
| `+` | Soma | `8 + 2` | `10` | Se usar `+` entre dois textos (`"8" + "2"`), ele junta formando `"82"`! |
| `-` | Subtração | `8 - 2` | `6` | Funciona normalmente com resultados negativos (`2 - 8` $\rightarrow$ `-6`). |
| `*` | Multiplicação | `8 * 2` | `16` | Para calcular 15% de um valor, multiplique por `0.15`. |
| `/` | Divisão Real | `7 / 2` | `3.5` | Sempre devolve um `float` (mesmo `8 / 2` devolve `4.0`). |
| `//` | Divisão Inteira | `7 // 2` | `3` | Descarta a parte decimal sem arredondar para cima. |
| `%` | Resto da Divisão | `7 % 2` | `1` | Muito usado para saber se um número é múltiplo de outro. |
| `**` | Potência | `3 ** 2` | `9` | Calcula $3^2 = 9$. |

### A Regra dos Parênteses `()` (Erro nº 1 em Cálculo de Médias!)
Na matemática e no Python, **multiplicação (`*`) e divisão (`/`) são feitas antes de soma (`+`) e subtração (`-`)**.
Veja o que acontece se você esquecer os parênteses ao calcular a média de duas notas (`8.0` e `10.0`):
```python
# ERRADO: divide apenas o 10.0 por 2 (dando 5.0) e soma com 8.0 -> Resultado: 13.0!
media_errada = 8.0 + 10.0 / 2

# CORRETO: os parênteses forçam a soma (18.0) a acontecer antes da divisão por 2 -> Resultado: 9.0!
media_correta = (8.0 + 10.0) / 2
```

---

## 4. Entrada de Dados (`input`) e Conversão (`int`, `float`)

O comando `input("Mensagem: ")` pausa o programa, mostra a mensagem na tela e espera o usuário digitar algo e apertar `Enter`.

> **Ponto Crítico:** O `input()` **sempre devolve um texto (`str`)**, mesmo que o usuário digite apenas dígitos numéricos!

Por isso, seguimos três padrões de leitura:

```python
# 1. Quando queremos ler um TEXTO (usamos .strip() para limpar espaços extras):
nome_usuario = input("Digite seu nome: ").strip()

# 2. Quando queremos ler um NÚMERO INTEIRO (convertemos com int()):
idade_usuario = int(input("Digite sua idade: "))

# 3. Quando queremos ler um NÚMERO DECIMAL aceitando vírgula ou ponto (Padrão QA):
entrada_altura = input("Digite sua altura (m): ").strip().replace(",", ".")
altura_usuario = float(entrada_altura)
```

---

## 5. Saída Formatada (`print` com *f-strings*)

Para mostrar variáveis misturadas com texto de forma limpa, colocamos a letra **`f`** antes das aspas e colocamos o nome da variável entre chaves `{}`:

```python
produto = "Caderno"
preco = 24.5

# Sem formatação de casas decimais:
print(f"Produto: {produto} | Preço: R$ {preco}")
# Saída: Produto: Caderno | Preço: R$ 24.5

# Com formatação de 2 casas decimais (:.2f):
print(f"Produto: {produto} | Preço: R$ {preco:.2f}")
# Saída: Produto: Caderno | Preço: R$ 24.50
```

---

## 6. Erros Comuns Neste Módulo e Como Evitá-los

1. **Concatenar em vez de somar (`"10" + "20"` virando `"1020"`):**
   - *Causa:* Esqueceu de envolver o `input()` com `int(...)` ou `float(...)`.
2. **`ValueError: could not convert string to float: '7,5'`:**
   - *Causa:* O usuário digitou vírgula no lugar de ponto e o código não usou `.replace(",", ".")`.
3. **Média dando um valor maior que a própria nota:**
   - *Causa:* Esqueceu de colocar parênteses `(nota_1 + nota_2) / 2` antes de dividir.

---

## Próximo Passo

Agora que você concluiu a leitura da teoria:
1. Veja e execute os 3 programas na pasta [`exemplos/`](./exemplos/README.md).
2. Abra o raciocínio do primeiro exercício em [`raciocinio/PYZ-SEQ-N1-001.md`](./raciocinio/PYZ-SEQ-N1-001.md) para iniciar a prática!
