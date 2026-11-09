# Guia de Boas Práticas e Regras de Desenvolvimento em Python

Este guia resume as boas práticas exigidas pelo **`agente-desenvolvimento`** e pelo **`responsavel-repositorio`** em todos os exercícios do repositório.

---

## 1. Nomenclatura com Significado (Clean Code + PEP 8)

O código é lido muito mais vezes do que é escrito. Escolha nomes que expliquem **o que** o dado representa.

| Elemento | Padrão PEP 8 | Ruim (Evite) | Bom (Recomendado) |
| :--- | :--- | :--- | :--- |
| **Variáveis** | `snake_case` | `x = 25`, `n = "Ana"`, `vlr = 10.5` | `idade_aluno = 25`, `nome_cliente = "Ana"`, `preco_unitario = 10.5` |
| **Booleanos (`bool`)** | `eh_...`, `possui_...`, `esta_...` | `ativo = True`, `maior = False` | `esta_ativo = True`, `eh_maior_de_idade = False` |
| **Funções** | `verbo_no_infinitivo_...` | `media(a, b)`, `proc(x)` | `calcular_media(nota_1, nota_2)`, `validar_cpf(cpf)` |
| **Constantes** | `UPPER_SNAKE_CASE` | `if idade >= 18:` *(18 solto)* | `MAIORIDADE_PENAL = 18` $\rightarrow$ `if idade >= MAIORIDADE_PENAL:` |
| **Arquivos `.py`** | `snake_case.py` | `Exercicio 1.py`, `MeuCodigo.py` | `ex001_boas_vindas_soma.py`, `calculadora_imc.py` |

---

## 2. Formatação e Estilo (PEP 8)

- **Indentação:** Sempre **4 espaços** por nível de bloco (nunca misture Tab com espaços).
- **Espaços em Operadores:** Coloque 1 espaço ao redor de operadores (`soma = valor_1 + valor_2`, `idade >= 18`), mas não coloque espaço dentro dos parênteses (`print(soma)`).
- **Tamanho da Linha:** Mantenha linhas com no máximo **88 caracteres** para facilitar a leitura.
- **Uso de `f-strings`:** Prefira `f"Olá, {nome}! Você tem {idade} anos."` em vez de concatenar com `+` (`"Olá, " + nome + "! Você tem " + str(idade) + " anos."`).

---

## 3. Organização Lógica de um Script Python

Estruture seus arquivos sempre nesta ordem:

```python
"""
Módulo: Breve descrição do que este exercício faz.
ID: PYZ-SEQ-N1-001
"""

# 1. CONSTANTES (se houver)
TAXA_SERVICO = 0.10


# 2. FUNÇÕES DE PROCESSAMENTO (a partir do Módulo 05)
def calcular_total_com_taxa(valor_consumo: float) -> float:
    """Calcula o valor final da conta adicionando a taxa de serviço."""
    return valor_consumo * (1 + TAXA_SERVICO)


# 3. BLOCO PRINCIPAL (Entrada -> Processamento -> Saída)
def main() -> None:
    valor_digitado = float(input("Digite o valor do consumo (R$): "))
    total_pagar = calcular_total_com_taxa(valor_digitado)
    print(f"Total a pagar com taxa: R$ {total_pagar:.2f}")


if __name__ == "__main__":
    main()
```

---

## 4. Como Ler Erros do Python (*Tracebacks*) sem Pânico

Quando um erro aparecer no terminal, **não apague tudo**. Leia de baixo para cima:

1. **`SyntaxError`:** O Python não entendeu a gramática (faltou fechar parênteses `)`, aspas `"` ou dois-pontos `:` no final do `if`/`for`/`def`).
2. **`IndentationError`:** Um bloco de código está desalinhado (faltaram os 4 espaços após `if:`, `for:` ou `def:`).
3. **`NameError: name '...' is not defined`:** Você tentou usar uma variável antes de criá-la ou digitou o nome dela diferente (ex.: criou `idade_usuario` e chamou `idade_usario`).
4. **`TypeError`:** Você tentou fazer uma operação entre tipos incompatíveis (ex.: somar texto `"10"` com número `5` sem converter com `int()`).
5. **`ValueError`:** O tipo está certo, mas o conteúdo é inválido (ex.: tentar converter `int("abc")`).
6. **`IndexError: list index out of range`:** Você tentou acessar uma posição da lista que não existe (lembre-se: em Python, a primeira posição é sempre `0`).
