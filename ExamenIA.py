#Examen
import math
import random 
from functools import partial
rand = partial(random.randint)
def pesos():
    tamaño_entrada = 5
    numero_ocultas = 5
    tamaño_salida = 1
    random.seed(7)
    capa_oculta = [[random.randint(-100,100)/100 for _ in range(tamaño_entrada + 1)]
                   for _ in range(numero_ocultas)]
    capa_salida = [[random.randint(-100,100)/100 for _ in range(numero_ocultas + 1)]
                   for _ in range(tamaño_salida)]
    return capa_oculta,capa_salida
ocu,salida = pesos()
print(ocu)
print(salida)
