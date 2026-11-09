---
name: tarefas-faculdade
description: Executar tarefas e trabalhos de faculdade criando uma pasta única por tarefa contendo README (com instruções de execução), 01-enunciado, 02-estudo-e-explicacao e 03-entrega-professor.
---

# Resolução e Explicação de Tarefas de Faculdade (`tarefas-faculdade`)

## Propósito

Atender demandas reais da faculdade do aluno com **duplo objetivo**:
1. **Aprendizado Real:** Explicar em detalhes como o problema foi pensado, qual a lógica utilizada, o teste de mesa e o funcionamento de cada linha de código (para que o aluno saiba explicar ao professor e fazer sozinho na prova).
2. **Organização Unificada por Tarefa:** Concentrar tudo o que pertence a cada tarefa dentro de sua própria pasta (`faculdade/<NN-nome-da-tarefa>/`), dividida internamente em `01-enunciado/`, `02-estudo-e-explicacao/`, `03-entrega-professor/` e um `README.md` explicando cada item e como executar o programa.

---

## Estrutura Obrigatória de Pastas (`faculdade/<NN-nome-da-tarefa>/`)

Toda tarefa de faculdade recebe um identificador `PYZ-FAC-<NUMERO>` e **sua própria pasta** dentro de `faculdade/`:

```text
faculdade/
├── README.md                                      # Índice geral de todas as tarefas da faculdade
└── <NN-nome-da-tarefa>/                           # Pasta única da tarefa (ex.: 01-sistema-avaliacao-uvvon)
    ├── README.md                                  # Explica o que há em cada subpasta e COMO EXECUTAR o código
    ├── 01-enunciado/                              # Enunciado original e regras do professor
    │   └── enunciado.md
    ├── 02-estudo-e-explicacao/                    # Uso exclusivo do ALUNO (NÃO enviar ao professor)
    │   ├── explicacao-detalhada-logica.md         # Explicação passo a passo de como foi feito e por quê
    │   └── codigo_comentado_aula.py               # Código com comentários didáticos linha a linha
    └── 03-entrega-professor/                      # PASTA LIMPA PRONTA PARA COPIAR E ENVIAR
        └── <nome_do_script>.py                    # Código limpo, testado, em PEP 8 (sem metadados de IA)
```

---

## Fluxo de Execução de uma Tarefa de Faculdade

Quando o aluno enviar um enunciado ou tarefa da faculdade, siga obrigatoriamente estes 6 passos:

### Passo 1: Análise do Enunciado e Salvamento (`01-enunciado/`)
- Identifique todas as entradas, regras de negócio, saídas exigidas e **restrições do professor da faculdade**.
- Salve o enunciado em `faculdade/<NN-nome-da-tarefa>/01-enunciado/enunciado.md`.

### Passo 2: Construção e Execução do Código Limpo (`03-entrega-professor/`)
- Crie o código final dentro de `faculdade/<NN-nome-da-tarefa>/03-entrega-professor/<nome_do_script>.py`.
- Regras para o arquivo de entrega:
  - Seguir estritamente o nível de Python ensinado na disciplina do aluno (não usar recursos avançados se a matéria for de algoritmos básicos).
  - Aplicar boas práticas (nomes claros em `snake_case`, indentação de 4 espaços, organização limpa).
  - Sem marcadores como `# Gerado por IA` ou `# ID: PYZ-...`.
  - **Executar e testar o código** no terminal com diferentes entradas para garantir que funciona 100% sem erros.

### Passo 3: Criação da Versão Comentada Linha a Linha (`02-estudo-e-explicacao/`)
- Crie `faculdade/<NN-nome-da-tarefa>/02-estudo-e-explicacao/codigo_comentado_aula.py` explicando o papel de cada variável, condição e laço.

### Passo 4: Documento de Explicação Detalhada (`02-estudo-e-explicacao/explicacao-detalhada-logica.md`)
- Utilizando o template `Docs/templates/template-explicacao-faculdade.md`, crie o guia completo contendo:
  1. **Traduzindo o Enunciado:** O que o professor realmente pediu, em palavras simples.
  2. **Como Pensar para Resolver (A Lógica do Zero):** Decomposição em Entrada $\rightarrow$ Processamento $\rightarrow$ Saída e o algoritmo em português.
  3. **Explicação Bloco a Bloco:** O que cada parte do código faz e *por que* foi escolhida aquela estrutura.
  4. **Teste de Mesa Passo a Passo:** Tabela mostrando os valores das variáveis mudando a cada linha.
  5. **Perguntas que o Professor Pode Fazer:** 2 ou 3 perguntas comuns de arguição/prova sobre esse código com as respostas.

### Passo 5: Criação do `README.md` da Tarefa (`faculdade/<NN-nome-da-tarefa>/README.md`)
- Crie um `README.md` na raiz da pasta da tarefa explicando claramente:
  - O que tem em cada uma das 3 subpastas (`01-enunciado/`, `02-estudo-e-explicacao/`, `03-entrega-professor/`).
  - **Como executar o código** no terminal (comandos `python` / `py` e exemplo de como interagir com as entradas do programa).

### Passo 6: Registro pelo `responsavel-repositorio`
- Atualizar `faculdade/README.md` e `Docs/progresso-aluno.md` na seção de **Tarefas de Faculdade**.
