# Escribe un programa que calcule la raíz cuadrada de un número utilizando el método de Newton-Raphson

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import datetime
import numpy as np


def raiz_cuadrada(n):
    x = n
    while True:
        raiz = 0.5 * (x + n / x)
        if abs(x - raiz) < 1e-9:
            break
        x = raiz
    return raiz


numero = float(input("Introduce un número: "))
raiz = raiz_cuadrada(numero)
print("La raíz cuadrada de", numero, "es", raiz)


# Escribe un programa que pida al usuario una cadena de texto y cuente cuántas veces aparece cada letra en la cadena.
cadena = input("Introduce una cadena de texto: ")
frecuencias = {}
for letra in cadena:
    if letra in frecuencias:
        frecuencias[letra] += 1
    else:
        frecuencias[letra] = 1

print("Frecuencias de letras en la cadena:")
for letra, frecuencia in frecuencias.items():
    print(letra, ":", frecuencia)


# Escribe un programa que genere una lista de números aleatorios y calcule la media, la mediana y la desviación estándar de la lista.
# istallar pip install numpy


n = int(input("Introduce el tamaño de la lista: "))
minimo = int(input("Introduce el valor mínimo de la lista: "))
maximo = int(input("Introduce el valor máximo de la lista: "))

lista = np.random.randint(minimo, maximo + 1, size=n)
media = np.mean(lista)
mediana = np.median(lista)
desviacion_estandar = np.std(lista)

print("Lista generada:", lista)
print("Media:", media)
print("Mediana:", mediana)
print("Desviación estándar:", desviacion_estandar)

# Programa para calcular la diferencia en días entre dos fechas:


fecha1 = input("Introduce la primera fecha (AAAA-MM-DD): ")
fecha2 = input("Introduce la segunda fecha (AAAA-MM-DD): ")

fecha1_dt = datetime.datetime.strptime(fecha1, '%Y-%m-%d')
fecha2_dt = datetime.datetime.strptime(fecha2, '%Y-%m-%d')

diferencia = fecha2_dt - fecha1_dt

print(f"La diferencia entre {fecha1} y {fecha2} es de {diferencia.days} días.")


