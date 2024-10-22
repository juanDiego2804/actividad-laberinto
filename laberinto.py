#Juan Diego Castro Mariscal
#Jose Antonio Castro Mariscal
def imprimirLaberinto(laberinto):
    for fila in laberinto:
        print(" ".join(str(celda) for celda in fila))  # Unimos los elementos de cada fila en una cadena separada por espacios



def preguntas(): #preguntas/acertijos para el caso de que caiga en cierta casilla
    print("Responde minimo 2 preguntas bien para poder avanzar\n")
    aciertos=0
    print("Este paradigma sugiere la solucion de cada subproblema una unica vez y guardar un registro de los resultados de donde la solucion al problema original puede ser obtenida")
    print("1. Fuerza Bruta")
    print("2. Divide y venceras")
    print("3. Programacion dinamica")
    respuesta= int(input("Respuesta: "))
    if respuesta==3:
        aciertos=aciertos+1
        
    print("\nVoy camino al aeropuerto, de camino veo sentadas a 3 personas, cada una con 2 cajas, y en cada una de las bolsas hay 7 perritos,¿Cuantos vamos al aeropuerto?")
    respuesta2=int(input("Respuesta: "))
    if respuesta2==1:
        aciertos=aciertos+1
    
    print("\nQuien es el futbolista con mas goles anotados de toda la historia: ")
    print("1.Lionel Messi")
    print("2.Cristiano Ronaldo")
    print("3.Pele")
    respuesta3= int(input("Respuesta: "))
    if respuesta3==2:
        aciertos=aciertos+1
    
    print("\nNumero de respuestas correctas: ",aciertos)
    if aciertos>=2:
        return True
    else:
        return preguntas()
        

#Algoritmo principal usando programacion dinamica
def encontrarCamino(laberinto, i, j, camino): # i para las filas,  j para las columnas
    filas = len(laberinto)
    columnas = len(laberinto[0])

    # Condición de éxito: Si llegamos a la salida
    if laberinto[i][j] == 2:
        camino.append((i, j))  # Añadir la posición de la salida al camino
        return True

    # Si la posición actual es un camino (0) y no hemos visitado
    if laberinto[i][j] == 0:
        if i==1 and j==1:
            print("Caiste en la celda (1,1), responde las preguntas: ")
            
            preguntas()
            
            
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

        # Si ninguna dirección es válida, regresamos
        camino.pop()  # Eliminar la posición actual del camino
        laberinto[i][j] = 0  # Desmarcar la posición para futuras búsquedas

    return False

def ejecutarEjemploDeUso(laberinto,i):
    print("\n\nLaberinto inicial #",i)
    imprimirLaberinto(laberinto)
    print("\n\n")
    # Iniciar la búsqueda desde la entrada (0, 0)
    camino = []
    if encontrarCamino(laberinto, 0, 0, camino):
        print("Camino encontrado:", camino)
    else:
        print("No se encontró un camino")
     

# Definir el laberinto como una matriz de 6x6
laberinto1 = [#laberinto donde cae en celda (1,1), debe responder preguntas
    [0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 2]  # La salida está en [5][5]
]


#Ejemplo con laberinto2
laberinto2 = [#laberinto donde no hay camino posible
    [0, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 2]  
]



#Ejemplo con laberinto3
laberinto3 = [ #laberinto donde no cae en las preguntas
    [0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 2]  
]


ejecutarEjemploDeUso(laberinto1,1)


ejecutarEjemploDeUso(laberinto2,2)


ejecutarEjemploDeUso(laberinto3,3)