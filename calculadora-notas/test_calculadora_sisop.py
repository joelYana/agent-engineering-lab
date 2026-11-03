import pytest
from calculadora_sisop import promedio, nota_min_final, mensaje_resultado

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

def test_mensaje_necesito_0():
    assert mensaje_resultado(0) == "Ya aprobaste, no necesitas rendir el final"

def test_mensaje_necesito_negativo():
    assert mensaje_resultado(-10) == "Ya aprobaste, no necesitas rendir el final"

def test_mensaje_caso1():
    assert mensaje_resultado(2) == "Necesitas 2 en el final para pasar el curso"

def test_mensaje_no_aprueba():
    assert mensaje_resultado(21) == "Ya no puedes aprobar aunque saques 20"

def test_mensaje_necesita_20():
    assert mensaje_resultado(20) == "Necesitas la nota maxima en el examen para pasar"

def test_mensaje_necesito_19():
    assert mensaje_resultado(19) == "Necesitas 19 en el final para pasar el curso"

def test_mensaje_necesito_1():
    assert mensaje_resultado(1) == "Necesitas 1 en el final para pasar el curso"