#!/usr/bin/python3

from time import *
from random import *
import random
import string


def creaListaObjetos(cantidad):
    elementos = []
    lista_enteros=[]
    lista_flotantes=[]
    lista_cadenas=[]
    listaOrdenada = []
    # Llenamos la lista con diferentes tipos
    while len(elementos) != cantidad:
        if len(elementos) < cantidad:
            elementos.append(random.choice(string.ascii_letters))
        if len(elementos) < cantidad:
            elementos.append(float(round(uniform(1.0, 2.0), 1)) ) # con 1 decimal
        if len(elementos) < cantidad:
            elementos.append(randint(1,100))

    # Ordenamos la lista de objetos
    inicio = time()
    for elemento in elementos:
        if isinstance(elemento, int): # sí es un entero
            lista_enteros.append(elemento)
        elif isinstance(elemento, float):
            lista_flotantes.append(elemento)
        elif isinstance(elemento, str):
            lista_cadenas.append(elemento)
    listaOrdenada = sorted(lista_enteros) + sorted(lista_cadenas) + sorted(lista_flotantes)
    
    print("---------------------------------------------------------")
    print("ORDENAMIENTO EN LA LISTA DE OBJETOS") 
    #print("Lista de objetos ordenada : ", listaOrdenada)
    final = time() - inicio
    tiempo = float(final*1000)
    print("Tiempo : ", tiempo, " ms")
   
    return elementos


""" Separa lista de objetos en listas A,B,C """
def separaListas(lista, tipo_de_lista):
    lista_enteros=[]
    lista_flotantes=[]
    lista_cadenas=[]
    # Agregamos a las listas según su tipo
    for elemento in lista:
        if isinstance(elemento, int): # sí es un entero
            lista_enteros.append(elemento)
        elif isinstance(elemento, float):
            lista_flotantes.append(elemento)
        elif isinstance(elemento, str):
            lista_cadenas.append(elemento)
        
    # Ordenamos la lista que haya elegido el usuario
    inicio = time()
    try:
        if tipo_de_lista == 1:
            lista_cadenas.sort() # Lista de cadenas
        if tipo_de_lista == 2:
            lista_flotantes.sort() # Lista de flotantes
        if tipo_de_lista == 3:
            lista_enteros.sort() # Lista de enteros
    except:
        print("Error inesperado")

    #print(lista_cadenas, lista_enteros, lista_flotantes)
    if tipo_de_lista == 1 or tipo_de_lista == 2 or tipo_de_lista == 3:
        final = time() - inicio 
        tiempo = float(final*1000) 
        print("Tiempo : ", tiempo, " ms")
    else:
        print("¡Haz introducido una opción no válida!")



objetos=creaListaObjetos(10000) # 10000 elementos
print("---------------------------------------------------------")
print("ORDENAMIENTO EN LA LISTA DE UN SÓLO DATO")
try: # validamos que solo ingrese enteros
    tipo = int(input("Lista que desea comparar\n 1) Cadena de texto \n 2) Flotante \n 3) Entero\n : "))
    lista_unica=separaListas(objetos, tipo)
    #print("Tiempo lista única : ", lista_unica, " ms")
except:
    print("Haz introducido una entrada que no es un número")

print("---------------------------------------------------------")











