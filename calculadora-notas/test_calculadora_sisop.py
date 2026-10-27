import pytest
from calculadora_sisop import promedio, nota_min_final

# Caso 1: prácticas 15, 20, 20, 18, 20 y 13; tarea académica 20; parcial 8. El promedio de prácticas da 17.666... y la nota mínima del final, 2.
# Caso 2: todas las notas en 20. El promedio da 20 y la nota mínima del final, -11.
# Caso 3 (real): pcs: 15, 20, 19, 15, 15, 15 ta = 18, parcial = 9, prom esperado = 16.5 , nota_min_final = 3

def test_nota_min_caso1():
    assert nota_min_final(promedio(15, 20, 20, 18, 20, 13), 20, 8) == 2

def test_promedio_caso1():
    assert promedio(15, 20, 20, 18, 20, 13) == pytest.approx(106/6)

def test_nota_min_caso2():
    assert nota_min_final(20, 20, 20) == -11

def test_promedio_caso2():
    assert promedio(20, 20, 20, 20, 20, 20) == 20

def test_nota_min_caso3():
    assert nota_min_final(16.5, 18, 9) == 3

def test_promedio_caso3():
    assert promedio(15, 20, 19, 15, 15, 15) == pytest.approx(99/6)