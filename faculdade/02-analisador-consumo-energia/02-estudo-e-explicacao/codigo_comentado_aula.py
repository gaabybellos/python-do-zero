"""
ARQUIVO DE ESTUDO E AULA (NÃO ENVIAR AO PROFESSOR)
Tarefa: PYZ-FAC-002 — Analisador de Consumo e Tarifa de Energia Elétrica
Objetivo: Demonstrar o uso de acumuladores, descoberta de maior/menor valor e faixas tarifárias.
"""

LIMITE_FAIXA_SOCIAL = 100.0
LIMITE_FAIXA_MODERADA = 300.0

TARIFA_SOCIAL = 0.50
TARIFA_MODERADA = 0.75
TARIFA_ELEVADA = 0.95

TAXA_BANDEIRA_AMARELA = 15.00
TAXA_BANDEIRA_VERMELHA = 35.00
DESCONTO_SOCIAL_RESIDENCIAL = 0.10


def ler_inteiro_positivo(mensagem, minimo, maximo):
    """Lê um número inteiro dentro do intervalo [minimo, maximo]."""
    while True:
        entrada = input(mensagem).strip()
        try:
            valor = int(entrada)
            if minimo <= valor <= maximo:
                return valor
            print(f"Valor invalido! Digite um numero inteiro entre {minimo} e {maximo}.")
        except ValueError:
            print("Entrada invalida! Digite apenas um numero inteiro.")


def ler_consumo_kwh(mensagem):
    """Lê um consumo em kWh (>= 0.0), aceitando ponto ou vírgula."""
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            consumo = float(entrada)
            if consumo >= 0.0:
                return consumo
            print("Valor invalido! O consumo nao pode ser negativo.")
        except ValueError:
            print("Entrada invalida! Digite um numero valido (ex: 150.5 ou 150,5).")


def ler_tipo_instalacao(mensagem):
    """Lê e padroniza a sigla do imóvel ('R' ou 'C') usando .upper()."""
    while True:
        # `.upper()` transforma 'r' minúsculo em 'R' maiúsculo automaticamente!
        tipo = input(mensagem).strip().upper()
        if tipo in ("R", "C"):
            return tipo
        print("Opcao invalida! Digite 'R' para Residencial ou 'C' para Comercial.")


def calcular_fatura(consumo_kwh, tipo_instalacao):
    """Aplica a regra de negócio de faixas de kWh e retorna (faixa, valor_fatura)."""
    if consumo_kwh <= LIMITE_FAIXA_SOCIAL:
        faixa = "Social (Isento de Bandeira)"
        valor_fatura = consumo_kwh * TARIFA_SOCIAL
        # Desconto de 10% apenas se for Residencial ('R') dentro da faixa social:
        if tipo_instalacao == "R":
            valor_fatura *= 1.0 - DESCONTO_SOCIAL_RESIDENCIAL
    elif consumo_kwh <= LIMITE_FAIXA_MODERADA:
        faixa = "Moderada (Bandeira Amarela)"
        valor_fatura = (consumo_kwh * TARIFA_MODERADA) + TAXA_BANDEIRA_AMARELA
    else:
        faixa = "Elevada (Bandeira Vermelha)"
        valor_fatura = (consumo_kwh * TARIFA_ELEVADA) + TAXA_BANDEIRA_VERMELHA

    return faixa, valor_fatura


def main():
    print("=== ANALISADOR DE CONSUMO E TARIFA DE ENERGIA ===")
    quantidade_imoveis = ler_inteiro_positivo(
        "Quantidade de imoveis a analisar [1 a 50]: ", 1, 50
    )

    # Acumuladores começam em 0.0:
    soma_consumo = 0.0
    faturamento_total = 0.0

    # Variáveis para guardar extremos (maior e menor) começam como `None` (vazio),
    # e assumem o valor do 1º imóvel lido na primeira repetição!
    maior_consumo = None
    menor_consumo = None

    for numero_imovel in range(1, quantidade_imoveis + 1):
        print(f"\n--- Imovel {numero_imovel} de {quantidade_imoveis} ---")
        consumo_kwh = ler_consumo_kwh("Consumo mensal em kWh [>= 0]: ")
        tipo_instalacao = ler_tipo_instalacao(
            "Tipo de instalacao [R - Residencial | C - Comercial]: "
        )

        faixa_tarifaria, valor_fatura = calcular_fatura(consumo_kwh, tipo_instalacao)

        # Acumulando os totais:
        soma_consumo += consumo_kwh
        faturamento_total += valor_fatura

        # Atualizando o maior e o menor consumo:
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
