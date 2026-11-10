# Empieza con al menos dos letras
# caso 1:
# Plate: HE                                                                   
# Valid 
# caso 2:
# Plate: H2                                                                  
# Invalid 

# Max 6 caracteres, min 2
# caso 1:
# Plate: HELLOO                                                                   
# Valid 
# caso 2:
# Plate: HALLOOU                                                             
# Invalid 

# Numeros al final y no comience en 0
# caso 1:
# Plate: HOLA50                                                            
# Valid 
# caso 2:
# Plate: HALL2A                                                      
# Invalid 
# caso 3:
# Plate: HALL02                                                   
# Invalid 

# No puntuaciones guiones ni espacios
# caso 1:
# Plate: HOLAAA                                                           
# Valid 
# caso 2:
# Plate: HA L                                                  
# Invalid 
# caso 3:
# Plate: HA_                                                 
# Invalid 

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    return longitud_valida(s) and empieza_dos_letras(s) and solo_alfanumericos(s) and numeros_al_final(s)

# En is_valid la func longitud va primero porq en esta con una entrada de una letra falla
def empieza_dos_letras(s):
    return s[0].isalpha() and s[1].isalpha()

def longitud_valida(s):
    return 2 <= len(s) <= 6 

def solo_alfanumericos(s):
    return s.isalnum()

def numeros_al_final(s):
    hay_numero = False
    for caracter in s:
        if caracter.isnumeric() and not hay_numero:
            hay_numero = True
            if int(caracter) == 0:
                return False
        elif caracter.isalpha() and hay_numero:
            return False    
        
    return True

if __name__ == "__main__":
    main()