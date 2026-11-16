# 1. Entradas que deben generar ValueError:
#    - 1+1
#    - 1 + 1 + 1
#    - 5 ^ 2
#    - a + 1

# 2. División entre cero (ZeroDivisionError):
#    - 1 / 0

# 3. Casos válidos:
#    - Caso 1: 2 + 3 -> 5.0
#    - Caso 2: -10 - 5 -> -15.0
#    - Caso 3: 4 * 6 -> 24.0
#    - Caso 4: 1 / 3 -> 0.333...

import pytest
from interpreter import calcular_operacion

def test_1_mas_1_pegado():
    with pytest.raises(ValueError):
        calcular_operacion("1+1")

def test_1_mas_1_mas_1():
    with pytest.raises(ValueError):
        calcular_operacion("1 + 1 + 1")

def test_5_potencia_2():
    with pytest.raises(ValueError):
        calcular_operacion("5 ^ 2")

def test_a_mas_1():
    with pytest.raises(ValueError):
        calcular_operacion("a + 1")

def test_1_entre_0():
    with pytest.raises(ZeroDivisionError):
        calcular_operacion("1 / 0")

def test_2_mas_3():
    assert calcular_operacion("2 + 3") == 5.0

def test_menos_10_menos_5():
    assert calcular_operacion("-10 - 5") == -15.0

def test_4_por_6():
    assert calcular_operacion("4 * 6") == 24.0

def test_1_entre_3():
    assert calcular_operacion("1 / 3") == pytest.approx(1/3)