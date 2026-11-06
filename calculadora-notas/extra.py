practicas = []
for _ in range(6):
    pc = float(input("pc: "))
    practicas.append(pc)

print(practicas[0], practicas[1])

suma = 0
for p  in practicas:
    suma += p

print(suma)