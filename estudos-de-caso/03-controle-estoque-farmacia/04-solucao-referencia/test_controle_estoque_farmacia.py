from controle_estoque_farmacia import (
    adicionar_medicamento_estoque,
    baixar_estoque,
    buscar_medicamento,
)


def test_cadastro_e_unicidade_de_codigo_qa():
    estoque = []
    sucesso_1 = adicionar_medicamento_estoque(
        estoque, "med01", "Dipirona 500mg", 10, 5, 8.50
    )
    assert sucesso_1 is True
    assert len(estoque) == 1

    # Tentativa de cadastrar codigo duplicado (mesmo em maiusculo) deve ser bloqueada
    sucesso_duplicado = adicionar_medicamento_estoque(
        estoque, "MED01", "Outro Nome", 20, 5, 10.0
    )
    assert sucesso_duplicado is False
    assert len(estoque) == 1


def test_baixa_estoque_e_protecao_saldo_negativo_bva():
    estoque = []
    adicionar_medicamento_estoque(estoque, "MED01", "Dipirona", 10, 5, 8.50)

    # Tentativa de retirar 11 unidades (acima do saldo 10) -> Bloqueado!
    ok_excesso, _ = baixar_estoque(estoque, "MED01", 11)
    assert ok_excesso is False
    assert buscar_medicamento(estoque, "MED01")["quantidade"] == 10

    # Retirada exatamente no limite (10 unidades -> saldo 0)
    ok_limite, _ = baixar_estoque(estoque, "MED01", 10)
    assert ok_limite is True
    assert buscar_medicamento(estoque, "MED01")["quantidade"] == 0
