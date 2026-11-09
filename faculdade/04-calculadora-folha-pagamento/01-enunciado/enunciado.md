# Tarefa de Faculdade 04 — Calculadora Modular de Folha de Pagamento (`PYZ-FAC-004`)

## Enunciado do Problema

**DESCRIÇÃO: PROCESSADOR MODULAR DE CONTRACHEQUE COM TESTES AUTOMATIZADOS**

Desenvolva um sistema modularizado em Python (separando funções puras de cálculo da entrada/saída de dados) que calcule o contracheque de um colaborador a partir de:

1. **Salário Base Mensal (`R$`):** valor `> 0.0` (carga horária padrão de `220` horas mensais);
2. **Quantidade de Horas Extras trabalhadas (`>= 0.0`):** cada hora extra vale **50% a mais** que o valor da hora normal;
3. **Quantidade de Dependentes (`int >= 0`):** cada dependente concede um bônus de auxílio-família de **R\$ 150,00** (apenas para salários base de até **R\$ 3.500,00**).

### Regras de Desconto Previdenciário e Imposto Retido (Sobre Bruto = Base + Horas Extras)

- **Até R\$ 2.000,00:** Alíquota de **8%**;
- **De R\$ 2.000,01 até R\$ 4.500,00:** Alíquota de **11%**;
- **Acima de R\$ 4.500,00:** Alíquota de **14%**.

$$\text{Salário Líquido} = (\text{Salário Base} + \text{Valor Horas Extras}) - \text{Desconto} + \text{Auxílio Dependentes}$$
