# caso 1: 2 + 3 = 5.0
# caso 2: -10 - 5 = -15.0
# caso 3: 4 * 6 = 24.0
# caso 4: 1 / 3 = 0.3
# caso 5: 2 / 3 = 0.7

# Especificación

# 1. Entradas que debe rechazar:
#    - 1+1
#    - 1 + 1 + 1
#    - 5 ^ 2
#    - a + 1

# 2. Manejo de entradas incorrectas:
#    - Mostrar: "Datos incorrectos, reingrese los datos. Ejemplo: 1 + 1".
#    - Solicitar nuevamente los datos hasta que sean válidos.

# 3. División entre cero:
#    - Mostrar: "No se puede dividir entre 0".
#    - Solicitar nuevos números para realizar el cálculo.
#    - Manejar ZeroDivisionError mediante except.

# 4. Operadores no permitidos:
#    - Utilizar raise para rechazar operadores como "^".
#    - Actualmente, "5 ^ 2" se procesaría en el bloque else.

def main():
    while True:
        texto = input("Expression: ")
        try:
            resultado = calcular_operacion(texto)
        except ValueError:
            print("Reingrese los datos, ejm: 1 + 1")
        except ZeroDivisionError:
            print("No se puede dividir entre 0")
        else:
            print(f"{resultado:.1f}")
            break

def calcular_operacion(texto):
    op1, operador, op2 = texto.split()
    op1 = float(op1)
    op2 = float(op2)

    if operador == '+':
        resultado = op1 + op2
    elif operador == '-':
        resultado = op1 - op2
    elif operador == '*':
        resultado = op1 * op2
    elif operador == '/':
        resultado = op1 / op2
    else:
        raise ValueError("Operador no válido")

    return resultado

if __name__ == "__main__":
    main()