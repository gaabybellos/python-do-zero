"""
ARQUIVO DE ESTUDO E EXPLICAÇÃO (VERSÃO COMENTADA)
Estudo de Caso: PYZ-CASE-004 — Calculadora Modular de Folha de Pagamento
Aviso: Estudo de caso fictício e autoral criado exclusivamente para aprendizado.
"""

CARGA_HORARIA_MENSAL = 220.0
ADICIONAL_HORA_EXTRA = 1.50
VALOR_POR_DEPENDENTE = 150.00
TETO_AUXILIO_DEPENDENTE = 3500.00

LIMITE_FAIXA_1 = 2000.00
LIMITE_FAIXA_2 = 4500.00

ALIQUOTA_FAIXA_1 = 0.08
ALIQUOTA_FAIXA_2 = 0.11
ALIQUOTA_FAIXA_3 = 0.14


# 1. FUNÇÕES PURAS DE NEGÓCIO (SEM INPUT E SEM PRINT -> 100% TESTÁVEIS!)
def calcular_valor_horas_extras(salario_base: float, horas_extras: float) -> float:
    """Calcula o valor total das horas extras com adicional de 50%."""
    if salario_base <= 0.0:
        raise ValueError("O salario base deve ser maior que zero.")
    if horas_extras < 0.0:
        raise ValueError("As horas extras nao podem ser negativas.")

    valor_hora_normal = salario_base / CARGA_HORARIA_MENSAL
    return round(horas_extras * valor_hora_normal * ADICIONAL_HORA_EXTRA, 2)


def calcular_desconto_previdenciario(remuneracao_bruta: float) -> float:
    """Aplica a alíquota de 8%, 11% ou 14% conforme a faixa de remuneração bruta."""
    if remuneracao_bruta < 0.0:
        raise ValueError("A remuneracao bruta nao pode ser negativa.")

    if remuneracao_bruta <= LIMITE_FAIXA_1:
        aliquota = ALIQUOTA_FAIXA_1
    elif remuneracao_bruta <= LIMITE_FAIXA_2:
        aliquota = ALIQUOTA_FAIXA_2
    else:
        aliquota = ALIQUOTA_FAIXA_3

    return round(remuneracao_bruta * aliquota, 2)


def calcular_auxilio_dependentes(salario_base: float, dependentes: int) -> float:
    """Concede R$ 150,00 por dependente caso o salário base seja de até R$ 3.500,00."""
    if dependentes < 0:
        raise ValueError("O numero de dependentes nao pode ser negativo.")
    if salario_base <= TETO_AUXILIO_DEPENDENTE:
        return round(dependentes * VALOR_POR_DEPENDENTE, 2)
    return 0.0


def gerar_contracheque(
    salario_base: float, horas_extras: float, dependentes: int
) -> dict:
    """Orquestra os cálculos e retorna um dicionário com os campos do contracheque."""
    valor_extras = calcular_valor_horas_extras(salario_base, horas_extras)
    remuneracao_bruta = round(salario_base + valor_extras, 2)
    desconto = calcular_desconto_previdenciario(remuneracao_bruta)
    auxilio = calcular_auxilio_dependentes(salario_base, dependentes)
    salario_liquido = round(remuneracao_bruta - desconto + auxilio, 2)

    return {
        "salario_base": round(salario_base, 2),
        "valor_horas_extras": valor_extras,
        "remuneracao_bruta": remuneracao_bruta,
        "desconto": desconto,
        "auxilio_dependentes": auxilio,
        "salario_liquido": salario_liquido,
    }


# 2. CAMADA DE ENTRADA E SAÍDA NO TERMINAL (I/O)
def ler_float_valido(
    mensagem: str, minimo: float, aceita_zero: bool = True
) -> float:
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            valor = float(entrada)
            cond_zero = aceita_zero and valor >= minimo
            cond_pos = not aceita_zero and valor > minimo
            if cond_zero or cond_pos:
                return valor
            print(f"Valor invalido! Respeite o limite minimo ({minimo:.2f}).")
        except ValueError:
            print("Entrada invalida! Digite um numero valido (ex: 2500.00 ou 2500,00).")


def ler_inteiro_nao_negativo(mensagem: str) -> int:
    while True:
        entrada = input(mensagem).strip()
        try:
            valor = int(entrada)
            if valor >= 0:
                return valor
            print("Valor invalido! Digite um numero inteiro >= 0.")
        except ValueError:
            print("Entrada invalida! Digite apenas um numero inteiro.")


def main() -> None:
    print("=== CALCULADORA DE FOLHA DE PAGAMENTO ===")
    salario_base = ler_float_valido(
        "Salario base mensal (R$) [> 0]: ", 0.0, aceita_zero=False
    )
    horas_extras = ler_float_valido(
        "Quantidade de horas extras [>= 0]: ", 0.0, aceita_zero=True
    )
    dependentes = ler_inteiro_nao_negativo("Numero de dependentes [>= 0]: ")

    dados = gerar_contracheque(salario_base, horas_extras, dependentes)

    print("\n==========================================")
    print("           RESUMO DO CONTRACHEQUE         ")
    print("==========================================")
    print(f"Salario Base          : R$ {dados['salario_base']:.2f}")
    print(f"Horas Extras (+50%)   : R$ {dados['valor_horas_extras']:.2f}")
    print(f"Remuneracao Bruta     : R$ {dados['remuneracao_bruta']:.2f}")
    print(f"Desconto Retido       : - R$ {dados['desconto']:.2f}")
    print(f"Auxilio Dependentes   : + R$ {dados['auxilio_dependentes']:.2f}")
    print("------------------------------------------")
    print(f"SALARIO LIQUIDO FINAL : R$ {dados['salario_liquido']:.2f}")


if __name__ == "__main__":
    main()
