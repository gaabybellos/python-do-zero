# Sistema de Fechamento de Boletim Academico

TOTAL_ESTUDANTES = 5
FREQUENCIA_MINIMA = 75.0
NOTA_APROVACAO_DIRETA = 7.0
NOTA_MINIMA_EXAME = 4.0
MEDIA_APROVACAO_EXAME = 5.0


def ler_valor_valido(mensagem, limite_minimo, limite_maximo):
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


def main():
    total_aprovados = 0
    total_reprovados_nota = 0
    total_reprovados_falta = 0

    print("=== SISTEMA DE FECHAMENTO DE BOLETIM ACADEMICO ===")

    for numero_estudante in range(1, TOTAL_ESTUDANTES + 1):
        print(f"\n--- Estudante {numero_estudante} de {TOTAL_ESTUDANTES} ---")

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

        nota_semestral = nota_pp1 + nota_pp2 + nota_teorica

        if frequencia < FREQUENCIA_MINIMA:
            situacao = "Reprovado por Falta"
            total_reprovados_falta += 1
            print(f"Nota Semestral: {nota_semestral:.2f} | Frequencia: {frequencia:.1f}%")
            print(f"Situacao Final: {situacao} (frequencia abaixo de 75%)")

        elif nota_semestral >= NOTA_APROVACAO_DIRETA:
            situacao = "Aprovado (Direto)"
            total_aprovados += 1
            print(f"Nota Semestral: {nota_semestral:.2f} | Frequencia: {frequencia:.1f}%")
            print(f"Situacao Final: {situacao}")

        elif nota_semestral < NOTA_MINIMA_EXAME:
            situacao = "Reprovado por Nota (Direto)"
            total_reprovados_nota += 1
            print(f"Nota Semestral: {nota_semestral:.2f} | Frequencia: {frequencia:.1f}%")
            print(f"Situacao Final: {situacao} (sem direito a exame)")

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
