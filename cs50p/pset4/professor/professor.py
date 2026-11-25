# $ python professor.py                                               
# Level: 1                                               
# 2 + 8 = 10                             
# 3 + 7 = 10                                                     
# 9 + 4 = 10                                                              
# EEE                                                                     
# 9 + 4 = 11                                                                                  
# EEE                                                                    
# 9 + 4 = 12                                                                         
# EEE                                                                           
# 9 + 4 = 13                                                                       
# 2 + 9 = 11
# 1 + 4 = 5
# 9 + 5 = 14                                                              
# 2 + 1 = 3
# 1 + 5 = 6
# 2 + 4 = 6
# 1 + 6 = 7
#Score: 9

# $ python professor.py                                               
# Level: -1       
# Level: 1                                    
# 2 + 8 = 10                             
# 3 + 7 = 10                                                     
# 9 + 4 = 10                                                              
# EEE                                                                     
# 9 + 4 = 11                                                                                  
# EEE                                                                    
# 9 + 4 = 12                                                                         
# EEE                                                                           
# 9 + 4 = 13                                                                       
# 2 + 9 = 11
# 1 + 4 = 5
# 9 + 5 = 14                                                              
# 2 + 1 = 3
# 1 + 5 = 6
# 2 + 4 = 6
# 1 + 6 = 7
# Score: 9

# $ python professor.py
# Level: a
# Level: 2
# 22 + 88 = 110
# 33 + 77 = 110
# 99 + 44 = 100
# EEE
# 99 + 44 = 115
# EEE
# 99 + 44 = 145
# EEE
# 99 + 44 = 143
# 22 + 99 = 121
# 11 + 44 = 55
# 99 + 55 = 154
# 22 + 11 = 33
# 11 + 55 = 66
# 22 + 44 = 66
# 11 + 66 = 77
# Score: 9

import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        flag = False

        for _ in range(3): 
            try:
                rpta = int(input(f"{num1} + {num2} = "))
            except ValueError:
                print("EEE")
            else:
                if rpta == num1 + num2:
                    score += 1
                    flag = True
                    break
                else:
                    print("EEE")

        correcta = num1 + num2 
        if not flag:
            print(f"{num1} + {num2} = {correcta}")

    print(f"Score: {score}")

def valida_level(level):
    nivel = int(level)
    if 1 <= nivel <= 3:
        return nivel
    else:
        raise ValueError("Nivel fuera de rango")

def get_level():
    while True:
        level = input("Level: ")
        try:
            level_validado = valida_level(level)
        except ValueError:
            pass
        else:
            return level_validado

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Nivel fuera de rango")


if __name__ == "__main__":
    main()