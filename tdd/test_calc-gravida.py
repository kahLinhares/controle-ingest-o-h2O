# Test_calculadora_agua.py usando TDD
def test_calculo_agua_para_gravidas():
    # Assumindo que a função `calcular_agua_para_gravidas` ainda não existe
    from calculadora_agua import calcular_agua_para_gravidas

    # Teste básico: 2 litros por dia mais 300 ml para grávidas
    assert calcular_agua_para_gravidas(70) == (70 * 35) + 0.3