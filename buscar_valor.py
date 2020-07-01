#!/usr/bin/python3

from time import *
from random import *
import random
import string

usuario = int(input("Cantidad de elementos en la lista : "))
busqueda = input("Valor que desea buscar : ")

def buscaEnListaDeObjetos(valor, cantidad):
    elementos = []
    # Llenamos la lista con diferentes tipos
    while len(elementos) != cantidad:
        if len(elementos) < cantidad:
            elementos.append(random.choice(string.ascii_letters))
        if len(elementos) < cantidad:
            elementos.append(float(round(uniform(1.0, 2.0), 1)) ) # con 1 decimal
        if len(elementos) < cantidad:
            elementos.append(randint(1,100))

    # Buscamos el elemento en la lista de objetos
    inicio = time()
    try:
        if valor.find(".") >= 0: # sí es un decimal
            print("Encontrado index ", elementos.index(float(valor)))
        elif valor.isdigit(): # sí es un entero
            print("Encontrado index ", elementos.index(int(valor)))
        elif valor.isalpha(): # sí es una cadena
            print("Encontrado index ", elementos.index(valor))
        else:
            print("Tipo de cáracter no válido")
    except Exception as error:
        print("Error : ", "el valor ", valor, "no se encuentra en la lista.")

    final = time() - inicio
    tiempo = float(final*1000)
        
    return tiempo

# Busca un elemento en una lista de un solo tipo
def BuscaElementosEnListaUnica(valor, longitud, tipo_de_lista):
    elementos = []
    # Llenamos la lista con diferentes tipos
    while len(elementos) != longitud:
        try:
            if tipo_de_lista == 1:
                elementos.append(random.choice(string.ascii_letters))
            if tipo_de_lista == 2:
                elementos.append(float(round(uniform(1.0, 2.0), 1)) ) # con 1 decimal
            if tipo_de_lista == 3:
                elementos.append(randint(1,100))
        except:
            print("Error inesperado")
    
    # Buscamos el elemento en la lista de un sólo tipo
    inicio = time()
    if valor.isalpha(): # Cadena 
        print("Encontrado index ", elementos.index(valor))
    elif valor.find(".") >= 0: # Flotante
        print("Encontrado index ", elementos.index(float(valor)))
    elif valor.isdigit(): # Entero
        print("Encontrado index ", elementos.index(int(valor)))
    else:
        print("Tipo de datos incorrecto")

    final = time() - inicio
    tiempo = float(final*1000)
        
    return tiempo


# ......................................................................
print("---------------------------------------------------------")
print("BÚSQUEDA EN LA LISTA DE OBJETOS")
tiempo_lista_de_objetos=buscaEnListaDeObjetos(busqueda, usuario)
print("Tiempo lista de objetos : ", tiempo_lista_de_objetos, " ms")
print("---------------------------------------------------------")
print("BÚSQUEDA EN LA LISTA DE UN SÓLO TIPO DE DATO")
try: # validamos que solo ingrese enteros
    tipo = int(input("Lista que desea comparar\n 1) Cadena de texto \n 2) Flotante \n 3) Entero\n : "))
    tiempo_lista_unica=BuscaElementosEnListaUnica(busqueda, usuario, tipo)
    print("Tiempo lista única : ", tiempo_lista_unica, " ms")
except:
    print("Haz introducido una entrada que no es un número")








