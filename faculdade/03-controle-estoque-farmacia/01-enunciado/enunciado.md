# Tarefa de Faculdade 03 — Controle de Estoque de Farmácia (`PYZ-FAC-003`)

## Enunciado do Problema

**DESCRIÇÃO: SISTEMA DE CONTROLE DE ESTOQUE E ALERTA DE REPOSIÇÃO**

Desenvolva um programa em Python com um **menu interativo** que gerencie os medicamentos de uma farmácia utilizando **listas e dicionários**. O menu deve oferecer as seguintes opções:

1. **Cadastrar Medicamento:** lê o código único (texto não vazio), nome, quantidade inicial (`>= 0`), estoque mínimo (`>= 1`) e preço unitário (`> 0.0`). Não deve permitir códigos duplicados.
2. **Registrar Saída (Venda/Dispensação):** lê o código do medicamento e a quantidade a retirar (`> 0`). Se a quantidade solicitada for maior que o saldo disponível, a operação deve ser bloqueada com mensagem de erro.
3. **Listar Relatório Geral e Alertas de Estoque Baixo:** exibe todos os medicamentos cadastrados, o valor financeiro total em estoque e destaca com `[ALERTA: REPOR ESTOQUE]` aqueles cuja quantidade atual seja **menor** que o estoque mínimo.
4. **Encerrar Sistema:** finaliza a execução.
