# Folha de Consulta Rápida — Fundamentos e Módulo 01 (`cheat-sheet-python-qa.md`)

> Esta folha de consulta reúne **apenas os comandos já ensinados até o Módulo 01**, crescendo junto com a sua evolução na trilha.

---

## 1. Exibir na Tela (`print` e *f-strings*)

```python
nome_aluno = "Ana"
media_final = 8.567

# Exibir texto simples
print("Bem-vindo ao Python!")

# Exibir variáveis dentro do texto com f-string (coloque a letra f antes das aspas)
print(f"Aluna: {nome_aluno}")

# Formatar número decimal (float) com 2 casas após o ponto (:.2f)
print(f"Média formatada: {media_final:.2f}")  # Exibe: Média formatada: 8.57
```

---

## 2. Ler Dados do Teclado (`input`) e Converter Tipos

> **Regra de Ouro:** O comando `input()` **sempre** devolve um texto (`str`). Para fazer contas matemáticas, converta com `int()` ou `float()`!

```python
# 1. Ler um texto (str) e remover espaços extras nas pontas com .strip()
nome_cliente = input("Digite seu nome: ").strip()

# 2. Ler um número inteiro (int)
quantidade_pessoas = int(input("Digite a quantidade de pessoas: "))

# 3. Ler um número decimal (float) aceitando tanto ponto (1.5) quanto vírgula (1,5) — Dica de QA!
entrada_preco = input("Digite o preço (R$): ").strip().replace(",", ".")
preco_produto = float(entrada_preco)
```

---

## 3. Operadores Aritméticos (Contas Matemáticas)

| Operador | Operação | Exemplo em Python | Resultado |
| :--- | :--- | :--- | :--- |
| `+` | Adição (Soma) | `10 + 5` | `15` |
| `-` | Subtração | `10 - 4` | `6` |
| `*` | Multiplicação | `6 * 3` | `18` |
| `/` | Divisão (sempre gera `float`) | `10 / 2` | `5.0` |
| `//` | Divisão Inteira (descarta decimais) | `7 // 2` | `3` |
| `%` | Resto da Divisão (Módulo) | `7 % 2` | `1` |
| `**` | Potência (Elevado a) | `2 ** 3` | `8` |

> **Atenção aos Parênteses `()`:** Assim como na matemática, `*` e `/` são calculados antes de `+` e `-`. Para calcular uma média, **sempre use parênteses na soma**:
> `media = (nota_1 + nota_2 + nota_3) / 3`

---

## 4. Comandos Úteis no Terminal

```powershell
# Executar um script Python
python caminho/do/arquivo.py

# Verificar estilo PEP 8 com o Ruff
ruff check .

# Executar os testes automatizados com o Pytest
pytest -v
```
