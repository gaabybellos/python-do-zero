# Glossário de Programação e Qualidade (QA) para Iniciantes (`glossario-programacao-e-qa.md`)

Este glossário traduz, em linguagem simples e direta, os termos técnicos que você encontrará ao longo dos módulos.

---

## 1. Fundamentos de Programação e Python

| Termo | O que significa na prática? | Exemplo Simples |
| :--- | :--- | :--- |
| **Algoritmo** | Sequência finita e lógica de passos para resolver um problema. | Uma receita de bolo ou o passo a passo para somar dois números. |
| **Programa / Script (`.py`)** | Um arquivo de texto com extensão `.py` contendo instruções escritas em Python para o computador executar. | `ex001_boas_vindas_soma.py` |
| **Terminal (Console)** | A tela de texto (como o PowerShell ou Prompt de Comando) onde digitamos comandos para rodar nossos programas. | `python meu_programa.py` |
| **Variável** | Um espaço na memória do computador com uma etiqueta (`nome_em_snake_case`) usado para guardar um valor. | `idade_aluno = 20` |
| **Constante** | Um valor fixo de regra de negócio que não muda durante a execução, escrito em letras maiúsculas (`UPPER_SNAKE_CASE`). | `TAXA_SERVICO = 0.10` |
| **Tipo de Dado (*Type*)** | Define que espécie de informação está guardada: texto (`str`), inteiro (`int`), decimal (`float`) ou lógico (`bool`). | `"Ana"` (`str`), `10` (`int`), `9.5` (`float`), `True` (`bool`). |
| **Indentação** | Os **4 espaços** no início de uma linha que indicam ao Python quais comandos pertencem a um bloco (`def`, `if`, `for`, `while`). | Todo código dentro de `def main():` começa com 4 espaços. |
| **Função (`def`)** | Um bloco de código reutilizável com nome próprio que executa uma tarefa específica. | `def calcular_dobro(numero):` |
| **Retorno (`return`)** | O resultado final que uma função devolve para quem a chamou (diferente de `print`, que apenas mostra texto na tela). | `return numero * 2` |
| **Traceback (Rastro de Erro)** | A mensagem que o Python exibe no terminal quando algo falha, indicando o arquivo, o número da linha e o tipo do erro. | `ValueError: could not convert string to float` |

---

## 2. Termos de Engenharia de Qualidade (QA) e Boas Práticas

| Termo de QA / Engenharia | O que significa na prática? | Por que importa desde o Dia 1? |
| :--- | :--- | :--- |
| **PEP 8** | O guia oficial de estilo do Python (nomes em `snake_case`, 4 espaços de indentação, linhas de até 88 caracteres). | Deixa o código limpo, padronizado e fácil de ler por qualquer pessoa. |
| **Teste de Mesa** | Simular o programa manualmente em uma tabela (linha por linha) anotando o valor de cada variável antes de programar. | Permite encontrar erros de raciocínio antes mesmo de abrir o Python. |
| **Caminho Feliz (*Happy Path*)** | Testar o programa com entradas normais e corretas que o usuário deveria digitar. | Confirma que a regra principal do programa funciona. |
| **Valor Limite (*Boundary Value - BVA*)** | Testar exatamente nas fronteiras de uma regra (ex.: se aprova com `>= 7.0`, testar `6.9`, `7.0` e `7.1`). | A maioria dos erros de lógica acontece por trocar `>` por `>=` ou `<` por `<=`. |
| **Teste Negativo (*Negative Test*)** | Testar o programa com entradas erradas ou inesperadas (letras no lugar de números, números negativos, vazio). | Garante que o programa avise o usuário em vez de travar. |
| **Programação Defensiva** | Escrever o código prevendo erros de digitação do usuário (como trocar vírgula por ponto ou usar `try/except`). | Impede que o programa quebre durante o uso real. |
| **Linter (`ruff`)** | Ferramenta automática que analisa o código em busca de erros de estilo (PEP 8) ou variáveis não utilizadas. | Funciona como um revisor automático instantâneo. |
| **Teste Automatizado (`pytest`)** | Um script que executa suas funções automaticamente com várias entradas e confere se o resultado está correto (`assert`). | Permite validar em segundos se uma alteração não quebrou nada. |
