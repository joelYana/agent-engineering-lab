name = input("What's your name? ")

match name:
    case "Raphinha" | "Lamine" | "Pedri":
        print("Barcelona")
    case "Mbappe":
        print("Real Madrid")
    case _:
        print("No found")