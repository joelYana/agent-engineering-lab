# Entrada: heLLo  -> Salida esperada: $0
# Entrada: Hey  -> Salida esperada: $20
# Entrada:   hello  -> Salida esperada: $0
# Entrada:  There you are  -> Salida esperada: $100
# Entrada: Hi  -> Salida esperada: $20
# Entrada: Oh hello  -> Salida esperada: $100

greeting = input("Greeting: ")
greeting = greeting.lstrip().lower()

if greeting.startswith('hello'):
    print("$0")
elif greeting.startswith('h'):
    print("$20")
else:
    print("$100")