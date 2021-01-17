#Red Neuronal XOR
import math 
def sigmoide(x):
    return 1/(1 + math.exp(-x)) #retorna un solo valor

def producto_punto(v,w):
    return sum(x*y for x,y in zip(v,w)) #suma ponderada de pesos y entradas

def salida_neurona(pesos, entradas):
    return sigmoide(producto_punto(pesos,entradas)) #Llama sigmoide del resultado de producto punto.

    #red_neuronal = lista de listas de pesos
    #entrada = inputs de la capa
    
red_neuronal = [[[20,20,-30],[20,20,-10]], [[-60,60,-30]]]

entrada1 = [0,0]
entrada2 = [1,0]
entrada3 = [0,1]
entrada4 = [1,1]
def ffnn(red_neuronal, entrada):
    salidas=[] 
    for capa in red_neuronal:
        entrada = entrada + [1]
        salida=[salida_neurona(neurona,entrada) for neurona in capa]
        salidas.append(salida)
        entrada = salida
    return salidas

import random 
from functools import partial
rand = partial(random.randint)

    #pesos random entre [-1,1]
def random_nn():
    random.seed(7)
    xor_nn = [#capa oculta, 2 neuronas
                [[rand(-100,100)/100,rand(-100,100)/100,rand(-100,100)/100],
                [rand(-100,100)/100,rand(-100,100)/100,rand(-100,100)/100]],
                [[rand(-100,100)/100,rand(-100,100)/100,rand(-100,100)/100]]
            ]
    return xor_nn

xor_nn = random_nn()

def backpropagation(xor_nn, v_entrada, v_objetivo):
    salidas_ocultas, salidas = ffnn(xor_nn, v_entrada)
    salida_nueva = []
    oculta_nuevo = []
    alfa = 0.1  #usualmente 0.1 es un buen valor
    error = 0.5*sum((salida-objetivo)*(salida-objetivo) for salida, objetivo in zip(salidas, v_objetivo))
    salida_deltas = [salida*(1-salida)*(salida-objetivo) for salida,objetivo in zip(salidas, v_objetivo)]
    for i, neurona_salida in enumerate(xor_nn[-1]):
        for j, salida_oculta in enumerate(salidas_ocultas + [1]):
            neurona_salida[j] -= salida_deltas[i]*salida_oculta*alfa
        salida_nueva.append(neurona_salida)
    ocultas_deltas = [salida_oculta*(1-salida_oculta)*producto_punto(salida_deltas, [n[i] for n in xor_nn[-1]]) for i, salida_oculta in enumerate(salidas_ocultas)]
    for i, neurona_oculta in enumerate(xor_nn[0]):
        for j, input in enumerate(v_entrada + [1]):
            neurona_oculta[j] -= ocultas_deltas[i]*input*alfa
        oculta_nuevo.append(neurona_oculta)
    return oculta_nuevo, salida_nueva, error


promedio_errores_cuadrados=1
i=1
while promedio_errores_cuadrados > 0.0005:
    oculta, salida, error1 = backpropagation(xor_nn,[x*2-1 for x in [1,1]], [0])
    xor_nn = [oculta, salida]
    oculta, salida, error2 = backpropagation(xor_nn,[x*2-1 for x in [0,1]], [1])
    xor_nn = [oculta, salida]
    oculta, salida, error3 = backpropagation(xor_nn,[x*2-1 for x in [1,0]], [1])
    xor_nn = [oculta, salida]
    oculta, salida, error4 = backpropagation(xor_nn,[x*2-1 for x in [0,0]], [0])
    xor_nn = [oculta, salida]
    promedio_errores_cuadrados = (error1+error2+error3+error4)/4
    print("Promedio errores cuadrados:", promedio_errores_cuadrados)
    print("Iteración:",i)
    i=i+i

    #pruebas
print(ffnn(xor_nn, [x*2-1 for x in [1,1]])[-1])
print(ffnn(xor_nn, [x*2-1 for x in [0,1]])[-1])
print(ffnn(xor_nn, [x*2-1 for x in [1,0]])[-1])
print(ffnn(xor_nn, [x*2-1 for x in [0,0]])[-1])
