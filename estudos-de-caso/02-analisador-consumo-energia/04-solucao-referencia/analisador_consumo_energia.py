# Estudo de Caso 02 (PYZ-CASE-002) - Analisador de Consumo e Tarifa de Energia
# Estudo de caso ficticio e autoral criado exclusivamente para aprendizado.

LIMITE_FAIXA_SOCIAL = 100.0
LIMITE_FAIXA_MODERADA = 300.0

TARIFA_SOCIAL = 0.50
TARIFA_MODERADA = 0.75
TARIFA_ELEVADA = 0.95

TAXA_BANDEIRA_AMARELA = 15.00
TAXA_BANDEIRA_VERMELHA = 35.00
DESCONTO_SOCIAL_RESIDENCIAL = 0.10


def ler_inteiro_positivo(mensagem: str, minimo: int, maximo: int) -> int:
    while True:
        entrada = input(mensagem).strip()
        try:
            valor = int(entrada)
            if minimo <= valor <= maximo:
                return valor
            print(
                f"Valor invalido! Digite um numero inteiro entre "
                f"{minimo} e {maximo}."
            )
        except ValueError:
            print("Entrada invalida! Digite apenas um numero inteiro.")


def ler_consumo_kwh(mensagem: str) -> float:
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            consumo = float(entrada)
            if consumo >= 0.0:
                return consumo
            print("Valor invalido! O consumo nao pode ser negativo.")
        except ValueError:
            print("Entrada invalida! Digite um numero valido (ex: 150.5 ou 150,5).")


def ler_tipo_instalacao(mensagem: str) -> str:
    while True:
        tipo = input(mensagem).strip().upper()
        if tipo in ("R", "C"):
            return tipo
        print("Opcao invalida! Digite 'R' para Residencial ou 'C' para Comercial.")


def calcular_fatura(consumo_kwh: float, tipo_instalacao: str) -> tuple[str, float]:
    if consumo_kwh < 0.0:
        raise ValueError("O consumo nao pode ser negativo.")
    tipo_limpo = tipo_instalacao.strip().upper()
    if tipo_limpo not in ("R", "C"):
        raise ValueError("Tipo de instalacao invalido. Use 'R' ou 'C'.")

    if consumo_kwh <= LIMITE_FAIXA_SOCIAL:
        faixa = "Social (Isento de Bandeira)"
        valor_fatura = consumo_kwh * TARIFA_SOCIAL
        if tipo_limpo == "R":
            valor_fatura *= 1.0 - DESCONTO_SOCIAL_RESIDENCIAL
    elif consumo_kwh <= LIMITE_FAIXA_MODERADA:
        faixa = "Moderada (Bandeira Amarela)"
        valor_fatura = (consumo_kwh * TARIFA_MODERADA) + TAXA_BANDEIRA_AMARELA
    else:
        faixa = "Elevada (Bandeira Vermelha)"
        valor_fatura = (consumo_kwh * TARIFA_ELEVADA) + TAXA_BANDEIRA_VERMELHA

    return faixa, round(valor_fatura, 2)


def main() -> None:
    print("=== ANALISADOR DE CONSUMO E TARIFA DE ENERGIA ===")
    quantidade_imoveis = ler_inteiro_positivo(
        "Quantidade de imoveis a analisar [1 a 50]: ", 1, 50
    )

    soma_consumo = 0.0
    faturamento_total = 0.0
    maior_consumo = None
    menor_consumo = None

    for numero_imovel in range(1, quantidade_imoveis + 1):
        print(f"\n--- Imovel {numero_imovel} de {quantidade_imoveis} ---")
        consumo_kwh = ler_consumo_kwh("Consumo mensal em kWh [>= 0]: ")
        tipo_instalacao = ler_tipo_instalacao(
            "Tipo de instalacao [R - Residencial | C - Comercial]: "
        )

        faixa_tarifaria, valor_fatura = calcular_fatura(consumo_kwh, tipo_instalacao)

        soma_consumo += consumo_kwh
        faturamento_total += valor_fatura

        if maior_consumo is None or consumo_kwh > maior_consumo:
            maior_consumo = consumo_kwh
        if menor_consumo is None or consumo_kwh < menor_consumo:
            menor_consumo = consumo_kwh

        print(f"Faixa Aplicada : {faixa_tarifaria}")
        print(f"Valor da Fatura: R$ {valor_fatura:.2f}")

    media_consumo = soma_consumo / quantidade_imoveis

    print("\n==================================================")
    print("          RELATORIO CONSOLIDADO DA REGIAO         ")
    print("==================================================")
    print(f"Total de Imoveis Analisados : {quantidade_imoveis}")
    print(f"Media de Consumo            : {media_consumo:.2f} kWh")
    print(f"Maior Consumo Registrado    : {maior_consumo:.2f} kWh")
    print(f"Menor Consumo Registrado    : {menor_consumo:.2f} kWh")
    print(f"Faturamento Total           : R$ {faturamento_total:.2f}")


if __name__ == "__main__":
    main()
