# Programa para simular el juego de la vida de Conway
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Tamaño del tablero
n = 50

# Crear tablero aleatorio
tablero = np.random.randint(2, size=(n, n))

# Función para actualizar el tablero en cada iteración
def actualizar_tablero(frameNum, img, tablero, n):
    # Crear copia del tablero actual
    nuevo_tablero = tablero.copy()

    # Recorrer cada celda y actualizar su estado
    for i in range(n):
        for j in range(n):
            # Contar el número de vecinos vivos
            vecinos = int((tablero[i, (j-1)%n] + tablero[i, (j+1)%n] +
                           tablero[(i-1)%n, j] + tablero[(i+1)%n, j] +
                           tablero[(i-1)%n, (j-1)%n] + tablero[(i-1)%n, (j+1)%n] +
                           tablero[(i+1)%n, (j-1)%n] + tablero[(i+1)%n, (j+1)%n]))

            # Aplicar las reglas del juego de la vida
            if tablero[i, j] == 1 and (vecinos < 2 or vecinos > 3):
                nuevo_tablero[i, j] = 0
            elif tablero[i, j] == 0 and vecinos == 3:
                nuevo_tablero[i, j] = 1

    # Actualizar el tablero y mostrarlo
    tablero[:] = nuevo_tablero[:]
    img.set_data(tablero)
    return img,

# Crear animación
fig, ax = plt.subplots()
img = ax.imshow(tablero, cmap='binary')
ani = animation.FuncAnimation(fig, actualizar_tablero, fargs=(img, tablero, n), frames=100, interval=50, blit=True)

plt.show()

