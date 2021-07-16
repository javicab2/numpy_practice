# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 20:12:36 2021

@author: Javicab2
"""
import numpy as np

array_a = np.array([1,2,3,4,5]) #vector

print(array_a)
print(array_a.shape)  #tamaño 

array_b = np.array([[1,2,3,4,5],[6,7,8,9,10]]) #matriz

print(array_b)
print(array_b.shape)
print(array_b.size)    #fila por columna


array_c = array_b.T #transpuesta

print(array_c)

array_c = array_b.reshape(5,2) #reforma el array (debe mantener el size)

print(array_c)

print(array_c[0,1]) #imprime el elemento [0,1]

print(array_c[:,1]) #imprime todos los elementos de la columna 1


############### default arrays ####################

array_d = np.array([[1,2,3],[4,5,6]],dtype=float) #fuerza el tipo de dato
print(array_d)

array_d = np.zeros((2,4),dtype=int)  #zeros
print(array_d)

array_d = np.ones((2,4),dtype=int)  #unos
print(array_d)

array_d = np.full((2,4),4)   #llenar con un numero 
print(array_d)

array_d = np.random.random((2,4))  #random
print(array_d)

############### advanced indexing #################

print(array_d[:,1:3:1])  #slice columna inicial:columna final (no incluye),paso
print(array_d[:,-1:-3:-1])          #indexación negativa

mayor_que_3 = array_b>3     #array booleano 
print(mayor_que_3)

array_menor_3 = np.where(array_b>3,array_b,0) #metodo where, primero la condicion,dato si se cumple,dato si no cumple
print(array_menor_3)

array_menor_4_mayor_2 =np.logical_and(array_b<4,array_b>2)     #logical and, requiere las dos condiciones
print(array_menor_4_mayor_2)

print(array_b[array_menor_4_mayor_2])

########################### array math  ###############

array_x = np.array([[1,2],[3,4]])
array_y = np.array([[2,2],[6,6]])

#operaciones con un array 

print(array_x.sum())    #suma todos los elementos, si le agregamos arg axis = 0 suma col, axis = 0 suma fila
print(array_x.sum(axis=0))  
print(array_x.cumsum()) #suma acumulada de los elementos anteriores
print(array_x.prod())   #multiplicacion
print(array_x.cumprod()) #multiplicacion e los elementos anteriores

#operaciones con mas de un array

print(array_x + array_y)      #son todas operaciones uno a uno
print(array_x - array_y)
print(array_x * array_y)
print(array_x / array_y)

print(np.dot(array_x,array_y))   #multiplicacion vectorial de matrices

################# broadcasting ###################
#significa que si queremos realizar operaciones sin que tengan el tamaño adecuado broadcasting completa los elementos faltantes repitiendo los elementos 

array_z = np.array([[1,2]])

print(array_x + array_z)