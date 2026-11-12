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

## 💡 Como Nasceu Este Projeto (História e Propósito)

Este repositório nasceu de uma necessidade real em família: **ele foi criado inicialmente para ajudar meu sogro nos estudos da faculdade**, guiando-o nos primeiros passos da lógica de programação e do Python de forma didática, paciente e estruturada.

Ao unir essa mentoria passo a passo com a minha experiência na área de **Qualidade de Software (QA)** - ensinando desde cedo a validar entradas, testar limites e escrever código limpo, percebi que o material tinha ficado rico demais para ficar guardado. Por isso, adaptei todos os exemplos e estudos de caso para cenários autorais e abertos, e **resolvi publicar este repositório como Open Source para ajudar outras pessoas** que também estão começando do zero absoluto na programação ou na faculdade.

---

## 🚀 Por Que Este Repositório é Diferente? (Abordagem QA-First)

A maioria dos materiais para iniciantes ensina apenas o **"Caminho Feliz" (*Happy Path*)** - códigos que quebram assim que o usuário digita `1,5` com vírgula em vez de `1.5`, aperta `Enter` vazio ou digita um número negativo.

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

## ⚡ Como Usar Este Repositório (Guia Passo a Passo)

Você pode usar este projeto de **3 maneiras complementares**: estudando por conta própria pelas apostilas e exercícios, estudando com mentoria dos **4 Agentes de IA**, ou praticando **Engenharia de Qualidade (QA)** nos Estudos de Caso.

### Passo 0: Instalação e Preparação Inicial

> 💡 **Nunca instalou o Python?** Siga primeiro o passo a passo ilustrado em [`Docs/00-preparacao-ambiente.md`](./Docs/00-preparacao-ambiente.md).

1. **Clone o repositório** (ou clique no botão verde ***"Use this template"*** no GitHub para criar sua própria cópia):
   ```bash
   git clone https://github.com/gaabybellos/python-do-zero.git
   cd python-do-zero
   ```
2. **Instale as ferramentas de qualidade (`pytest` e `ruff`):**
   ```bash
   python -m pip install -e ".[dev]"
   ```
3. **Inicialize seu arquivo de progresso local** (`Docs/progresso-local.md`, que é ignorado pelo Git para não sujar seu `git status`):
   ```bash
   python scripts/resetar_progresso.py
   ```

---

### 📖 Modo 1: Estudo Autônomo (Sem IA, direto pelos materiais e terminal)

Ideal para quem quer ler a teoria com calma, executar exemplos comentados e resolver cada exercício passo a passo:

1. **Leia a Base Fundamental:**
   - Comece por [`Docs/01-o-que-e-python-fundamentos.md`](./Docs/01-o-que-e-python-fundamentos.md) e consulte o [`Docs/glossario-programacao-e-qa.md`](./Docs/glossario-programacao-e-qa.md) sempre que encontrar um termo novo.
2. **Estude a Apostila do Módulo e Execute os Exemplos Análogos:**
   - Leia [`modulos/01-introducao-e-variaveis/conteudo-teorico.md`](./modulos/01-introducao-e-variaveis/conteudo-teorico.md).
   - Rode os exemplos prontos no terminal para ver o Python em ação (sem entregar a resposta dos exercícios):
     ```bash
     python modulos/01-introducao-e-variaveis/exemplos/exemplo_01_variaveis_e_tipos.py
     python modulos/01-introducao-e-variaveis/exemplos/exemplo_02_entrada_e_conversao.py
     python modulos/01-introducao-e-variaveis/exemplos/exemplo_03_desconto_produto_qa.py
     ```
3. **Planeje a Lógica e o Teste de Mesa Antes de Codificar:**
   - Abra o arquivo de raciocínio do exercício (ex.: [`modulos/01-introducao-e-variaveis/raciocinio/PYZ-SEQ-N1-001.md`](./modulos/01-introducao-e-variaveis/raciocinio/PYZ-SEQ-N1-001.md)).
   - Preencha **Entrada**, **Processamento**, **Saída**, o **Pseudocódigo** e os **3 cenários do Teste de Mesa** (Caminho Feliz, Valor Limite e Entrada Inválida).
4. **Programe e Execute no Terminal:**
   - Abra o esqueleto do exercício (ex.: [`modulos/01-introducao-e-variaveis/exercicios/ex001_boas_vindas_soma.py`](./modulos/01-introducao-e-variaveis/exercicios/ex001_boas_vindas_soma.py)), substitua os blocos `# TODO` pelo seu código e execute:
     ```bash
     python modulos/01-introducao-e-variaveis/exercicios/ex001_boas_vindas_soma.py
     ```
