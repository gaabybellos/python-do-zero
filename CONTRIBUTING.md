# Guia de Contribuição (`CONTRIBUTING.md`)

Obrigado pelo interesse em contribuir com o **Python do Zero (QA-First & AI-Guided)**! Este projeto é Open Source e foi criado para ajudar estudantes iniciantes a aprenderem Lógica de Programação, Python, Clean Code e Qualidade de Software desde o primeiro dia.

---

## Como Contribuir

1. **Faça um Fork** deste repositório.
2. **Crie uma Branch** para a sua melhoria:
   ```bash
   git checkout -b feat/minha-melhoria
   ```
3. **Respeite os Padrões de Qualidade e Integridade do Projeto:**
   - Todo código Python deve seguir a **PEP 8** (máximo de 88 caracteres por linha) e passar sem erros no `ruff check .`.
   - Toda entrada de usuário (`input()`) em soluções de referência deve aplicar **Programação Defensiva** (aceitar decimais com vírgula ou ponto via `.replace(",", ".")`, tratar `ValueError` e validar limites).
   - Novos estudos de caso em `estudos-de-caso/<NN-nome-do-caso>/` devem ser **100% autorais e fictícios** (nunca trabalhos acadêmicos reais) e conter:
     - `README.md` (explicando os arquivos e como executar)
     - `01-enunciado/enunciado.md` (com aviso de estudo de caso fictício)
     - `02-estudo-e-explicacao/explicacao-detalhada-logica.md` (com Teste de Mesa BVA)
     - `02-estudo-e-explicacao/codigo_comentado_aula.py`
     - `04-solucao-referencia/<script_limpo>.py` e `test_<script_limpo>.py`
4. **Rode os Testes Localmente antes do Pull Request:**
   ```bash
   ruff check .
   pytest -v
   ```
5. **Abra um Pull Request** descrevendo claramente o que foi adicionado ou aprimorado.
