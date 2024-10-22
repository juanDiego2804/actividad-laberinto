#Juan Diego Castro Mariscal
#Jose Antonio Castro Mariscal



# Definir la función para encontrar el camino
def encontrarCamino(laberinto, i, j, camino):
    filas = len(laberinto)
    columnas = len(laberinto[0])

    # Condición de éxito: Si llegamos a la salida
    if laberinto[i][j] == 2:
        camino.append((i, j))  # Añadir la posición de la salida al camino
        return True

    # Si la posición actual es un camino (0) y no hemos visitado
    if laberinto[i][j] == 0:
        # Marcar la posición actual como visitada
        laberinto[i][j] = -1  # Usamos -1 para marcar las casillas visitadas
        camino.append((i, j))  # Añadir la posición actual al camino

        # Explorar direcciones (arriba, abajo, izquierda, derecha)
        if i > 0 and encontrarCamino(laberinto, i - 1, j, camino):  # Arriba
            return True
        if i < filas - 1 and encontrarCamino(laberinto, i + 1, j, camino):  # Abajo
            return True
        if j > 0 and encontrarCamino(laberinto, i, j - 1, camino):  # Izquierda
            return True
        if j < columnas - 1 and encontrarCamino(laberinto, i, j + 1, camino):  # Derecha
            return True

        # Si ninguna dirección es válida, hacemos backtracking
        camino.pop()  # Eliminar la posición actual del camino
        laberinto[i][j] = 0  # Desmarcar la posición para futuras búsquedas

    return False

# Definir el laberinto como una matriz de 6x6
laberinto = [
    [0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 2]  # La salida está en [5][5]
]

# Iniciar la búsqueda desde la entrada (0, 0)
camino = []
if encontrarCamino(laberinto, 0, 0, camino):
    print("Camino encontrado:", camino)
else:
    print("No se encontró un camino")