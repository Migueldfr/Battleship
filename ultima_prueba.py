import numpy as np
import random
import time
from clases import Tablero




def inicializar_tablero_local(tamaño = 10):
    print('Muy buenas, hoy vamos a jugar al hundir la flota')
    Id_local = input('Aqui necesito del primer jugador: ')
    print('Bienvenido ' + Id_local + ' hoy jugaras de local')
    tablero_local = np.full((10,10), ' ')
    return tablero_local, Id_local
def inicializar_tablero_visitor():
    time.sleep(2)
    Id_visitor = random.choice(['Manuel','Carlos','Cesar'])
    print('Bienvenido ' + str(Id_visitor) + ' hoy jugaras como visitante')
    tablero_visitor = np.full((10,10), ' ')
    return tablero_visitor, Id_visitor



tablero_local, Id_local = inicializar_tablero_local()
tablero_visitor, Id_visitor = inicializar_tablero_visitor()
Id_local
Id_visitor





def colocar_barco(barco,tablero):
    for casilla in barco:
        tablero[casilla] = 'O'
    return tablero


def barcos_visitor(tablero_visitor):
    barco_eslora_4 = [(1,1),(1,2),(1,3),(1,4)]
    barco_eslora_3_1 = [(3,0),(3,1),(3,2)] 
    barco_eslora_3_2 = [(3,4),(4,4),(5,4)]
    barco_eslora_2_1 = [(6,9),(5,9)]
    barco_eslora_2_2 = [(6,1),(6,2)]
    barco_eslora_2_3 = [(8,1),(8,2)]
    barco_eslora_1_1 = [(8,8)]
    barco_eslora_1_2 = [(6,6)]
    barco_eslora_1_3 = [(3,9)]
    barco_eslora_1_4 = [(2,7)]
    tablero_visitor = tablero_visitor = np.full((10,10), ' ')
    asignaciones = 0
    eslora = [4,3,2,1]
    while asignaciones < 10:
    
        num_pos = int(input(f'Dime numero de posiciones quieres que tenga tu barco, {Id_visitor}\n'))
        if num_pos in eslora:
            if num_pos == 4:
                print('Solo tienes un barco con estas caracteristicas')
                colocar_barco(barco_eslora_4,tablero_visitor)
                asignaciones += 1
                eslora.remove(4)
                print('te quedan con estas posiciones', eslora)
            elif num_pos == 3:
                print('Tienes dos barcos de estas caracteristicas')
                colocar_barco(barco_eslora_3_1,tablero_visitor)
                colocar_barco(barco_eslora_3_2,tablero_visitor)
                asignaciones += 2
                eslora.remove(3)
                print('te quedan con estas posiciones', eslora)
            elif num_pos == 2:
                print('tienes tres barcos con estas caracteristicas')
                colocar_barco(barco_eslora_2_1,tablero_visitor)
                colocar_barco(barco_eslora_2_2,tablero_visitor)
                colocar_barco(barco_eslora_2_3,tablero_visitor)
                asignaciones += 3
                eslora.remove(2)
                print('te quedan con estas posiciones', eslora)
            elif num_pos == 1:
                print('Tienes 4 barcos con estas carcteristicas')
                colocar_barco(barco_eslora_1_1,tablero_visitor)
                colocar_barco(barco_eslora_1_2,tablero_visitor)
                colocar_barco(barco_eslora_1_3,tablero_visitor)
                colocar_barco(barco_eslora_1_4,tablero_visitor)
                asignaciones +=4     
        else:
            print('Elige otro porque este es invalido')
        
    
    print(tablero_visitor)
    return tablero_visitor

def barcos_local(tablero_local):
    time.sleep(2)
    print(f'Primero vamos a probar a introducir los barcos manualmente porque estamos testeando la demo, jugador {Id_local}\n')
    barco_eslora_4 = [(0,9),(1,9),(2,9),(3,9)]
    barco_eslora_3_1 = [(8,6),(8,7),(8,8)] 
    barco_eslora_3_2 = [(9,1),(9,2),(9,3)]
    barco_eslora_2_1 = [(2,5),(2,6)]
    barco_eslora_2_2 = [(5,2),(5,3)]
    barco_eslora_2_3 = [(7,0),(7,1)]
    barco_eslora_1_1 = [(6,6)]
    barco_eslora_1_2 = [(0,4)]
    barco_eslora_1_3 = [(5,9)]
    barco_eslora_1_4 = [(2,1)]
    tablero_local = np.full((10,10), ' ')
    asignaciones = 0
    eslora = [4,3,2,1]
    while asignaciones < 10:
        time.sleep(2)
        num_pos = int(input(f'Dime numero de posiciones quieres que tenga tu barco\n'))
        if num_pos in eslora:
            if num_pos == 4:
                print('Solo tienes un barco con estas caracteristicas')
                colocar_barco(barco_eslora_4,tablero_local)
                asignaciones += 1
                eslora.remove(4)
                print('te quedan con estas posiciones', eslora)
            elif num_pos == 3:
                print('Tienes dos barcos de estas caracteristicas')
                colocar_barco(barco_eslora_3_1,tablero_local)
                colocar_barco(barco_eslora_3_2,tablero_local)
                asignaciones += 2
                eslora.remove(3)
                print('te quedan con estas posiciones', eslora)
            elif num_pos == 2:
                print('tienes tres barcos con estas caracteristicas')
                colocar_barco(barco_eslora_2_1,tablero_local)
                colocar_barco(barco_eslora_2_2,tablero_local)
                colocar_barco(barco_eslora_2_3,tablero_local)
                asignaciones += 3
                eslora.remove(2)
                print('te quedan con estas posiciones', eslora)
            elif num_pos == 1:
                print('Tienes 4 barcos con estas carcteristicas')
                colocar_barco(barco_eslora_1_1,tablero_local)
                colocar_barco(barco_eslora_1_2,tablero_local)
                colocar_barco(barco_eslora_1_3,tablero_local)
                colocar_barco(barco_eslora_1_4,tablero_local)
                asignaciones +=4     
        else:
            print('Elige otro porque este es invalido')
    
    print ('Ya has terminado de asignar barcos, y asi queda tu tablero', Id_local)
    print(tablero_local)
    return tablero_local




