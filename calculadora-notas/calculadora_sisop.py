#Fórmula de Calificación:( 2Pb + 2Ta + 3Ex1 + 3Ex2 ) / 10
# Calculo para saber cuanto necesito en el ex2 para aprobar con 10,5 
# el curso

# Caso 1: prácticas 15, 20, 20, 18, 20 y 13; tarea académica 20; parcial 8. El promedio de prácticas da 17.666... y la nota mínima del final, 2.
# Caso 2: todas las notas en 20. El promedio da 20 y la nota mínima del final, -11.
# Caso 3 : pcs: 15, 20, 19, 15, 15, 15 ta = 18, parcial = 9, prom esperado = 16.5 , nota_min_final = 3
# Caso 4 : pcs: 15, 20, 19, 14, 15, 11 ta = 20, parcial = 11, prom esperado = 15.67 , nota_min_final = 1

# main pedirá las seis prácticas mediante un for, ya que
# conocemos la cantidad. Las notas se guardarán en una lista.
# La función promedio recibirá esa lista para realizar el cálculo.

# Lo que no cambia: los resultados de los tres casos anteriores.
# Se añadirá un cuarto caso.
# La función promedio dividirá la suma de las notas entre
# len(lista), que en este caso será 6.

import math

def main():
    practicas = []
    for _ in range(6):
        pc = float(input("pc: "))
        practicas.append(pc)

    prom = promedio(practicas)

    ta = float(input("ta: "))
    ex1 = float(input("ex1: "))

    nota = nota_min_final(prom, ta, ex1)
    print(mensaje_resultado(nota))

def promedio(practicas):
    suma = 0
    for pc in practicas:
        suma += pc
    pb = suma/len(practicas)
    return pb

def nota_min_final(prom, ta, ex1):
    nota_aprobatoria = 10.5
    puntaje_requerido = nota_aprobatoria * 10
    puntaje_acumulado = 2 * prom + 2 * ta + 3 * ex1
    ex2 = math.ceil((puntaje_requerido - puntaje_acumulado)/3)
    return ex2

def mensaje_resultado(nota_necesaria):
    if nota_necesaria <= 0:
        return "Ya aprobaste, no necesitas rendir el final"
    elif nota_necesaria <= 19:
        return f"Necesitas {nota_necesaria} en el final para pasar el curso"
    elif nota_necesaria == 20:
        return "Necesitas la nota maxima en el examen para pasar"
    else:
        return "Ya no puedes aprobar aunque saques 20"

if __name__ == "__main__": 
    main()