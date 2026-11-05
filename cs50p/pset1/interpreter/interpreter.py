# caso 1: 2 + 3 = 5.0
# caso 2: -10 - 5 = -15.0
# caso 3: 4 * 6 = 24.0
# caso 4: 1 / 3 = 0.3
# caso 5: 2 / 3 = 0.7

op1, operacion, op2 = input("Expression: ").split()
op1 = float(op1)
op2 = float(op2)

if operacion == '+':
    resultado = op1 + op2
elif operacion == '-':
    resultado = op1 - op2
elif operacion == '*':
    resultado = op1 * op2
else:
    resultado = op1 / op2

print(f"{resultado:.1f}")