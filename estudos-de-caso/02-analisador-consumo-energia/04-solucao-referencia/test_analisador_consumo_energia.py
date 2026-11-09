import pytest
from analisador_consumo_energia import calcular_fatura


def test_calcular_fatura_faixa_social_bva():
    # Ate 100.0 kWh: Residencial tem 10% de desconto; Comercial nao tem
    faixa_res, valor_res = calcular_fatura(100.0, "r")
    assert faixa_res == "Social (Isento de Bandeira)"
    assert valor_res == 45.00

    faixa_com, valor_com = calcular_fatura(100.0, "C")
    assert faixa_com == "Social (Isento de Bandeira)"
    assert valor_com == 50.00


def test_calcular_fatura_faixa_moderada_e_elevada_bva():
    faixa_mod, valor_mod = calcular_fatura(200.0, "R")
    assert faixa_mod == "Moderada (Bandeira Amarela)"
    assert valor_mod == 165.00

    faixa_elev, valor_elev = calcular_fatura(400.0, "C")
    assert faixa_elev == "Elevada (Bandeira Vermelha)"
    assert valor_elev == 415.00


def test_calcular_fatura_entradas_invalidas_qa():
    with pytest.raises(ValueError):
        calcular_fatura(-5.0, "R")
    with pytest.raises(ValueError):
        calcular_fatura(100.0, "X")
