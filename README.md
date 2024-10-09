# Actividad-laberinto
Actividad de la materia de análisis de algoritmos

Alumno1 - Juan Diego Castro Mariscal

Alumno2 - José Antonio Castro Mariscal


Estas en un laberinto misterioso y necesitas encontrar la salida. Este laberinto está representado por una matriz cuadrada en la que algunas celdas son caminos y otras son paredes. El objetivo es encontrar un camino desde la entrada hasta la salida utilizando la estrategia de programación dinámica.

Pasos a realizar:

1- Define una matriz cuadrada (minimo de 6X6) que represente el laberinto. Usar valores como 0 para caminos y 1 para paredes.

2- Establece la ubicación de la entrada, (siempre en 0,0), designa la entrada con el valor 0  y la salida en el laberinto  con el valor 2.

  2.1- Asegúrate de que haya al menos una ruta posible desde la entrada hasta la salida.

3- Implementa un algoritmo de programación dinámica para encontrar un camino desde la entrada hasta la salida del laberinto.

   3.1- Divide el laberinto en secciones más pequeñas y explora recursivamente cada sección para buscar el camino correcto(optar por dividirlo en cuadrantes, filas, columnas u otras subdivisiones creativas).
     -Al implementar la exploración recursiva, asegúrate de que cada subdivisión explore su propia sección del laberinto y/o su solución impacte directamente en las siguientes instancias o porciones del laberinto. Puedes utilizar funciones recursivas para facilitar este       proceso.
   
4- Define una condición de éxito para tu algoritmo. Por ejemplo, considera que el algoritmo tenga éxito cuando encuentra la salida o cuando ha explorado todo el laberinto.

5- Introduce reglas especiales en el laberinto para complicar la exploración, como celdas que teletransportan al explorador a otro lugar, celdas con acertijos,  o celdas teletransportadoras que cambian dinámicamente. (3 lleva al 4 y 4 lleva al 3), entre otras ideas 
   excéntricas.
   
  5.1- Agrega elementos excéntricos al laberinto, como celdas que solo pueden atravesarse en ciertas condiciones o celdas que requieren resolver acertijos para pasar. (crear la celda 111, que si llegan ahi debe hacer una pregunta trivia y no se abre hasta que no se 
       conteste bien)




Objetivos por integrante:

Alumno2:

  Commit 1: realizar los pasos 1, 2 y 2.1     
  Commit 3: realizar el paso 5
    
Alumno1: 

  Commit 2: realizar los pasos 3, 3.1 y 4         
  Commit 4: realizar el paso 5.1

