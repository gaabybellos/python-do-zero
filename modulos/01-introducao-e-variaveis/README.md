# Módulo 01 — Introdução, Variáveis e Estrutura Sequencial (`PYZ-SEQ`)

- **Status do Módulo:** ✅ Autossuficiente (Teoria, Exemplos, 6 Exercícios e Revisão Modelo disponíveis)
- **Pré-requisitos:** Leitura de [`Docs/00-preparacao-ambiente.md`](../../Docs/00-preparacao-ambiente.md) e [`Docs/01-o-que-e-python-fundamentos.md`](../../Docs/01-o-que-e-python-fundamentos.md)

---

## 🧭 Navegação Rápida do Módulo 01

1. 📖 **[Aula Teórica Completa (`conteudo-teorico.md`)](./conteudo-teorico.md)**: Estude os conceitos de variáveis, tipos (`str`, `int`, `float`, `bool`), operadores aritméticos, `input()`, conversão de tipos e `print()` com *f-strings*.
2. 🧪 **[Exemplos Executáveis Análogos (`exemplos/`)](./exemplos/README.md)**: Rode 3 pequenos programas comentados por bloco antes de iniciar os exercícios.
3. 🧩 **[Raciocínio Lógico e Teste de Mesa (`raciocinio/`)](./raciocinio/PYZ-SEQ-N1-001.md)**: Preencha a decomposição E-P-S e os cenários de QA antes de codificar.
4. 💻 **Exercícios Práticos (`exercicios/`)**: Resolva os 6 exercícios graduais listados abaixo.
5. 🔍 **[Exemplo de Revisão de Código e QA (`revisoes/`)](./revisoes/PYZ-SEQ-N1-001-review-exemplo.md)**: Veja como o `agente-desenvolvimento` avalia PEP 8, Clean Code e casos de borda.

---

## 🎯 Objetivos de Aprendizado

1. Estruturar algoritmos sequenciais usando **Entrada $\rightarrow$ Processamento $\rightarrow$ Saída (E-P-S)**.
2. Nomear variáveis em `snake_case` e constantes em `UPPER_SNAKE_CASE` seguindo a **PEP 8**.
3. Utilizar corretamente os tipos primitivos (`str`, `int`, `float`, `bool`) e os operadores aritméticos (`+`, `-`, `*`, `/`, `//`, `%`, `**`).
4. Ler entradas do teclado com `input()`, higienizar decimais (`.strip().replace(",", ".")`), converter com `int()`/`float()` e formatar saídas com *f-strings* (`:.2f`).

---

## 🏋️ Lista de Exercícios do Módulo 01 (`2 N1 + 2 N2 + 2 N3`)

### Nível 1 — Fixação (Aplicação Direta)

#### 1. `PYZ-SEQ-N1-001` — Boas-vindas e Soma Simples
- **Enunciado:** Crie um programa que pergunte o nome do estudante e dois números inteiros. Ao final, mostre uma mensagem de boas-vindas personalizada com o nome dele e o resultado da soma dos dois números.
- **Critérios de Aceite (QA):**
  - Remover espaços extras do nome com `.strip()`.
  - Converter ambas as parcelas com `int()` para somar matematicamente (e não concatenar textos).
  - Funcionar corretamente com zero e números negativos.
- **Exemplo de Entrada:** Nome: `Gabriel` | 1º número: `10` | 2º número: `25`
- **Saída Esperada:** `Olá, Gabriel! A soma de 10 + 25 é 35.`
- **Arquivos:** [Raciocínio (`PYZ-SEQ-N1-001.md`)](./raciocinio/PYZ-SEQ-N1-001.md) | [Código (`ex001_boas_vindas_soma.py`)](./exercicios/ex001_boas_vindas_soma.py)

#### 2. `PYZ-SEQ-N1-002` — Antecessor, Sucessor e Dobro de um Número
- **Enunciado:** Crie um programa que leia um único número inteiro e exiba na tela o seu antecessor (`numero - 1`), o seu sucessor (`numero + 1`) e o seu dobro (`numero * 2`).
- **Critérios de Aceite (QA):**
  - Usar variáveis semânticas (`numero_digitado`, `antecessor`, `sucessor`, `dobro`).
  - Testar na fronteira do zero (`0` $\rightarrow$ antecessor `-1`, sucessor `1`, dobro `0`).
- **Exemplo de Entrada:** Número: `15`
- **Saída Esperada:** `Número: 15 | Antecessor: 14 | Sucessor: 16 | Dobro: 30`
- **Arquivos:** [Raciocínio (`PYZ-SEQ-N1-002.md`)](./raciocinio/PYZ-SEQ-N1-002.md) | [Código (`ex002_antecessor_sucessor.py`)](./exercicios/ex002_antecessor_sucessor.py)

---

