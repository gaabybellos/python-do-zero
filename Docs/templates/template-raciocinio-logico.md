# Template de Raciocínio Lógico, Teste de Mesa e QA (`template-raciocinio-logico.md`)

Utilizado pelo aluno em conjunto com o **`agente-logica`** **antes** de escrever qualquer linha de código Python.

---

## Identificação

- **ID do Exercício:** `PYZ-<MODULO>-<NIVEL>-<ID>`
- **Título:** `<Nome do Exercício>`
- **Módulo:** `<NN - Nome do Módulo>`

## 1. Decomposição do Problema (E-P-S)

- **Entradas (Quais dados eu recebo? Qual o tipo e os limites de cada um?):**
  - `...`
- **Processamento (Quais regras, validações ou cálculos preciso aplicar?):**
  - `...`
- **Saídas (O que preciso mostrar ao final?):**
  - `...`

## 2. Algoritmo em Português Estruturado (Passo a Passo)

```text
1. Ler ...
2. Validar se ...
3. Calcular ...
4. Se ..., então ...
5. Exibir ...
```

## 3. Teste de Mesa com Mentalidade de QA (Simulação Manual)

Preencha a tabela abaixo simulando o computador passo a passo com as **3 categorias de teste de QA**:

| Categoria de Teste (QA) | Valores de Entrada | Estado das Variáveis | Saída Produzida | Saída Está Correta? |
| :--- | :--- | :--- | :--- | :--- |
| **1. Caminho Feliz (*Happy Path*)** | | | | |
| **2. Valor Limite (*Boundary Value - BVA*)** | | | | |
| **3. Entrada Inválida / Negativa (*Negative Test*)** | | | | |

## 4. Validação do `agente-logica`

- [ ] Entradas, processamento e saídas estão completos?
- [ ] O passo a passo resolve o problema sem pular etapas?
- [ ] O Teste de Mesa cobriu Caminho Feliz, Valor Limite (BVA) e Entrada Inválida?
- **Status:** `[ ] Aguardando validação` | `[ ] Validado — Liberado para o agente-desenvolvimento`
