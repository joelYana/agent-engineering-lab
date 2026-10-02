#Fórmula de Calificación:( 2Pb + 2Ta + 3Ex1 + 3Ex2 ) / 10
# Calculo para saber cuanto necesito en el ex2 para aprobar con 10,5 
# el curso

import math

p1 = float(input("p1: "))
p2 = float(input("p2: "))
p3 = float(input("p3: "))
p4 = float(input("p4: "))
p5 = float(input("p5: "))
p6 = float(input("p6: "))

ta = float(input("ta: "))
ex1 = float(input("ex1: "))

pb = (p1+p2+p3+p4+p5+p6)/6

nota_aprobatoria = 10.5
puntaje_requerido = nota_aprobatoria * 10
ex2 = math.ceil((puntaje_requerido - (2 * pb + 2 * ta + 3 * ex1))/3)

print(f"Necesito {ex2} para aprobar")