### Nível 2 — Prática (Combinação de Conceitos e Formatação)

#### 3. `PYZ-SEQ-N2-003` — Média de Notas Escolares
- **Enunciado:** Crie um programa que receba 3 notas decimais (`float`) de um estudante, calcule a média aritmética simples e exiba o resultado formatado com **2 casas decimais** (`:.2f`).
- **Critérios de Aceite (QA):**
  - Aceitar notas digitadas tanto com ponto (`7.5`) quanto com vírgula (`7,5`).
  - Garantir o uso de parênteses na soma `(nota_1 + nota_2 + nota_3) / 3`.
- **Exemplo de Entrada:** Notas: `7,5`, `8.0`, `9,2`
- **Saída Esperada:** `A média das 3 avaliações é: 8.23`
- **Arquivos:** [Raciocínio (`PYZ-SEQ-N2-003.md`)](./raciocinio/PYZ-SEQ-N2-003.md) | [Código (`ex003_media_escolar.py`)](./exercicios/ex003_media_escolar.py)

#### 4. `PYZ-SEQ-N2-004` — Conversor de Medidas e Moeda com Taxa Fixa
- **Enunciado:** Crie um programa que leia uma distância em metros (`float`) e um valor em Reais (`R$`). Converta e exiba a distância em centímetros (`* 100`) e milímetros (`* 1000`), e converta o valor em Reais para Dólares utilizando a constante fixa didática `TAXA_DOLAR_FIXA = 5.00`.
- **Critérios de Aceite (QA):**
  - Declarar a constante `TAXA_DOLAR_FIXA = 5.00` em `UPPER_SNAKE_CASE` no topo do arquivo.
  - Exibir o valor convertido em dólares com 2 casas decimais (`US$ X.XX`).
- **Exemplo de Entrada:** Distância: `2.5` metros | Valor: `R$ 150.00`
- **Saída Esperada:** `2.50 m = 250.0 cm (2500.0 mm) | R$ 150.00 = US$ 30.00`
- **Arquivos:** [Raciocínio (`PYZ-SEQ-N2-004.md`)](./raciocinio/PYZ-SEQ-N2-004.md) | [Código (`ex004_conversor_medidas_moeda.py`)](./exercicios/ex004_conversor_medidas_moeda.py)

---

### Nível 3 — Desafio (Problemas Contextualizados)

#### 5. `PYZ-SEQ-N3-005` — Calculadora de Conta de Restaurante
- **Enunciado:** Crie um programa que leia o valor total de consumo em um restaurante (`float`) e a quantidade de pessoas na mesa (`int`). Calcule o valor da taxa de serviço de 10% (usando a constante `TAXA_SERVICO = 0.10`), o valor total com a taxa e quanto cada pessoa deverá pagar.
- **Critérios de Aceite (QA):**
  - Aceitar decimais com vírgula ou ponto no valor do consumo.
  - Exibir todos os valores monetários formatados com `R$ X.XX`.
- **Exemplo de Entrada:** Consumo: `200,00` | Pessoas: `4`
- **Saída Esperada:** `Taxa (10%): R$ 20.00 | Total: R$ 220.00 | Valor por pessoa: R$ 55.00`
- **Arquivos:** [Raciocínio (`PYZ-SEQ-N3-005.md`)](./raciocinio/PYZ-SEQ-N3-005.md) | [Código (`ex005_conta_restaurante.py`)](./exercicios/ex005_conta_restaurante.py)

#### 6. `PYZ-SEQ-N3-006` — Simulador Didático de Salário Líquido
- **Enunciado:** *(Simulação didática)* Crie um programa que leia o nome de um colaborador, o salário bruto mensal (`float`) e a quantidade de vendas realizadas no mês (`int`). Cada venda concede um bônus fixo de `R$ 25.00` (`BONUS_POR_VENDA = 25.00`), e sobre o salário base incide um desconto fixo simulado de 12% (`ALIQUOTA_DESCONTO = 0.12`). Exiba o salário bruto, o total de bônus, o valor do desconto e o salário líquido final.
- **Critérios de Aceite (QA):**
  - Utilizar constantes para `BONUS_POR_VENDA` e `ALIQUOTA_DESCONTO`.
  - Testar o cenário de borda com `0` vendas realizadas no mês.
- **Exemplo de Entrada:** Nome: `Carla` | Salário Base: `3000.00` | Vendas: `10`
- **Saída Esperada:** `Bruto: R$ 3000.00 | Bônus: +R$ 250.00 | Desconto: -R$ 360.00 | Líquido: R$ 2890.00`
- **Arquivos:** [Raciocínio (`PYZ-SEQ-N3-006.md`)](./raciocinio/PYZ-SEQ-N3-006.md) | [Código (`ex006_salario_liquido.py`)](./exercicios/ex006_salario_liquido.py)
