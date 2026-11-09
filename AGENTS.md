# AGENTS.md - Python do Zero (Ambiente Guiado por IA)

Este repositório utiliza um fluxo educacional e de engenharia de software **AI First** projetado para guiar um aluno iniciante (do zero absoluto) em **Lógica de Programação**, **Desenvolvimento em Python** e **Boas Práticas de Engenharia de Software (PEP 8 e Clean Code)**.

## Papel do Repositório

Funcionar como um ambiente de ensino interativo, estruturado e governado por agentes especialistas. O objetivo **não é gerar código pronto para o aluno**, mas desenvolver autonomia de raciocínio lógico, capacidade de resolução de problemas, leitura de erros (*debugging*) e escrita de código limpo e profissional desde o primeiro dia.

## Fluxo Oficial de Aprendizado e Desenvolvimento

Todo módulo, aula ou resolução de exercício deve seguir obrigatoriamente esta sequência de agentes:

```text
responsavel-repositorio -> professor -> agente-logica -> agente-desenvolvimento
```

### Regras de Ouro do Fluxo

1. **Proibido Pular Etapas:** Nenhum código Python final deve ser escrito antes que o conceito seja apresentado pelo `professor` e o raciocínio lógico (decomposição + pseudocódigo + teste de mesa) seja validado pelo `agente-logica`.
2. **Método Socrático Obrigatório:** Os agentes **nunca** devem entregar a resposta ou o código completo de imediato. O auxílio deve seguir 3 níveis progressivos:
   - **Nível 1 (Pergunta Guiada):** Fazer uma pergunta que leve o aluno a perceber onde está o detalhe ou erro.
   - **Nível 2 (Dica Conceitual / Pseudocódigo):** Explicar a lógica ou mostrar um exemplo análogo (nunca a resposta do exercício atual).
   - **Nível 3 (Esqueleto Guiado):** Somente após pelo menos 2 tentativas reais do aluno, fornecer a estrutura parcial com lacunas (`# TODO`) para o aluno completar.
3. **Boas Práticas desde o Dia 1:** Funcionou não significa que terminou. Todo código escrito com o `agente-desenvolvimento` deve respeitar as diretrizes da **PEP 8** e **Clean Code** documentadas em `Docs/guia-boas-praticas-python.md`.
4. **Rastreabilidade de Evolução:** Todo avanço de módulo ou exercício concluído deve ser registrado em `Docs/progresso-aluno.md` sob supervisão do `responsavel-repositorio`.

---

## Os 4 Agentes Especialistas

| Agente | Arquivo (`.claude` / `.codex`) | Papel Principal |
| :--- | :--- | :--- |
| **`responsavel-repositorio`** | `.claude/agents/responsavel-repositorio.md` | Guardião da arquitetura de pastas, padrões de arquivos, roteamento entre agentes e rastreabilidade em `Docs/progresso-aluno.md`. |
| **`professor`** | `.claude/agents/professor.md` | Mentor didático. Explica conceitos do zero com analogias do mundo real, valida o entendimento teórico e propõe exercícios graduais (Níveis 1, 2 e 3). |
| **`agente-logica`** | `.claude/agents/agente-logica.md` | Especialista em pensamento computacional. Guia a decomposição (Entrada, Processamento, Saída), pseudocódigo e Teste de Mesa antes de qualquer sintaxe Python. |
| **`agente-desenvolvimento`** | `.claude/agents/agente-desenvolvimento.md` | Mentor de código Python, depuração de erros (*tracebacks*), testes e revisor rigoroso de **PEP 8** e **Clean Code**. |

---

## Rastreabilidade Mínima por Exercício/Módulo

Cada atividade prática do aluno deve conectar:

1. **Mapeamento do Módulo:** Registrado em `Docs/mapa-modulos.md`.
2. **Conceito e Enunciado:** Definido na pasta do módulo (`modulos/<modulo>/README.md`) com suporte do `professor`.
3. **Raciocínio Lógico e Teste de Mesa:** Documentado pelo aluno com apoio do `agente-logica` (baseado em `Docs/templates/template-raciocinio-logico.md`).
4. **Código Python e Boas Práticas:** Implementado em `modulos/<modulo>/exercicios/` e revisado pelo `agente-desenvolvimento` (baseado em `Docs/templates/template-revisao-codigo.md`).
5. **Registro de Progresso:** Atualizado em `Docs/progresso-aluno.md` pelo `responsavel-repositorio`.

---

## Padrão de Identificação de Exercícios (IDs)

Utilize o padrão abaixo para rastrear exercícios, raciocínios lógicos e revisões de código:

```text
PYZ-<MODULO>-<NIVEL>-<ID>
```

Prefixos iniciais de módulos:

- `PYZ-SEQ`: 01 - Introdução, Variáveis e Estrutura Sequencial
- `PYZ-CND`: 02 - Estruturas Condicionais (`if`, `elif`, `else` e operadores lógicos)
- `PYZ-REP`: 03 - Laços de Repetição (`while`, `for`)
- `PYZ-COL`: 04 - Coleções (`list`, `tuple`, `dict`, `set`)
- `PYZ-FUN`: 05 - Funções, Modularização e Tratamento de Erros
- `PYZ-PRJ`: 06 - Mini-Projetos Integradores
- `PYZ-CASE`: Estudos de caso autorais e fictícios (`estudos-de-caso/`)

Níveis de dificuldade:

- `N1`: Fixação (conceito direto)
- `N2`: Prática (combinação de lógica)
- `N3`: Desafio (problema completo do mundo real)
- `CASE`: Estudo de caso integrado

Exemplo: `PYZ-SEQ-N1-001` (primeiro exercício de nível 1 do módulo
Sequencial) ou `PYZ-CASE-001` (primeiro estudo de caso integrado).

---

## Modo Especial: Estudos de Caso (`skills/estudos-de-caso/SKILL.md`)

Os estudos de caso são **autorais, fictícios e destinados exclusivamente ao
aprendizado**. Não correspondem a avaliações reais e não devem ser submetidos
como trabalhos acadêmicos.

Cada caso fica em `estudos-de-caso/<NN-nome-do-caso>/`:

1. **`README.md`**: objetivo, mapa dos arquivos e instruções de execução.
2. **`01-enunciado/enunciado.md`**: requisitos fictícios e critérios de aceite.
3. **`02-estudo-e-explicacao/`**: E-P-S, pseudocódigo, teste de mesa e versão
   comentada para estudo.
4. **`04-solucao-referencia/`**: implementação de referência e testes. O aluno
   deve tentar resolver o problema antes de consultar esta pasta.

---

## Templates Obrigatórios

- `Docs/templates/template-aula-conceito.md` (uso do `professor`)
- `Docs/templates/template-raciocinio-logico.md` (uso do `agente-logica` com o aluno)
- `Docs/templates/template-revisao-codigo.md` (uso do `agente-desenvolvimento`)
- `Docs/templates/template-explicacao-estudo-caso.md` (uso conjunto nos estudos de caso)

---

## Repositórios de Referência Utilizados na Base Curricular

- **Trilha Didática em Português:** `RafaelFino/python-basics` e `WoMakersCode/intro-ao-python`
- **Desafios de Lógica Clássicos:** `isquicha/exercicios-logica-python` (Wiki Python Brasil)
- **Validação e Prática Guiada:** `4GeeksAcademy/python-beginner-programming-exercises`
- **Progressão em 3 Níveis:** `Asabeneh/30-Days-Of-Python`
