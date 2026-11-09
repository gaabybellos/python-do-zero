"""
Exemplo 01 — Variáveis, Constantes e Tipos Básicos (`str`, `int`, `float`, `bool`)
Problema Análogo: Exibir a ficha cadastral de um livro e o valor de um lote.

Saída esperada no terminal:
Livro: Dom Casmurro | Páginas: 256 | Disponível: True
Preço unitário: R$ 39.90 | Lote (3 un.): R$ 119.70
"""

QUANTIDADE_PADRAO_LOTE = 3


def main() -> None:
    # 1. Criação de variáveis com os 4 tipos primitivos em snake_case
    titulo_livro = "Dom Casmurro"
    numero_paginas = 256
    preco_unitario = 39.90
    esta_disponivel = True

    # 2. Processamento aritmético simples
    valor_total_lote = preco_unitario * QUANTIDADE_PADRAO_LOTE

    # 3. Saída formatada com f-strings
    print(
        f"Livro: {titulo_livro} | Páginas: {numero_paginas} | "
        f"Disponível: {esta_disponivel}"
    )
    print(
        f"Preço unitário: R$ {preco_unitario:.2f} | "
        f"Lote ({QUANTIDADE_PADRAO_LOTE} un.): R$ {valor_total_lote:.2f}"
    )


if __name__ == "__main__":
    main()
