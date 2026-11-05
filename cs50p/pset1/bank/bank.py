# Entrada: heLLo  -> Salida esperada: $0
# Entrada: Hey  -> Salida esperada: $20
# Entrada:   hello  -> Salida esperada: $0
# Entrada:  There you are  -> Salida esperada: $100
# Entrada: Hi  -> Salida esperada: $20
# Entrada: Oh hello  -> Salida esperada: $100

# Resuelve Home Federal Savings Bank
#Programa bank.py a mano. Tus pruebas deben incluir un saludo con espacios al inicio, uno en mayúsculas y uno donde hello aparezca en 
# medio del texto. 
#Verificación: todas las salidas coinciden con tus predicciones; haces commit y me mandas código y salida.

# Correcto: los seis casos ya cubren los tres resultados posibles y las trampas de espacios, mayúsculas y “hello” en medio.

#Ahora escribe bank.py a mano, debajo de esos comentarios. Necesitas comprobar con qué empieza un texto, y str tiene un método para eso:
#  búscalo en la documentación de métodos de texto, como hiciste con removeprefix.

#Ejecútalo con los seis casos, compara cada salida con tu predicción, haz commit y mándame el código y la salida.

greeting = input("Greeting: ")
greeting = greeting.lstrip().lower()

if greeting.startswith('hello'):
    print("$0")
elif greeting.startswith('h'):
    print("$20")
else:
    print("$100")
