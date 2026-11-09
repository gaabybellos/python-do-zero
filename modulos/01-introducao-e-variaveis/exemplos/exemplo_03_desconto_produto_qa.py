"""
Exemplo 03 — Cálculo de Porcentagem e Constantes (Clean Code & QA)
Problema Análogo: Calcular 15% de desconto à vista no preço de um fone de ouvido.

Exemplo de Entrada: Preço = 200,00
Saída Esperada: Preço: R$ 200.00 | Desconto (15%): R$ 30.00 | Final: R$ 170.00
"""

PERCENTUAL_DESCONTO_VISTA = 0.15


def main() -> None:
    # 1. Entrada higienizada (remove espaços e aceita vírgula ou ponto)
    entrada_preco = input("Digite o preço do produto (R$): ").strip().replace(",", ".")
    preco_original = float(entrada_preco)

    # 2. Processamento usando constante nomeada (sem números mágicos)
    valor_desconto = preco_original * PERCENTUAL_DESCONTO_VISTA
    preco_final = preco_original - valor_desconto

    # 3. Saída clara e formatada
    print(
        f"Preço: R$ {preco_original:.2f} | "
        f"Desconto (15%): R$ {valor_desconto:.2f} | "
        f"Final: R$ {preco_final:.2f}"
    )


if __name__ == "__main__":
    main()
