# Registro de Progresso do Aluno (`progresso-aluno.md`)

Arquivo mantido pelo **`responsavel-repositorio`** para rastrear a evolução do aluno ao longo da trilha e garantir que todas as etapas do fluxo (`professor -> agente-logica -> agente-desenvolvimento`) foram cumpridas com padrões de **Clean Code, PEP 8 e Qualidade (QA)**.

> **Dica:** Para reiniciar o seu progresso do zero a qualquer momento, execute:
> `python scripts/resetar_progresso.py`

## Status Geral da Trilha

| Módulo | Prefixo | Status | Exercícios Concluídos |
| :--- | :--- | :--- | :--- |
| 01 - Introdução, Variáveis e Estrutura Sequencial | `PYZ-SEQ` | Em Andamento | 0 / 3 |
| 02 - Estruturas Condicionais | `PYZ-CND` | Bloqueado | 0 / 3 |
| 03 - Laços de Repetição | `PYZ-REP` | Bloqueado | 0 / 3 |
| 04 - Coleções (Listas, Tuplas, Dicionários) | `PYZ-COL` | Bloqueado | 0 / 3 |
| 05 - Funções, Modularização e Testes | `PYZ-FUN` | Bloqueado | 0 / 3 |
| 06 - Mini-Projetos Integradores | `PYZ-PRJ` | Bloqueado | 0 / 2 |

---

## Rastreabilidade Detalhada por Exercício (Módulo Atual)

| ID do Exercício | Título | Teoria (`professor`) | Lógica & QA (`agente-logica`) | Código & PEP 8 (`agente-desenvolvimento`) | Arquivo de Código | Status Final |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `PYZ-SEQ-N1-001` | Boas-vindas e Soma Simples | Pronto para iniciar | Pendente | Pendente | `modulos/01-introducao-e-variaveis/exercicios/ex001_boas_vindas_soma.py` | A Fazer |
| `PYZ-SEQ-N2-002` | Média de Notas Escolares | Pendente | Pendente | Pendente | `modulos/01-introducao-e-variaveis/exercicios/ex002_conversor_media.py` | A Fazer |
| `PYZ-SEQ-N3-003` | Calculadora de Conta de Restaurante | Pendente | Pendente | Pendente | `modulos/01-introducao-e-variaveis/exercicios/ex003_conta_restaurante.py` | A Fazer |

---

## Catálogo de Tarefas Acadêmicas Resolvidas (`faculdade/`)

| ID da Tarefa | Tema / Disciplina | Pasta da Tarefa | Validações QA & Testes | Status |
| :--- | :--- | :--- | :--- | :--- |
| `PYZ-FAC-001` | Sistema de Fechamento de Boletim Acadêmico | `faculdade/01-sistema-boletim-academico/` | Vírgula/ponto, limites BVA e presença mínima | Concluído |
| `PYZ-FAC-002` | Analisador de Consumo e Tarifa de Energia | `faculdade/02-analisador-consumo-energia/` | Acumuladores, extremos (`maior`/`menor`) e faixas | Concluído |
| `PYZ-FAC-003` | Controle de Lotes e Estoque de Farmácia | `faculdade/03-controle-estoque-farmacia/` | Unicidade de código e bloqueio de saldo negativo | Concluído |
| `PYZ-FAC-004` | Calculadora Modular de Folha de Pagamento | `faculdade/04-calculadora-folha-pagamento/` | Funções puras + Suíte automatizada `pytest` | Concluído |
