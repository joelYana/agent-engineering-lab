# caso 1: 2 + 3 = 5.0
# caso 2: -10 - 5 = -15.0
# caso 3: 4 * 6 = 24.0
# caso 4: 1 / 3 = 0.3
# caso 5: 2 / 3 = 0.7

secuencia = input("Expression: ").split()
op1 = float(secuencia[0])
operacion  = secuencia[1]
op2 = float(secuencia[2])

if operacion == '+':
    resultado = op1 + op2
elif operacion == '-':
    resultado = op1 - op2
elif operacion == '*':
    resultado = op1 * op2
else:
    resultado = op1 / op2

print(f"{resultado:.1f}")