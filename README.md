# Python do Zero — Lógica, Clean Code & Mentalidade de QA Guiados por IA

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Code Style: Ruff](https://img.shields.io/badge/Code%20Style-Ruff%20%2F%20PEP%208-261230?logo=ruff&logoColor=D7FF64)
![Tests: Pytest](https://img.shields.io/badge/QA%20Tests-Pytest-0A9EDC?logo=pytest&logoColor=white)
![Methodology: Shift-Left QA](https://img.shields.io/badge/Methodology-Shift--Left%20QA-success)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Bem-vindo ao **Python do Zero**! Este repositório Open Source é um ambiente de aprendizado interativo projetado para quem está começando a programar **do zero absoluto** e quer construir uma base sólida em:

1. **Lógica de Programação e Algoritmos** (Decomposição E-P-S e Teste de Mesa);
2. **Desenvolvimento em Python com Boas Práticas** (PEP 8 e Clean Code desde a primeira linha);
3. **Engenharia de Qualidade (*Shift-Left QA*)** (Programação Defensiva, Análise de Valor Limite - BVA, Partição de Equivalência, Testes Negativos e `pytest`).

Aqui, os agentes de IA **não entregam código pronto sem você pensar**: eles atuam como mentores socráticos que guiam seu raciocínio passo a passo.

---

## 🚀 Por Que Este Repositório é Diferente? (Abordagem QA-First)

A maioria dos materiais para iniciantes ensina apenas o **"Caminho Feliz" (*Happy Path*)** — códigos que quebram assim que o usuário digita `1,5` com vírgula em vez de `1.5`, aperta `Enter` vazio ou digita um número negativo.

Neste repositório, você aprende desde o **Módulo 01** a pensar como um **Engenheiro de Qualidade (QA)**:
- Testar as **fronteiras** das condições (*Boundary Value Analysis*: `<` vs `<=`, `>` vs `>=`);
- Proteger entradas do usuário contra falhas de digitação (`ValueError`, vírgula vs. ponto, limites);
- Separar regras de negócio de `input()`/`print()` para validar tudo automaticamente com **`pytest`**.

---

## 🤖 Como Funciona o Ciclo de Estudo com os 4 Agentes

Para cada tema e exercício, você é acompanhado por **4 agentes especialistas** nesta sequência:

```text
responsavel-repositorio -> professor -> agente-logica -> agente-desenvolvimento
```

1. **`responsavel-repositorio` (Guardião do Repositório):**
   - Verifica onde você parou em [`Docs/progresso-aluno.md`](./Docs/progresso-aluno.md), organiza as pastas e indica qual módulo ou exercício iniciar.
2. **`professor` (Mentor Teórico):**
   - Explica o conceito do dia usando analogias simples do cotidiano, tira suas dúvidas pelo Método Socrático e propõe exercícios em 3 níveis.
3. **`agente-logica` (Especialista em Pensamento Computacional & QA no Teste de Mesa):**
   - Antes de você escrever qualquer código Python, ajuda a quebrar o problema em **Entrada $\rightarrow$ Processamento $\rightarrow$ Saída**, montar o algoritmo em português e preencher o **Teste de Mesa com Caminho Feliz, Valor Limite (BVA) e Entrada Inválida**.
4. **`agente-desenvolvimento` (Mentor Python, Clean Code & Revisão QA):**
   - Guia a tradução para Python, ensina a ler mensagens de erro (*Tracebacks*) e realiza o Code Review exigindo **PEP 8, Clean Code e Validação Defensiva**.

---

## 🗺️ Trilha Completa de Módulos

| Módulo | Pasta / Guia | O que você vai aprender |
| :--- | :--- | :--- |
| **Módulo 00** | [`Docs/00-preparacao-ambiente.md`](./Docs/00-preparacao-ambiente.md) | Instalação do Python, configuração do `PATH`, execução no terminal e uso do `pytest` e `ruff`. |
| **Módulo 01** | [`modulos/01-introducao-e-variaveis/`](./modulos/01-introducao-e-variaveis/README.md) | Variáveis semânticas (`snake_case`), tipos (`str`, `int`, `float`, `bool`), operadores, `input()` e `print()`. |
| **Módulo 02** | [`modulos/02-estruturas-condicionais/`](./modulos/02-estruturas-condicionais/README.md) | Decisões com `if`, `elif`, `else`, operadores lógicos e Análise de Valor Limite (BVA). |
| **Módulo 03** | [`modulos/03-lacos-de-repeticao/`](./modulos/03-lacos-de-repeticao/README.md) | Repetição com `while` e `for`, contadores, acumuladores e validação defensiva de entradas. |
| **Módulo 04** | [`modulos/04-colecoes-listas-dicionarios/`](./modulos/04-colecoes-listas-dicionarios/README.md) | Organização de dados em memória com Listas (`list`), Tuplas (`tuple`) e Dicionários (`dict`). |
| **Módulo 05** | [`modulos/05-funcoes-e-modularizacao/`](./modulos/05-funcoes-e-modularizacao/README.md) | Funções puras (`def`/`return`), *Type Hints*, `try/except` e testes automatizados com `pytest`. |
| **Módulo 06** | [`modulos/06-mini-projetos/`](./modulos/06-mini-projetos/README.md) | Aplicações completas de terminal integrando todos os conceitos com cobertura de testes. |
| **Faculdade** | [`faculdade/`](./faculdade/README.md) | Catálogo de 4 tarefas acadêmicas completas resolvidas, comentadas linha a linha e validadas com QA. |

---

## 🎓 Catálogo de Tarefas Acadêmicas Resolvidas (`faculdade/`)

Cada tarefa em [`faculdade/`](./faculdade/README.md) possui sua própria pasta unificada contendo `README.md` (instruções de execução), `01-enunciado/`, `02-estudo-e-explicacao/` (explicação passo a passo da lógica + código comentado) e `03-entrega-professor/` (código limpo e testado):

1. **[`01-sistema-boletim-academico/`](./faculdade/01-sistema-boletim-academico/README.md):** Fechamento de notas e frequência com exame substitutivo, contadores, porcentagens e validação de vírgula/ponto.
2. **[`02-analisador-consumo-energia/`](./faculdade/02-analisador-consumo-energia/README.md):** Tarifação progressiva por faixas de kWh, acumuladores e descoberta de maior/menor consumo.
3. **[`03-controle-estoque-farmacia/`](./faculdade/03-controle-estoque-farmacia/README.md):** Sistema com menu interativo, lista de dicionários, unicidade de código e bloqueio de estoque negativo.
4. **[`04-calculadora-folha-pagamento/`](./faculdade/04-calculadora-folha-pagamento/README.md):** Processador modularizado em funções puras acompanhado de suíte automatizada **`pytest`**.

---

## ⚡ Como Usar Este Repositório (Para Estudantes e Comunidade)

### 1. Clonar e Preparar (ou clicar em *"Use this template"* no GitHub)
```bash
git clone https://github.com/gaabybellos/python-do-zero.git
cd python-do-zero
python -m pip install -e ".[dev]"
```

### 2. Iniciar seus Estudos com Qualquer Assistente de IA
Este repositório já vem configurado para **Antigravity**, **Claude Code** (`.claude/`), **Codex / Cursor** (`.codex/` e `AGENTS.md`). Basta abrir o projeto e enviar no chat:

> *"Olá! Quero começar meus estudos do zero. Chame o `responsavel-repositorio` e o `professor` para iniciarmos o Módulo 01 (`PYZ-SEQ-N1-001`)."*

### 3. Reiniciar o Progresso do Zero (Quando Quiser)
```bash
python scripts/resetar_progresso.py
```

### 4. Executar o Verificador PEP 8 (`ruff`) e os Testes Automatizados (`pytest`)
```bash
ruff check .
pytest -v
```

---

## 📚 Documentos de Referência

- [`AGENTS.md`](./AGENTS.md): Regras oficiais dos 4 agentes e contrato pedagógico.
- [`Docs/00-preparacao-ambiente.md`](./Docs/00-preparacao-ambiente.md): Guia de instalação do Python para iniciantes absolutos.
- [`Docs/guia-boas-praticas-python.md`](./Docs/guia-boas-praticas-python.md): Guia rápido de código limpo (PEP 8 e Clean Code).
- [`Docs/guia-validacao-e-qa.md`](./Docs/guia-validacao-e-qa.md): Guia prático de Programação Defensiva, Valores Limite (BVA) e mentalidade de QA.
- [`Docs/mapa-modulos.md`](./Docs/mapa-modulos.md): Arquitetura completa dos módulos e pastas.
- [`CONTRIBUTING.md`](./CONTRIBUTING.md): Como contribuir com novos exercícios e melhorias.
