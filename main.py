import numpy as np
import random 
from funciones import *
from clases import Tablero


#Jugador_local = Tablero('Id_local')
#print(Jugador_local.inicializar_tablero_local())


#tablero_local = inicializar_tablero_local()
#tablero_visitor = inicializar_tablero_visitor()

tablero_local, Id_local = inicializar_tablero_local
tablero_visitor, Id_visitor = inicializar_tablero_visitor



tablero_disparos_visitor = np.full((10,10), '__')
tablero_disparos_local = np.full((10,10), '__')

aciertos_jugador1 = 0
aciertos_jugador2 = 0

tablero_local = barcos_local(tablero_local)
tablero_visitor = barcos_visitor(tablero_visitor)


while aciertos_jugador1 < 20 and aciertos_jugador2 < 20:
    print('Turno jugador 1')
    tablero_disparos_local, aciertos_local = shooting_local(tablero_disparos_local)
    aciertos_jugador1 = aciertos_jugador1 + aciertos_local
    print(tablero_disparos_local)
    print('J1 lleva', aciertos_jugador1, 'aciertos')

    if aciertos_jugador1 >= 20:
        print('Jugador 1 ha ganado')
        break

    print('Turno jugador 2')
    tablero_disparos_visitor, aciertos_visitor = shooting_visitor(tablero_disparos_visitor)
    aciertos_jugador2 = aciertos_jugador2 + aciertos_visitor
    print('J2  lleva', aciertos_jugador2, 'aciertos')
    
    if aciertos_jugador1 >= 20:
        print('Jugador 1 ha ganado')
        break

