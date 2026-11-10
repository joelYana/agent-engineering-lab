# Caso 1: 
# camelCase: hola                                                  
# snake_case: hola

# Caso 2: 
# camelCase: holaQueTal                                                 
# snake_case: hola_que_tal

# Caso 3: 
# camelCase: holaQue                                             
# snake_case: hola_que

# Caso 4:
# camelCase: holaQ
# snake_case: hola_q

camel = input("camelCase: ")
snake = ''

for letra in camel:
    if letra.isupper():
        snake += '_'
        snake += letra.lower()
    else:
        snake += letra

print("snake_case:", snake)