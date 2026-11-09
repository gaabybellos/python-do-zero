# Estudo de Caso 01 (PYZ-CASE-001) - Sistema de Fechamento de Boletim
# Estudo de caso ficticio e autoral criado exclusivamente para aprendizado.

TOTAL_ESTUDANTES = 5
FREQUENCIA_MINIMA = 75.0
NOTA_APROVACAO_DIRETA = 7.0
NOTA_MINIMA_EXAME = 4.0
MEDIA_APROVACAO_EXAME = 5.0


def calcular_nota_semestral(
    nota_pp1: float, nota_pp2: float, nota_teorica: float
) -> float:
    return round(nota_pp1 + nota_pp2 + nota_teorica, 2)


def classificar_pre_exame(nota_semestral: float, frequencia: float) -> str:
    if frequencia < FREQUENCIA_MINIMA:
        return "Reprovado por Falta"
    if nota_semestral >= NOTA_APROVACAO_DIRETA:
        return "Aprovado (Direto)"
    if nota_semestral < NOTA_MINIMA_EXAME:
        return "Reprovado por Nota (Direto)"
    return "Em Exame Substitutivo"


def avaliar_pos_exame(nota_semestral: float, nota_exame: float) -> tuple[float, str]:
    media_final = round((nota_semestral + nota_exame) / 2.0, 2)
    if media_final >= MEDIA_APROVACAO_EXAME:
        return media_final, "Aprovado (Apos Exame)"
    return media_final, "Reprovado por Nota (Apos Exame)"


def ler_valor_valido(
    mensagem: str, limite_minimo: float, limite_maximo: float
) -> float:
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


def main() -> None:
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

        nota_semestral = calcular_nota_semestral(nota_pp1, nota_pp2, nota_teorica)
        status_inicial = classificar_pre_exame(nota_semestral, frequencia)

        if status_inicial == "Reprovado por Falta":
            total_reprovados_falta += 1
            print(
                f"Nota Semestral: {nota_semestral:.2f} | "
                f"Frequencia: {frequencia:.1f}%"
            )
            print(f"Situacao Final: {status_inicial} (frequencia abaixo de 75%)")

        elif status_inicial == "Aprovado (Direto)":
            total_aprovados += 1
            print(
                f"Nota Semestral: {nota_semestral:.2f} | "
                f"Frequencia: {frequencia:.1f}%"
            )
            print(f"Situacao Final: {status_inicial}")

        elif status_inicial == "Reprovado por Nota (Direto)":
            total_reprovados_nota += 1
            print(
                f"Nota Semestral: {nota_semestral:.2f} | "
                f"Frequencia: {frequencia:.1f}%"
            )
            print(f"Situacao Final: {status_inicial} (sem direito a exame)")

        else:
            print(
                f"Nota Semestral: {nota_semestral:.2f} -> "
                "Estudante em Exame Substitutivo!"
            )
            nota_exame = ler_valor_valido(
                "Nota do Exame Substitutivo [0.0 a 10.0]: ", 0.0, 10.0
            )
            media_final, situacao = avaliar_pos_exame(nota_semestral, nota_exame)

            if situacao == "Aprovado (Apos Exame)":
                total_aprovados += 1
            else:
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
