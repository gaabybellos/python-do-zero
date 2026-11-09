# Python do Zero — Lógica, Clean Code & Mentalidade de QA Guiados por IA

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Version](https://img.shields.io/badge/Version-0.1.0-blue)
![Code Style: Ruff](https://img.shields.io/badge/Code%20Style-Ruff%20%2F%20PEP%208-261230?logo=ruff&logoColor=D7FF64)
![Tests: Pytest](https://img.shields.io/badge/QA%20Tests-Pytest-0A9EDC?logo=pytest&logoColor=white)
![Methodology: Shift-Left QA](https://img.shields.io/badge/Methodology-Shift--Left%20QA-success)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Bem-vindo ao **Python do Zero**! Este repositório Open Source é um ambiente de aprendizado estruturado para quem está começando a programar **do zero absoluto** e quer construir uma base sólida em:

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

## 📊 Estado Atual e Roadmap de Maturidade (`v0.1.0`)

| Área do Repositório | Estado Atual | Detalhes |
| :--- | :--- | :--- |
| **Guias de Base, Glossário e QA** | ✅ Disponível | Instalação do zero, fundamentos de Python, glossário, guia PEP 8, guia QA e Cheat Sheet inicial. |
| **Módulo 01 (`PYZ-SEQ`)** | ✅ Autossuficiente | Teoria escrita completa, 3 exemplos executáveis análogos, 6 exercícios (`2 N1, 2 N2, 2 N3`), revisão modelo e testes. |
| **Módulos 02 a 06** | 🚧 Esqueletos Guiados | Objetivos, 6 exercícios planejados por módulo (4 projetos no Módulo 06) e templates de raciocínio prontos; aulas escritas em expansão gradual. |
| **Estudos de Caso (`estudos-de-caso/`)** | ✅ Disponível (4 casos) | 4 estudos de caso autorais e fictícios com explicação, solução de referência e suítes `pytest`. |
| **Suíte de Testes & CI (`pytest` + `ruff`)** | ✅ Configurado | Testes unitários nos 4 estudos de caso, testes estruturais de PEP 8 e workflow GitHub Actions em matriz Python. |

---

## 🤖 Como Funciona o Ciclo de Estudo com os 4 Agentes

Para cada tema e exercício, você é acompanhado por **4 agentes especialistas** nesta sequência:

```text
responsavel-repositorio -> professor -> agente-logica -> agente-desenvolvimento
```

1. **`responsavel-repositorio` (Guardião do Repositório):**
   - Verifica onde você parou em [`Docs/progresso-aluno.md`](./Docs/progresso-aluno.md), organiza as pastas e indica qual módulo ou exercício iniciar.
2. **`professor` (Mentor Teórico):**
   - Explica o conceito do dia usando analogias simples do cotidiano, tira suas dúvidas pelo Método Socrático e propõe exercícios graduais.
3. **`agente-logica` (Especialista em Pensamento Computacional & QA no Teste de Mesa):**
   - Antes de você escrever qualquer código Python, ajuda a quebrar o problema em **Entrada $\rightarrow$ Processamento $\rightarrow$ Saída**, montar o algoritmo em português e preencher o **Teste de Mesa com Caminho Feliz, Valor Limite (BVA) e Entrada Inválida**.
4. **`agente-desenvolvimento` (Mentor Python, Clean Code & Revisão QA):**
   - Guia a tradução para Python, ensina a ler mensagens de erro (*Tracebacks*) e realiza o Code Review exigindo **PEP 8, Clean Code e Validação Defensiva**.

---

## 🗺️ Mapa Completo da Trilha e Roadmap

| Módulo | Pasta / Guia | Status | O que você vai aprender |
| :--- | :--- | :--- | :--- |
| **Módulo 00** | [`Docs/00-preparacao-ambiente.md`](./Docs/00-preparacao-ambiente.md) | ✅ Pronto | Instalação do Python, configuração do `PATH`, execução no terminal e uso do `pytest` e `ruff`. |
| **Fundamentos** | [`Docs/01-o-que-e-python-fundamentos.md`](./Docs/01-o-que-e-python-fundamentos.md) | ✅ Pronto | O que é um programa, arquivo `.py`, terminal, E-P-S, variáveis, tipos, indentação e erros. |
| **Módulo 01** | [`modulos/01-introducao-e-variaveis/`](./modulos/01-introducao-e-variaveis/README.md) | ✅ Autossuficiente | Variáveis semânticas (`snake_case`), tipos (`str`, `int`, `float`, `bool`), operadores, `input()` e `print()`. |
| **Módulo 02** | [`modulos/02-estruturas-condicionais/`](./modulos/02-estruturas-condicionais/README.md) | 🚧 Esqueletos | Decisões com `if`, `elif`, `else`, operadores lógicos e Análise de Valor Limite (BVA). |
| **Módulo 03** | [`modulos/03-lacos-de-repeticao/`](./modulos/03-lacos-de-repeticao/README.md) | 🚧 Esqueletos | Repetição com `while` e `for`, contadores, acumuladores e validação defensiva de entradas. |
| **Módulo 04** | [`modulos/04-colecoes-listas-dicionarios/`](./modulos/04-colecoes-listas-dicionarios/README.md) | 🚧 Esqueletos | Organização de dados em memória com Listas (`list`), Tuplas (`tuple`) e Dicionários (`dict`). |
| **Módulo 05** | [`modulos/05-funcoes-e-modularizacao/`](./modulos/05-funcoes-e-modularizacao/README.md) | 🚧 Esqueletos | Funções puras (`def`/`return`), *Type Hints*, `try/except` e testes automatizados com `pytest`. |
| **Módulo 06** | [`modulos/06-mini-projetos/`](./modulos/06-mini-projetos/README.md) | 🚧 Esqueletos | Aplicações completas de terminal integrando todos os conceitos com cobertura de testes. |
| **Estudos de Caso** | [`estudos-de-caso/`](./estudos-de-caso/README.md) | ✅ Pronto | 4 casos autorais e fictícios com requisitos, explicação, solução de referência e suíte `pytest`. |

---

## 🧪 Estudos de Caso Autorais (`estudos-de-caso/`)

Os quatro casos em [`estudos-de-caso/`](./estudos-de-caso/README.md) são **fictícios, autorais e criados exclusivamente para aprendizado**. Eles não correspondem a avaliações reais e não devem ser submetidos como trabalhos escolares ou universitários.

Cada caso contém requisitos (`01-enunciado/`), explicação detalhada e código comentado (`02-estudo-e-explicacao/`) e uma solução de referência acompanhada de testes `pytest` (`04-solucao-referencia/`). Tente resolver o problema antes de consultar a solução!

1. **[`01-sistema-boletim-academico/`](./estudos-de-caso/01-sistema-boletim-academico/README.md):** regras fictícias de notas, frequência, contadores e validação de decimais.
2. **[`02-analisador-consumo-energia/`](./estudos-de-caso/02-analisador-consumo-energia/README.md):** tarifação fictícia por faixas, acumuladores e extremos.
3. **[`03-controle-estoque-farmacia/`](./estudos-de-caso/03-controle-estoque-farmacia/README.md):** menu interativo, coleções, unicidade de código e estoque não negativo.
4. **[`04-calculadora-folha-pagamento/`](./estudos-de-caso/04-calculadora-folha-pagamento/README.md):** regras fictícias em funções puras com testes `pytest`.

---

## ⚡ Como Usar Este Repositório (Para Estudantes e Comunidade)

### 1. Clonar e Preparar (ou clicar em *"Use this template"* no GitHub)
```bash
git clone https://github.com/gaabybellos/python-do-zero.git
cd python-do-zero
python -m pip install -e ".[dev]"
```

### 2. Iniciar ou Reiniciar seu Progresso Pessoal
Para criar seu arquivo de progresso local (`Docs/progresso-local.md`, ignorado pelo Git para não sujar seu `git status`):
```bash
python scripts/resetar_progresso.py
```

### 3. Estudar pelo Conteúdo Escrito ou com Qualquer Assistente de IA
- **Estudo Autônomo:** Comece lendo [`Docs/01-o-que-e-python-fundamentos.md`](./Docs/01-o-que-e-python-fundamentos.md) e [`modulos/01-introducao-e-variaveis/conteudo-teorico.md`](./modulos/01-introducao-e-variaveis/conteudo-teorico.md).
- **Estudo Guiado por IA:** Configurado para **Antigravity**, **Claude Code** (`.claude/`) e **Codex / Cursor** (`.codex/` e `AGENTS.md`). Basta abrir o projeto e enviar no chat:
  > *"Olá! Quero começar meus estudos do zero. Chame o `responsavel-repositorio` e o `professor` para iniciarmos o Módulo 01 (`PYZ-SEQ-N1-001`)."*

### 4. Executar o Verificador PEP 8 (`ruff`) e os Testes Automatizados (`pytest`)
```bash
ruff check .
pytest -v
```

---

## 📚 Documentos de Referência

- [`AGENTS.md`](./AGENTS.md): Regras oficiais dos 4 agentes e contrato pedagógico.
- [`Docs/00-preparacao-ambiente.md`](./Docs/00-preparacao-ambiente.md): Guia de instalação do Python para iniciantes absolutos.
- [`Docs/01-o-que-e-python-fundamentos.md`](./Docs/01-o-que-e-python-fundamentos.md): Fundamentos de programas, arquivos `.py`, terminal, variáveis e erros.
- [`Docs/glossario-programacao-e-qa.md`](./Docs/glossario-programacao-e-qa.md): Glossário de termos de programação e QA para iniciantes.
- [`Docs/cheat-sheet-python-qa.md`](./Docs/cheat-sheet-python-qa.md): Folha de consulta rápida dos comandos ensinados.
- [`Docs/guia-boas-praticas-python.md`](./Docs/guia-boas-praticas-python.md): Guia rápido de código limpo (PEP 8 e Clean Code).
- [`Docs/guia-validacao-e-qa.md`](./Docs/guia-validacao-e-qa.md): Guia prático de Programação Defensiva, Valores Limite (BVA) e mentalidade de QA.
- [`Docs/mapa-modulos.md`](./Docs/mapa-modulos.md): Arquitetura completa dos módulos e pastas.
- [`CONTRIBUTING.md`](./CONTRIBUTING.md): Como contribuir com novos exercícios e melhorias.
- [`SECURITY.md`](./SECURITY.md): Política de segurança e reporte de vulnerabilidades.
