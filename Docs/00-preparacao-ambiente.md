# Módulo 00 — Preparação do Ambiente do Zero Absoluto (`00-preparacao-ambiente.md`)

Se você nunca programou antes, este guia mostra passo a passo como preparar seu computador para rodar os exercícios deste repositório sem dor de cabeça.

---

## Passo 1: Instalar o Python (3.10 ou superior)

1. Acesse o site oficial: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Baixe a versão mais recente do **Python 3**.
3. **⚠️ ATENÇÃO (No Windows):** Na primeira tela do instalador, **marque obrigatoriamente a caixinha `"Add python.exe to PATH"`** na parte inferior da janela antes de clicar em *"Install Now"*.

---

## Passo 2: Testar se o Python Está Funcionando no Terminal

Abra o terminal do seu computador (**PowerShell** ou **Prompt de Comando** no Windows, ou **Terminal** no Linux/Mac) e digite:

```powershell
python --version
```

> **Dica para Windows:** Se aparecer uma mensagem de erro ou abrir a Microsoft Store, teste o lançador oficial do Windows:
> ```powershell
> py --version
> ```
> Se o `py` mostrar algo como `Python 3.12.x`, você pode usar `py` no lugar de `python` em todos os comandos!

---

## Passo 3: Clonar este Repositório e Instalar Ferramentas de Qualidade (Opcional, Recomendado)

Na pasta onde você guarda seus estudos, rode no terminal:

```powershell
git clone https://github.com/gaabybellos/python-do-zero.git
cd python-do-zero
```

Para instalar o **Pytest** (testes automatizados) e o **Ruff** (verificador de boas práticas PEP 8):

```powershell
python -m pip install -e ".[dev]"
```

---

## Passo 4: Como Executar Qualquer Exercício ou Tarefa

Para rodar um arquivo `.py`, basta passar o caminho dele para o comando `python` (ou `py`):

```powershell
# Exemplo 1: Rodando o primeiro exercício do Módulo 01
python modulos/01-introducao-e-variaveis/exercicios/ex001_boas_vindas_soma.py

# Exemplo 2: Rodando a Tarefa 01 da pasta Faculdade
python faculdade/01-sistema-boletim-academico/03-entrega-professor/sistema_boletim_academico.py
```

Para rodar os testes automatizados de qualidade (QA) e o verificador de código limpo (PEP 8):

```powershell
# Rodar todos os testes automatizados
pytest -v

# Verificar se todo o código segue a PEP 8 e Clean Code
ruff check .
```
