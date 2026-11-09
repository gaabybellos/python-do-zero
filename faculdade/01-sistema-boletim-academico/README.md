# Tarefa 01 — Sistema de Fechamento de Boletim Acadêmico (`PYZ-FAC-001`)

Esta pasta reúne **todo o material da Tarefa 01 da faculdade** em um único lugar, estruturado para estudo de **Laços de Repetição (`for` e `while`), Estruturas Condicionais (`if/elif/else`), Contadores e Validação Defensiva de Entradas (QA)**.

---

## 📂 O que tem em cada subpasta?

```text
01-sistema-boletim-academico/
├── README.md                              # Este guia da tarefa (estrutura e como executar)
├── 01-enunciado/
│   └── enunciado.md                       # Enunciado original e regras de negócio
├── 02-estudo-e-explicacao/                # MATERIAL DE ESTUDO (Não enviar ao professor)
│   ├── explicacao-detalhada-logica.md     # Decomposição E-P-S, passo a passo, Teste de Mesa (BVA) e dicas
│   └── codigo_comentado_aula.py           # Código comentado linha por linha explicando cada comando
└── 03-entrega-professor/                  # PASTA LIMPA PRONTA PARA ENVIAR AO PROFESSOR
    └── sistema_boletim_academico.py       # Código final limpo, testado e seguindo a PEP 8
```

---

## ▶️ Como Executar o Código

Abra o terminal na raiz do repositório (`python-do-zero`) e execute:

### Opção 1: Executar a versão limpa de entrega
```powershell
python faculdade/01-sistema-boletim-academico/03-entrega-professor/sistema_boletim_academico.py
```

### Opção 2: Executar a versão comentada de estudo
```powershell
python faculdade/01-sistema-boletim-academico/02-estudo-e-explicacao/codigo_comentado_aula.py
```

> **Dica para Windows:** Caso o comando `python` não funcione no seu terminal, utilize `py`:
> ```powershell
> py faculdade/01-sistema-boletim-academico/03-entrega-professor/sistema_boletim_academico.py
> ```

### Validações de Qualidade (QA) implementadas:
- Aceita decimais tanto com **vírgula (`1,5`)** quanto com **ponto (`1.5`)**.
- Bloqueia entradas vazias (`Enter` direto), espaços extras ou letras (`"abc"`), solicitando nova digitação sem encerrar o programa com `ValueError`.
- Garante que cada nota e a frequência respeitem estritamente os limites definidos no enunciado.
