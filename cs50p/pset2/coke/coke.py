# caso 1
# Amount Due: 50                                                       
# Insert Coin: 25                                                                 
# Amount Due: 25                                                                  
# Insert Coin: 5 
# Amount Due: 20                                                                  
# Insert Coin: 10    
# Amount Due: 10                                                                  
# Insert Coin: 10                                                                                                                              
# Change Owed: 0

# caso 2
# Amount Due: 50     
# Insert Coin: 50     
# Amount Due: 50    
# Insert Coin: 25  
# Amount Due: 25 
# Insert Coin: 25 
# Change Owed: 0

# caso 3
# Amount Due: 50     
# Insert Coin: 18  
# Amount Due: 50  
# Insert Coin: 25  
# Amount Due: 25 
# Insert Coin: 25 
# Change Owed: 0                                                  

# caso 4
# Amount Due: 50     
# Insert Coin: 25
# Amount Due: 25   
# Insert Coin: 10
# Amount Due: 15  
# Insert Coin: 25
# Change Owed: 10  

precio = 50                
amount = precio
monedas_aceptadas = [5, 10, 25]

while amount > 0:
    print("Amount Due:", amount)
    coin = int(input("Insert Coin: "))
    if coin in monedas_aceptadas:
        amount -= coin

change = abs(amount)
print("Change Owed:", change)