"""
Exemplo 02 — Entrada de Dados (`input`), Conversão e Cálculo de Área
Problema Análogo: Ler a largura e o comprimento de uma sala e calcular sua área (m²).

Exemplo de Entrada: Largura = 4 | Comprimento = 5.5
Saída Esperada: Uma sala de 4.00m x 5.50m possui área de 22.00 m².
"""


def main() -> None:
    # 1. Entrada de dados com higienização de vírgula para ponto (Dica de QA)
    entrada_largura = input("Digite a largura da sala (m): ").strip().replace(",", ".")
    entrada_comp = input("Digite o comprimento da sala (m): ").strip().replace(",", ".")

    largura_metros = float(entrada_largura)
    comprimento_metros = float(entrada_comp)

    # 2. Processamento (fórmula da área do retângulo)
    area_total = largura_metros * comprimento_metros

    # 3. Saída formatada com 2 casas decimais
    print(
        f"Uma sala de {largura_metros:.2f}m x {comprimento_metros:.2f}m "
        f"possui área de {area_total:.2f} m²."
    )


if __name__ == "__main__":
    main()
