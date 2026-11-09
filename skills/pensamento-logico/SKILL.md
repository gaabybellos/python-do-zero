---
name: pensamento-logico
description: Estruturar a resolução de problemas através de decomposição (Entrada, Processamento, Saída), pseudocódigo e Teste de Mesa antes de codar em Python.
---

# Pensamento Lógico e Algoritmos (`pensamento-logico`)

## Propósito

Separar a dificuldade de **resolver o problema** (lógica) da dificuldade de **escrever em Python** (sintaxe).

## Método em 4 Passos

### Passo 1: Decomposição (E-P-S)
Todo problema deve ser quebrado em:
1. **Entradas (Inputs):** Quais dados entram no programa e de que tipo são (número inteiro, decimal, texto)?
2. **Processamento (Regras):** Quais fórmulas, condições ou repetições transformam a entrada na saída?
3. **Saídas (Outputs):** O que exatamente o programa precisa mostrar ao usuário ou retornar?

### Passo 2: Algoritmo em Português Estruturado (Pseudocódigo)
O aluno deve escrever a receita numerada em português claro:
```text
1. Ler o valor da conta e guardar em valor_conta
2. Calcular 10% de taxa de serviço: taxa_servico = valor_conta * 0.10
3. Somar valor_conta + taxa_servico e guardar em total_pagar
4. Mostrar total_pagar na tela
```

### Passo 3: Teste de Mesa Obrigatório
O aluno deve preencher uma tabela simulando o computador linha por linha para pelo menos:
- **1 Caso Normal** (ex.: `valor_conta = 100.00`)
- **1 Caso de Borda / Exceção** (ex.: `valor_conta = 0.00` ou valor negativo)

### Passo 4: Validação de Transição
Só autorize a ida ao `agente-desenvolvimento` quando o Teste de Mesa produzir a saída esperada sem erros lógicos.