##\tablero_visitor_con_barcos = barcos_visitor(tablero_visitor)
##\
#tablero_local_con_barcos = barcos_local(tablero_local)



tablero_disparos_visitor = np.full((10,10), '__')
# print('Este es tu tablero de disparos hasta el momento', Id_visitor)


tablero_disparos_local = np.full((10,10), '__')
#print('Asi es como llevas taladrada la maquina')


def orden_disparar():
    disparo = []
    while True:
        

            fila = int(input('A que fila quieres disparar?\n'))

            if fila < 0 or fila >= 10:
                    print("Coordenadas erroneas, elige otra")
                    continue
            else:
                disparo.append(fila)
                columna = int(input('A que columna quieres disparar?\n'))
            if fila == 'Exit':
                pass 
            print('Escribe otro valor de columna porque salta un error')
            if columna < 0 or columna >= 10:
                print('Coordenadas erroneas, elige otra')
                continue
            else:
                disparo.append(columna)
                break
        
    return tuple(disparo)



def shooting_local(tablero_disparos_local):
    
    contador = 0
    aciertos = 0
    while contador >= 0:
        disparo = orden_disparar()
        if tablero_disparos_visitor[disparo] == 'X' or tablero_disparos_visitor[disparo] == '-':
            print('Vuelve a disparar')
            aciertos += 0
            pass
        if tablero_visitor[disparo] == 'O':
            print("Has acertado, es un barco")
            tablero_disparos_local[disparo] = 'X'
            tablero_visitor[disparo]= "X"
            contador += 1
            aciertos += 1
            print('Asi queda tu tablero de disparos \r' , tablero_disparos_local)
        if tablero_visitor [disparo] == " ":
            print('Has fallado, es agua')
            tablero_disparos_local[disparo] = '*'
            tablero_visitor [disparo] = '*'
            contador = -1
            print('Asi quedaria tu tablero \n', tablero_disparos_local)
            break
    print('Estos son tus aciertos', aciertos)
    return (tablero_disparos_local, aciertos)
    


def shooting_visitor(tablero_disparos_visitor):
    
    contador = 0
    aciertos = 0
    while contador >= 0:
        disparo = orden_disparar()
        if tablero_disparos_visitor[disparo] == 'X' or tablero_disparos_visitor[disparo] == '-':
            print('Vuelve a disparar')
            aciertos += 0
            pass
        if tablero_local[disparo] == 'O':
            print("Has acertado, es un barco")
            tablero_disparos_visitor[disparo] = "X"
            tablero_local[disparo] = 'X'
            contador += 1
            aciertos += 1
            #print('Asi queda tu tablero de disparos', disparos_visitor)
        if tablero_local [disparo] == " ":
            print('Has fallado, es agua')
            tablero_disparos_visitor[disparo] = '*'
            tablero_local [disparo] == '*'
            contador = -1
            #print('Asi quedaria tu tablero \n', disparos_visitor)
            break
    # print(f'Estos son tus aciertos {}', acierId_localtos)
    return (tablero_disparos_visitor, aciertos)






aciertos_jugador1 = 0
aciertos_jugador2 = 0

tablero_local = barcos_local(tablero_local)
tablero_visitor = barcos_visitor(tablero_visitor)


while aciertos_jugador1 < 20 and aciertos_jugador2 < 20:
    print(f'Turno {Id_local}')
    print(tablero_disparos_local)
    tablero_disparos_local, aciertos_local = shooting_local(tablero_disparos_local)
    aciertos_jugador1 = aciertos_jugador1 + aciertos_local
    print('J1 lleva', aciertos_jugador1, 'aciertos')

    if aciertos_jugador1 >= 20:
        print('Jugador 1 ha ganado')
        break

    print(f'Turno {Id_visitor}')
    tablero_disparos_visitor, aciertos_visitor = shooting_visitor(tablero_disparos_visitor)
    aciertos_jugador2 = aciertos_jugador2 + aciertos_visitor
    print('J2  lleva', aciertos_jugador2, 'aciertos')
    
    if aciertos_jugador1 >= 20:
        print('Jugador 1 ha ganado')
        break