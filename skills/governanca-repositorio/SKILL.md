---
name: governanca-repositorio
description: Garantir a organização estrutural, rastreabilidade de módulos e registro de evolução do aluno no repositório Python do Zero.
---

# Governança do Repositório (`governanca-repositorio`)

## Propósito

Utilize esta skill para manter o repositório limpo, organizado, padronizado e com rastreabilidade completa de tudo o que o aluno estuda e desenvolve.

## Fontes Obrigatórias

- `AGENTS.md`
- `Docs/mapa-modulos.md`
- `Docs/progresso-aluno.md`

## Regras de Organização

1. **Roteamento Obrigatório:** Antes de criar qualquer exercício ou arquivo de aula, verifique `Docs/mapa-modulos.md`.
2. **Nomenclatura de Arquivos:**
   - Pastas de módulos: `NN-nome-do-modulo` (ex.: `01-introducao-e-variaveis`).
   - Arquivos de raciocínio lógico: `modulos/<modulo>/raciocinio/PYZ-<MODULO>-<NIVEL>-<ID>.md`.
   - Arquivos de código Python: `modulos/<modulo>/exercicios/ex<ID>_<nome_descritivo>.py` (sempre em `snake_case`, sem acentos ou espaços).
   - Arquivos de revisão de código: `modulos/<modulo>/revisoes/PYZ-<MODULO>-<NIVEL>-<ID>-review.md`.
3. **Checklist de Conclusão de Exercício:**
   - [ ] Conceito estudado com o `professor`?
   - [ ] Raciocínio lógico e Teste de Mesa validados pelo `agente-logica`?
   - [ ] Código Python implementado pelo aluno e revisado em PEP 8 / Clean Code pelo `agente-desenvolvimento`?
   - [ ] Progresso registrado em `Docs/progresso-aluno.md`?
