jugadores = [
    {"nombre": "Lamine", "equipo": "Barcelona", "pais": "España"},
    {"nombre": "Raphinha", "equipo": "Barcelona", "pais": "Brasil"},
    {"nombre": "Gordon", "equipo": "Barcelona", "pais": "Inglaterra"},
    {"nombre": "Mbappe", "equipo": "Real Madrid", "pais": None},        
]

for jugador in jugadores:
    print(jugador["nombre"], jugador["equipo"], jugador["pais"], sep=', ')