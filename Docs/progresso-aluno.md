# Registro de Progresso do Aluno (`progresso-aluno.md`)

Arquivo mantido pelo **`responsavel-repositorio`** para rastrear a evolução do aluno ao longo da trilha e garantir que todas as etapas do fluxo (`professor -> agente-logica -> agente-desenvolvimento`) foram cumpridas com padrões de **Clean Code, PEP 8 e Qualidade (QA)**.

> **Dica:** Para inicializar seu progresso pessoal em `Docs/progresso-local.md` (ignorado pelo Git para não sujar seu `git status`) ou reiniciar do zero, execute:
> `python scripts/resetar_progresso.py`

## Status Geral da Trilha

| Módulo | Prefixo | Status | Exercícios Concluídos |
| :--- | :--- | :--- | :--- |
| 01 - Introdução, Variáveis e Estrutura Sequencial | `PYZ-SEQ` | Em Andamento | 0 / 6 |
| 02 - Estruturas Condicionais | `PYZ-CND` | Bloqueado | 0 / 6 |
| 03 - Laços de Repetição | `PYZ-REP` | Bloqueado | 0 / 6 |
| 04 - Coleções (Listas, Tuplas, Dicionários) | `PYZ-COL` | Bloqueado | 0 / 6 |
| 05 - Funções, Modularização e Testes | `PYZ-FUN` | Bloqueado | 0 / 6 |
| 06 - Mini-Projetos Integradores | `PYZ-PRJ` | Bloqueado | 0 / 4 |

---

## Rastreabilidade Detalhada por Exercício (Módulo 01 — `PYZ-SEQ`)

| ID do Exercício | Título | Teoria (`professor`) | Lógica & QA (`agente-logica`) | Código & PEP 8 (`agente-desenvolvimento`) | Arquivo de Código | Status Final |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `PYZ-SEQ-N1-001` | Boas-vindas e Soma Simples | Pronto para iniciar | Pendente | Pendente | `modulos/01-introducao-e-variaveis/exercicios/ex001_boas_vindas_soma.py` | A Fazer |
| `PYZ-SEQ-N1-002` | Antecessor, Sucessor e Dobro | Pendente | Pendente | Pendente | `modulos/01-introducao-e-variaveis/exercicios/ex002_antecessor_sucessor.py` | A Fazer |
| `PYZ-SEQ-N2-003` | Média de Notas Escolares | Pendente | Pendente | Pendente | `modulos/01-introducao-e-variaveis/exercicios/ex003_media_escolar.py` | A Fazer |
| `PYZ-SEQ-N2-004` | Conversor de Medidas e Moeda Fixa | Pendente | Pendente | Pendente | `modulos/01-introducao-e-variaveis/exercicios/ex004_conversor_medidas_moeda.py` | A Fazer |
| `PYZ-SEQ-N3-005` | Calculadora de Conta de Restaurante | Pendente | Pendente | Pendente | `modulos/01-introducao-e-variaveis/exercicios/ex005_conta_restaurante.py` | A Fazer |
| `PYZ-SEQ-N3-006` | Simulador Didático de Salário Líquido | Pendente | Pendente | Pendente | `modulos/01-introducao-e-variaveis/exercicios/ex006_salario_liquido.py` | A Fazer |

---

## Catálogo de Estudos de Caso Autorais (`estudos-de-caso/`)

Os casos abaixo são materiais fictícios de referência do projeto e não fazem parte do progresso individual do estudante.

| ID do Caso | Tema | Pasta | Validações QA & Testes | Status do Catálogo |
| :--- | :--- | :--- | :--- | :--- |
| `PYZ-CASE-001` | Sistema de Fechamento de Boletim | `estudos-de-caso/01-sistema-boletim-academico/` | Vírgula/ponto, limites BVA e suíte `pytest` | Referência disponível |
| `PYZ-CASE-002` | Analisador de Consumo e Tarifa | `estudos-de-caso/02-analisador-consumo-energia/` | Acumuladores, extremos (`maior`/`menor`) e `pytest` | Referência disponível |
| `PYZ-CASE-003` | Controle de Lotes e Estoque | `estudos-de-caso/03-controle-estoque-farmacia/` | Unicidade de código, saldo não negativo e `pytest` | Referência disponível |
| `PYZ-CASE-004` | Calculadora Modular de Folha de Pagamento | `estudos-de-caso/04-calculadora-folha-pagamento/` | Funções puras + suíte automatizada `pytest` | Referência disponível |
