# Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, 
# lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. 

#1: What time is it? 6:59 no imprime  
#2: What time is it? 7:00 breakfast time
#3: What time is it? 8:00 breakfast time
#4: What time is it? 8:01 no imprime  
#5: What time is it? 19:30 no imprime
#6: What time is it? 11:59 no imprime  
#7: What time is it? 12:00 lunch time
#8: What time is it? 13:00 lunch time
#9: What time is it? 13:01 no imprime  
#10: What time is it? 17:59 no imprime  
#11: What time is it? 18:00 dinner time
#12: What time is it? 19:00 dinner time
#13: What time is it? 19:01 no imprime  
# convert("7:30") -> 7.5
# convert("18:15") -> 18.25

def main():
    hora = input("What time is it? ")
    hora_convertida = convert(hora)

    if 7 <= hora_convertida <= 8:
        print("breakfast time")
    elif 12 <= hora_convertida <= 13:
        print("lunch time")
    elif 18 <= hora_convertida <= 19:
        print("dinner time")


def convert(time):
    horas, minutos = time.split(':')
    minutos = float(minutos)/60
    convertida = float(horas) + minutos
    return convertida

if __name__ == "__main__":
    main()