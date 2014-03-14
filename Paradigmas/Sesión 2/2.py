piedras = 50
ganador = 0
while (piedras > 0):
    print "Piedras restantes:", piedras

    p1 = int(raw_input("Piedras que retira el jugador 1 (1 - 5): "))
    piedras = piedras - p1

    if piedras <= 0:
        ganador = 1

    print "Piedras restantes:", piedras
        
    p2 = int(raw_input("Piedras que retira el jugador 2 (1 - 5): "))
    piedras = piedras - p2

    if piedras <= 0:
        ganador = 2

print "Ha ganado el jugador numero", ganador
