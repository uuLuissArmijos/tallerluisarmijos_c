from math import sqrt

def distancia (x1,y1,x2,y2):
    """
    Calcula la distancia euclidiana entre dos puntos en un plano cartesiano.
​
    Parámetros:
    x1 (float): La coordenada x del primer punto.
    y1 (float): La coordenada y del primer punto.
    x2 (float): La coordenada x del segundo punto.
    y2 (float): La coordenada y del segundo punto.
​
    Retorna:
    float: La distancia euclidiana entre los dos puntos.
    """
    respuesta= sqrt((x2-x1)**2+(y2-y1)**2)
    return respuesta