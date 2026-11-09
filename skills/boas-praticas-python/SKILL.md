---
name: boas-praticas-python
description: Aplicar regras de desenvolvimento profissional em Python (PEP 8, Clean Code, nomenclatura semântica, funções limpas e leitura de erros) para iniciantes.
---

# Boas Práticas de Desenvolvimento em Python (`boas-praticas-python`)

## Propósito

Ensinar o aluno a escrever código limpo, legível e profissional desde o primeiro script, evitando vícios comuns de iniciantes.

## Regras Essenciais de Código

1. **Nomenclatura Semântica e PEP 8:**
   - Variáveis e funções: sempre em `snake_case` e com nomes que revelem a intenção (`idade_usuario`, `calcular_media_final()`).
   - Constantes: sempre em `UPPER_SNAKE_CASE` no topo do arquivo (`TAXA_DESCONTO = 0.15`, `IDADE_MINIMA_CNH = 18`).
   - **Proibido:** Nomes de uma letra ou sem significado (`a`, `b`, `x`, `n1`, `n2`, `aux`, `var1`), exceto índices curtos se realmente necessário (preferindo ainda `for indice in ...` ou `for item in ...` para iniciantes).

2. **Evitar Números Mágicos:**
   - Nunca deixar números soltos em condições ou fórmulas sem explicação (`if nota >= 7:`). Extraia para uma constante nomeada (`MEDIA_APROVACAO = 7.0`).

3. **Simplicidade e Responsabilidade Única (Clean Code):**
   - Cada função deve fazer **apenas uma tarefa**.
   - Separar funções que **calculam/processam** de trechos que pedem dados com `input()` ou imprimem com `print()`. Isso permite testar a lógica facilmente!

4. **Leitura Guiada de Erros (Debugging):**
   - Ao encontrar um *Traceback*, ensine o aluno a ler:
     1. **A última linha:** Qual é o tipo do erro (`NameError`, `TypeError`, `ValueError`, `SyntaxError`, `IndentationError`) e a mensagem?
     2. **A linha indicada (`File ..., line X`):** O que está escrito exatamente nessa linha (ou na linha imediatamente anterior, no caso de `SyntaxError`)?

5. **Documentação e Tipagem Gradual:**
   - Comentários (`#`) devem explicar o **porquê** de uma regra, nunca repetir o óbvio.
   - Em funções (a partir do Módulo 05), incluir *Docstring* curta de 1 linha e *Type Hints* básicos (`def calcular_dobro(numero: int) -> int:`).
