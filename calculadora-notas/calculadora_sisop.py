#Fórmula de Calificación:( 2Pb + 2Ta + 3Ex1 + 3Ex2 ) / 10
# Calculo para saber cuanto necesito en el ex2 para aprobar con 10,5 
# el curso

import math

def main():
    p1 = float(input("p1: "))
    p2 = float(input("p2: "))
    p3 = float(input("p3: "))
    p4 = float(input("p4: "))
    p5 = float(input("p5: "))
    p6 = float(input("p6: "))
    prom = promedio(p1, p2, p3, p4, p5, p6)

    ta = float(input("ta: "))
    ex1 = float(input("ex1: "))

    nota = nota_min_final(prom, ta, ex1)
    print(f"Necesito {nota} para aprobar")

def promedio(p1, p2, p3, p4, p5, p6):
    pb = (p1+p2+p3+p4+p5+p6)/6
    return pb

def nota_min_final(prom, ta, ex1):
    nota_aprobatoria = 10.5
    puntaje_requerido = nota_aprobatoria * 10
    puntaje_acumulado = 2 * prom + 2 * ta + 3 * ex1
    ex2 = math.ceil((puntaje_requerido - puntaje_acumulado)/3)
    return ex2

if __name__ == "__main__": 
    main()