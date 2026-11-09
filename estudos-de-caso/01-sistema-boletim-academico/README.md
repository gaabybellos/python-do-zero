# Estudo de Caso 01 — Sistema de Fechamento de Boletim (`PYZ-CASE-001`)

> **Aviso de Integridade:** Estudo de caso fictício e autoral criado exclusivamente para aprendizado. Não corresponde a uma avaliação acadêmica real e não deve ser submetido como trabalho escolar ou universitário.

Esta pasta reúne o material completo do **Estudo de Caso 01**, focado em **Laços de Repetição (`for` e `while`), Estruturas Condicionais (`if/elif/else`), Contadores e Validação Defensiva de Entradas (QA)**.

---

## 📂 O que há em cada subpasta?

```text
01-sistema-boletim-academico/
├── README.md                                  # Guia do caso (estrutura e como executar)
├── 01-enunciado/
│   └── enunciado.md                           # Requisitos fictícios e regras de negócio
├── 02-estudo-e-explicacao/                    # Material de estudo detalhado
│   ├── explicacao-detalhada-logica.md         # Decomposição E-P-S, passo a passo e BVA
│   └── codigo_comentado_aula.py               # Código comentado explicando cada bloco
└── 04-solucao-referencia/                     # Solução de referência e testes pytest
    ├── sistema_boletim_academico.py           # Implementação limpa seguindo a PEP 8
    └── test_sistema_boletim_academico.py      # Suíte de testes automatizados (pytest)
```

---

## ▶️ Como Executar o Código e os Testes

Abra o terminal na raiz do repositório (`python-do-zero`) e execute:

### 1. Executar a solução interativa:
```powershell
python estudos-de-caso/01-sistema-boletim-academico/04-solucao-referencia/sistema_boletim_academico.py
```

### 2. Executar os testes automatizados (`pytest`):
```powershell
pytest estudos-de-caso/01-sistema-boletim-academico/04-solucao-referencia/test_sistema_boletim_academico.py -v
```
