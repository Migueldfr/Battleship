

import numpy as np 
import random



class Tablero():

    def __init__ (self, id_jugador, tamaño = 10):
        self.id_jugador = id_jugador
        self.tamaño = tamaño
    
    def inicializar_tablero_local(tamaño = 10):
        '''
        Esta funcion sirve para presentar el juego e inicializar el tablero.
        Donde se recoge el nombre del jugador Local.

        '''
        print('Muy buenas, hoy vamos a jugar al hundir la flota')
        Id_local = input('Aqui necesito tu nombre: ')
        print('Bienvenido ' + Id_local + ' hoy jugaras de local')
        tablero_local = np.full((10,10), ' ')
        return (tablero_local,Id_local)
    def inicializar_tablero_visitor():
        '''
        Esta funcion sirve para presentar el juego e inicializar el tablero.
         Donde se recoge el nombre de la maquina en este caso.
         El output que ejecuta es un random choice entre tres opciones.
        '''
        Id_visitor = random.choice(['Manuel', 'Carlos', 'Cesar'])
        print('Bienvenido ' + str(Id_visitor) + ' hoy jugaras como visitante')
        tablero_visitor = np.full((10,10), ' ')
        return (tablero_visitor,Id_visitor)







class jugador_visitante():
    
    def orden_disparar():
        disparo = []

        while True:
            fila = int(input('A que fila quieres disparar?'))
            if fila <= 0 or fila > 9:
                    print("Coordenadas erroneas, elige otra")
                    continue
            else:
                disparo.append(fila)
    
            columna = int(input('A que columna quieres disparar?'))
            if columna <= 0 or columna > 9:
                print('Coordenadas erroneas, elige otra')
                continue
            else:
                disparo.append(columna)
                break
            
        print(disparo)


    
