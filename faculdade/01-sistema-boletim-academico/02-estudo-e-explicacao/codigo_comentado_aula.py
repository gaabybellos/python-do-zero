"""
ARQUIVO DE ESTUDO E AULA (NÃO ENVIAR AO PROFESSOR)
Tarefa: PYZ-FAC-001 — Sistema de Fechamento de Boletim Acadêmico
Objetivo: Explicar linha por linha o funcionamento, as regras de negócio e as validações de QA.
"""

# ==============================================================================
# 1. CONSTANTES DE REGRAS DE NEGÓCIO (CLEAN CODE: SEM NÚMEROS MÁGICOS)
# ==============================================================================
TOTAL_ESTUDANTES = 5
FREQUENCIA_MINIMA = 75.0
NOTA_APROVACAO_DIRETA = 7.0
NOTA_MINIMA_EXAME = 4.0
MEDIA_APROVACAO_EXAME = 5.0


# ==============================================================================
# 2. FUNÇÃO DE VALIDAÇÃO DEFENSIVA (QA)
# ==============================================================================
def ler_valor_valido(mensagem, limite_minimo, limite_maximo):
    """
    Garante que o valor digitado pelo usuário:
    1. Aceite tanto vírgula ('1,5') quanto ponto ('1.5');
    2. Não quebre o programa se digitar letras ou Enter vazio (try/except ValueError);
    3. Esteja estritamente dentro do intervalo [limite_minimo, limite_maximo].
    """
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            valor = float(entrada)
            if limite_minimo <= valor <= limite_maximo:
                return valor
            print(
                f"Valor fora do intervalo! Digite um valor entre "
                f"{limite_minimo:.1f} e {limite_maximo:.1f}."
            )
        except ValueError:
            print("Entrada invalida! Digite apenas numeros (ex: 1.5 ou 1,5).")


# ==============================================================================
# 3. FLUXO PRINCIPAL (LAÇO DOS ESTUDANTES E ÁRVORE DE DECISÃO)
# ==============================================================================
def main():
    # Contadores inicializados em ZERO antes do laço começar:
    total_aprovados = 0
    total_reprovados_nota = 0
    total_reprovados_falta = 0

    print("=== SISTEMA DE FECHAMENTO DE BOLETIM ACADEMICO ===")

    # Repetição contada para os 5 estudantes (de 1 até 5):
    for numero_estudante in range(1, TOTAL_ESTUDANTES + 1):
        print(f"\n--- Estudante {numero_estudante} de {TOTAL_ESTUDANTES} ---")

        # Leitura validada das 3 avaliações e da frequência:
        nota_pp1 = ler_valor_valido(
            "Nota do Projeto Pratico 1 [0.0 a 2.0]: ", 0.0, 2.0
        )
        nota_pp2 = ler_valor_valido(
            "Nota do Projeto Pratico 2 [0.0 a 3.0]: ", 0.0, 3.0
        )
        nota_teorica = ler_valor_valido(
            "Nota da Avaliacao Teorica [0.0 a 5.0]: ", 0.0, 5.0
        )
        frequencia = ler_valor_valido(
            "Percentual de Frequencia [0.0 a 100.0]: ", 0.0, 100.0
        )

        # Soma semestral (máximo possível: 2.0 + 3.0 + 5.0 = 10.0)
        nota_semestral = nota_pp1 + nota_pp2 + nota_teorica

        # Regra 1: Frequência insuficiente reprova direto (mesmo com nota alta!)
        if frequencia < FREQUENCIA_MINIMA:
            situacao = "Reprovado por Falta"
            total_reprovados_falta += 1
            print(f"Nota Semestral: {nota_semestral:.2f} | Frequencia: {frequencia:.1f}%")
            print(f"Situacao Final: {situacao} (frequencia abaixo de 75%)")

        # Regra 2: Tem presença suficiente (>= 75%) e atingiu nota >= 7.0
        elif nota_semestral >= NOTA_APROVACAO_DIRETA:
            situacao = "Aprovado (Direto)"
            total_aprovados += 1
            print(f"Nota Semestral: {nota_semestral:.2f} | Frequencia: {frequencia:.1f}%")
            print(f"Situacao Final: {situacao}")

        # Regra 3: Tem presença (>= 75%), mas a nota ficou abaixo de 4.0
        elif nota_semestral < NOTA_MINIMA_EXAME:
            situacao = "Reprovado por Nota (Direto)"
            total_reprovados_nota += 1
            print(f"Nota Semestral: {nota_semestral:.2f} | Frequencia: {frequencia:.1f}%")
            print(f"Situacao Final: {situacao} (sem direito a exame)")

        # Regra 4: Tem presença (>= 75%) e nota entre 4.0 e 6.99 -> Exame Substitutivo
        else:
            print(
                f"Nota Semestral: {nota_semestral:.2f} -> "
                "Estudante em Exame Substitutivo!"
            )
            nota_exame = ler_valor_valido(
                "Nota do Exame Substitutivo [0.0 a 10.0]: ", 0.0, 10.0
            )
            media_final = (nota_semestral + nota_exame) / 2.0

            if media_final >= MEDIA_APROVACAO_EXAME:
                situacao = "Aprovado (Apos Exame)"
                total_aprovados += 1
            else:
                situacao = "Reprovado por Nota (Apos Exame)"
                total_reprovados_nota += 1

            print(
                f"Nota Semestral: {nota_semestral:.2f} | "
                f"Media Final: {media_final:.2f} | Frequencia: {frequencia:.1f}%"
            )
            print(f"Situacao Final: {situacao}")

    # Cálculo das porcentagens ao final da turma (fora do laço `for`)
    perc_aprovados = (total_aprovados / TOTAL_ESTUDANTES) * 100.0
    perc_reprovados_nota = (total_reprovados_nota / TOTAL_ESTUDANTES) * 100.0
    perc_reprovados_falta = (total_reprovados_falta / TOTAL_ESTUDANTES) * 100.0

    print("\n==================================================")
    print("           RESUMO ESTATISTICO DA TURMA            ")
    print("==================================================")
    print(f"Total de Estudantes Avaliados : {TOTAL_ESTUDANTES}")
    print(f"Aprovados                     : {total_aprovados} ({perc_aprovados:.1f}%)")
    print(
        f"Reprovados por Nota           : "
        f"{total_reprovados_nota} ({perc_reprovados_nota:.1f}%)"
    )
    print(
        f"Reprovados por Falta          : "
        f"{total_reprovados_falta} ({perc_reprovados_falta:.1f}%)"
    )


if __name__ == "__main__":
    main()
