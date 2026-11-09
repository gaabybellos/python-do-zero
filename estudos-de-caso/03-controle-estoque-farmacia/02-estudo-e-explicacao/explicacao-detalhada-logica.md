# Explicação Detalhada — Controle de Estoque de Farmácia (`PYZ-CASE-003`)

> **Aviso de Integridade:** Estudo de caso fictício e autoral criado exclusivamente para aprendizado. Não corresponde a uma avaliação acadêmica real e não deve ser submetido como trabalho escolar ou universitário.

## Identificação do Caso

- **ID:** `PYZ-CASE-003`
- **Tema:** Coleções (`list` e `dict`), Menu Interativo (`while True`) e Regras de Integridade de Dados (QA)
- **Pasta do Caso:** `estudos-de-caso/03-controle-estoque-farmacia/`

---

## 1. Como Organizar Cadastros em Memória (`list` de `dict`)

Em vez de criar dezenas de variáveis soltas, representamos **cada medicamento como um dicionário (`dict`)** com chaves nomeadas (`"codigo"`, `"nome"`, `"quantidade"`, `"estoque_minimo"`, `"preco_unitario"`) e guardamos todos os dicionários dentro de uma única **lista (`estoque = []`)**.

---

## 2. Validações de Qualidade (QA) Aplicadas

| Regra de Negócio / QA | O que aconteceria sem validação? | Como o código protege? |
| :--- | :--- | :--- |
| **Unicidade de Código** | Dois produtos teriam o mesmo código `"MED01"`, causando baixa no item errado. | `buscar_medicamento(estoque, codigo)` verifica se já existe antes de cadastrar. |
| **Proteção de Saldo Negativo** | Retirar `15` unidades de um item com saldo `10` deixaria `-5` no estoque. | `if qtd_saida > item["quantidade"]:` bloqueia a baixa e mantém o saldo intacto. |
| **Alerta de Estoque Mínimo** | Medicamento crítico acabaria sem aviso. | Compara `item["quantidade"] < item["estoque_minimo"]` e sinaliza no relatório. |
