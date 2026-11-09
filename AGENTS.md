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
- `PYZ-FAC`: Tarefas e Trabalhos da Faculdade (`faculdade/`)

Níveis de dificuldade:

- `N1`: Fixação (conceito direto)
- `N2`: Prática (combinação de lógica)
- `N3`: Desafio (problema completo do mundo real)
- `FAC`: Atividade Acadêmica da Faculdade

Exemplo: `PYZ-SEQ-N1-001` (Primeiro exercício de nível 1 do módulo Sequencial) ou `PYZ-FAC-001` (Primeira tarefa da faculdade).

---

## Modo Especial: Tarefas de Faculdade (`skills/tarefas-faculdade/SKILL.md`)

Quando o aluno trouxer uma **tarefa, lista de exercícios ou trabalho da faculdade**, os agentes atuam em modo de **Resolução Executada + Aula Explicativa Detalhada**, criando **uma pasta única para cada tarefa** em `faculdade/<NN-nome-da-tarefa>/` que concentra todas as subpastas daquela atividade:

1. **`faculdade/<NN-nome-da-tarefa>/README.md`**: Explica o que há em cada subpasta da tarefa e traz instruções claras de **como executar o código** no terminal.
2. **`faculdade/<NN-nome-da-tarefa>/01-enunciado/`**: Salvar o enunciado original (`enunciado.md`) e restrições do professor da faculdade.
3. **`faculdade/<NN-nome-da-tarefa>/02-estudo-e-explicacao/`**:
   - Criar `explicacao-detalhada-logica.md` (usando `Docs/templates/template-explicacao-faculdade.md`) explicando detalhadamente **o que foi feito**, **por que foi feito** e **como fazer do zero** (decomposição E-P-S, passo a passo lógico, Teste de Mesa e perguntas que o professor pode fazer na arguição/prova).
   - Criar `codigo_comentado_aula.py` com comentários didáticos linha por linha para estudo do aluno.
4. **`faculdade/<NN-nome-da-tarefa>/03-entrega-professor/`**:
   - Subpasta **100% limpa**, pronta para o aluno copiar/compactar e enviar ao professor da faculdade.
   - Contém apenas o(s) arquivo(s) `.py` final(is), executado(s) e testado(s), respeitando o nível de conhecimento ensinado na disciplina e as boas práticas de código limpo (sem marcações de IA ou rascunhos).

---

## Templates Obrigatórios

- `Docs/templates/template-aula-conceito.md` (uso do `professor`)
- `Docs/templates/template-raciocinio-logico.md` (uso do `agente-logica` com o aluno)
- `Docs/templates/template-revisao-codigo.md` (uso do `agente-desenvolvimento`)
- `Docs/templates/template-explicacao-faculdade.md` (uso conjunto nas tarefas de faculdade)

---

## Repositórios de Referência Utilizados na Base Curricular

- **Trilha Didática em Português:** `RafaelFino/python-basics` e `WoMakersCode/intro-ao-python`
- **Desafios de Lógica Clássicos:** `isquicha/exercicios-logica-python` (Wiki Python Brasil)
- **Validação e Prática Guiada:** `4GeeksAcademy/python-beginner-programming-exercises`
- **Progressão em 3 Níveis:** `Asabeneh/30-Days-Of-Python`
