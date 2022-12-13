
import random
import numpy as np
import Modo_Hundir_flota.funciones as funciones



filas = 10
columnas = 10
mar = ' '
mar_disparado = '*'
barco = 'O'
barco_disparado = 'X'
vidas = 20

tablero_visitor_con_barcos = np.full((10,10), ' ')
tablero_local_con_barcos = np.full((10,10), ' ')

tablero_disparos_visitor = np.full((10,10), '__')
tablero_disparos_local = np.full((10,10), '__')