5. **Valide seu Código com Padrão Profissional (PEP 8 e Revisão):**
   - Compare sua solução com a revisão modelo em [`modulos/01-introducao-e-variaveis/revisoes/PYZ-SEQ-N1-001-review-exemplo.md`](./modulos/01-introducao-e-variaveis/revisoes/PYZ-SEQ-N1-001-review-exemplo.md) e rode o linter:
     ```bash
     ruff check .
     ```

---

### 🤖 Modo 2: Estudo Guiado por IA (Com os 4 Agentes Socráticos)

O repositório já vem pré-configurado para **Google Antigravity**, **Claude Code** (`.claude/agents/`) e **Codex / Cursor** (`.codex/agents/` e `AGENTS.md`). Se você usa **ChatGPT, Gemini ou Claude na Web**, basta anexar o arquivo [`AGENTS.md`](./AGENTS.md) no início da conversa.

Copie e cole os prompts abaixo conforme avança em cada exercício:

1. **Iniciar um Módulo ou Exercício (`responsavel-repositorio` + `professor`):**
   > *"Olá! Quero estudar o exercício `PYZ-SEQ-N1-001`. Siga o fluxo do `AGENTS.md`: chame o `responsavel-repositorio` para localizar os arquivos e o `professor` para me explicar o conceito com analogia e me fazer a pergunta socrática de verificação."*
2. **Validar seu Raciocínio e Teste de Mesa (`agente-logica`):**
   > *"Atue como `agente-logica`. Preenchi o arquivo de raciocínio do `PYZ-SEQ-N1-001` com Entrada, Processamento, Saída e Teste de Mesa (Caminho Feliz, Valor Limite BVA e Entrada Inválida). Revise minha lógica usando o Método Socrático sem me entregar código Python."*
3. **Tirar Dúvidas de Código ou Pedir Code Review (`agente-desenvolvimento`):**
   > *"Atue como `agente-desenvolvimento`. Implementei minha solução no arquivo do exercício `PYZ-SEQ-N1-001`. Faça o Code Review pedagógico verificando PEP 8 (`snake_case`, até 88 colunas), Clean Code e Validação Defensiva de QA."*

---

### 🧪 Modo 3: Prática com Estudos de Caso e Testes Automatizados (`pytest`)

Para ver como problemas completos combinam **Lógica + Clean Code + Testes Automatizados**:

1. **Leia o Problema:** Abra `01-enunciado/enunciado.md` dentro de um dos casos em [`estudos-de-caso/`](./estudos-de-caso/README.md) e tente resolver sozinho primeiro.
2. **Estude a Decomposição e o Código Explicado Linha a Linha:** Consulte a pasta `02-estudo-e-explicacao/` do estudo de caso.
3. **Execute o Sistema Interativo no Terminal:**
   ```bash
   python estudos-de-caso/01-sistema-boletim-academico/04-solucao-referencia/sistema_boletim_academico.py
   ```
4. **Rode a Suíte Completa de Testes (`pytest`) e o Verificador PEP 8 (`ruff`):**
   ```bash
   pytest -v
   ruff check .
   ```

---

## 🗂️ Estrutura Visual do Repositório

```text
python-do-zero/
├── AGENTS.md                        # Regras oficiais dos 4 Agentes de IA e fluxo socrático
├── pyproject.toml                   # Configuração do projeto, pytest e ruff (PEP 8)
├── Docs/                            # Apostilas de base, guias de QA/PEP 8 e templates
│   ├── 00-preparacao-ambiente.md    # Como instalar Python, VS Code, pytest e ruff do zero
│   ├── 01-o-que-e-python-fundamentos.md
│   ├── glossario-programacao-e-qa.md
│   ├── cheat-sheet-python-qa.md     # Consulta rápida de comandos e técnicas de QA
│   ├── guia-boas-praticas-python.md # Regras de PEP 8 e Clean Code
│   └── guia-validacao-e-qa.md       # BVA, Partição de Equivalência e Programação Defensiva
├── modulos/                         # Trilha progressiva (Módulos 01 a 06 — 34 exercícios)
│   └── 01-introducao-e-variaveis/   # Módulo 01 completo com teoria, exemplos, exercícios e revisão
├── estudos-de-caso/                 # 4 Estudos de Caso autorais com explicação e testes pytest
├── tests/                           # Testes de qualidade estrutural do repositório e PEP 8
└── scripts/resetar_progresso.py     # Cria/reseta seu progresso local (Docs/progresso-local.md)
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
