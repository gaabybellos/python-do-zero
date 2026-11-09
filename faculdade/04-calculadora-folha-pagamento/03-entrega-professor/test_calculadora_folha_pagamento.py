import pytest
from calculadora_folha_pagamento import (
    calcular_auxilio_dependentes,
    calcular_desconto_previdenciario,
    calcular_valor_horas_extras,
    gerar_contracheque,
)


def test_calcular_valor_horas_extras_caminho_feliz():
    # Salario 2200 -> hora normal = R$ 10.00 -> hora extra (+50%) = R$ 15.00
    assert calcular_valor_horas_extras(2200.0, 10.0) == 150.00


def test_calcular_desconto_previdenciario_bordas_bva():
    # Borda Faixa 1 (ate 2000.00 -> 8%)
    assert calcular_desconto_previdenciario(2000.00) == 160.00
    # Borda Faixa 2 (acima de 2000.00 ate 4500.00 -> 11%)
    assert calcular_desconto_previdenciario(3000.00) == 330.00
    assert calcular_desconto_previdenciario(4500.00) == 495.00
    # Borda Faixa 3 (acima de 4500.00 -> 14%)
    assert calcular_desconto_previdenciario(5000.00) == 700.00


def test_calcular_auxilio_dependentes_borda_teto():
    assert calcular_auxilio_dependentes(3500.00, 2) == 300.00
    assert calcular_auxilio_dependentes(3500.01, 2) == 0.00


def test_gerar_contracheque_completo():
    resultado = gerar_contracheque(
        salario_base=2200.00, horas_extras=10.0, dependentes=2
    )
    assert resultado["valor_horas_extras"] == 150.00
    assert resultado["remuneracao_bruta"] == 2350.00
    assert resultado["desconto"] == 258.50
    assert resultado["auxilio_dependentes"] == 300.00
    assert resultado["salario_liquido"] == 2391.50


def test_validacoes_negativas_qa():
    with pytest.raises(ValueError):
        calcular_valor_horas_extras(0.0, 5.0)
    with pytest.raises(ValueError):
        calcular_valor_horas_extras(2200.0, -1.0)
    with pytest.raises(ValueError):
        calcular_auxilio_dependentes(2200.0, -2)
