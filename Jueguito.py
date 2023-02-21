import random

def comparador(posicion_Player1):

    posicion_pc = int(random.randrange(1,4))
     
    if posicion_Player1 != 1 and posicion_Player1 != 2 and posicion_Player1 != 3: 
        print("opcion invalida")
    else:

        if posicion_Player1 == posicion_pc:
            print("Empate")
        elif posicion_Player1 == 1 and posicion_pc == 2:
            print("Perdiste")
        elif posicion_Player1 == 2 and posicion_pc == 3:
            print("Perdiste")
        elif posicion_Player1 == 3 and posicion_pc == 1:
            print("Perdiste")
        else:
            print("Ganaste")

    
    return


print("** Piedra, Papel O Tijeras")

while True:
    print("Elije entre las 3 opciones")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijeras")
    comparador(int(input("Inserte su opcion: ")))
