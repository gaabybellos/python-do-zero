from sistema_boletim_academico import (
    avaliar_pos_exame,
    calcular_nota_semestral,
    classificar_pre_exame,
)


def test_calcular_nota_semestral():
    assert calcular_nota_semestral(2.0, 3.0, 5.0) == 10.0
    assert calcular_nota_semestral(1.5, 2.0, 3.5) == 7.0


def test_classificar_pre_exame_fronteiras_bva():
    # Reprovado por falta mesmo com nota 10.0 (Borda 74.9% < 75.0%)
    assert classificar_pre_exame(10.0, 74.9) == "Reprovado por Falta"
    # Aprovado direto na fronteira exata (7.0 e 75.0%)
    assert classificar_pre_exame(7.0, 75.0) == "Aprovado (Direto)"
    # Em exame substitutivo nas fronteiras 6.9 e 4.0
    assert classificar_pre_exame(6.9, 75.0) == "Em Exame Substitutivo"
    assert classificar_pre_exame(4.0, 80.0) == "Em Exame Substitutivo"
    # Reprovado direto por nota na fronteira 3.9
    assert classificar_pre_exame(3.9, 90.0) == "Reprovado por Nota (Direto)"


def test_avaliar_pos_exame_fronteiras_bva():
    media_aprov, status_aprov = avaliar_pos_exame(4.0, 6.0)
    assert media_aprov == 5.0
    assert status_aprov == "Aprovado (Apos Exame)"

    media_reprov, status_reprov = avaliar_pos_exame(4.0, 5.8)
    assert media_reprov == 4.9
    assert status_reprov == "Reprovado por Nota (Apos Exame)"
