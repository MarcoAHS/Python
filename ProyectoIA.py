import math
import random 
from functools import partial
rand = partial(random.randint)

def sigmoide(x):
    return 1/(1 + math.exp(-x)) #retorna un solo valor

def producto_punto(v,w):
    return sum(x*y for x,y in zip(v,w))
def salida_neurona(pesos, entradas):
    return sigmoide(producto_punto(pesos,entradas))

def ffnn(red_neuronal, entrada):
    salidas=[] 
    for capa in red_neuronal:
        entrada = entrada + [1]
        salida=[salida_neurona(neurona,entrada) for neurona in capa]
        salidas.append(salida)
        entrada = salida
    return salidas
def pesos():
    tamaño_entrada = 25
    numero_ocultas = 5
    tamaño_salida = 10
    random.seed(7)
    capa_oculta = [[random.randint(-100,100)/100 for _ in range(tamaño_entrada + 1)]
                   for _ in range(numero_ocultas)]
    capa_salida = [[random.randint(-100,100)/100 for _ in range(numero_ocultas + 1)]
                   for _ in range(tamaño_salida)]
    return capa_oculta,capa_salida

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

oculta, salida = pesos()
xor_nn=[oculta,salida]
objetivos = [[1 if i == j else 0 for i in range(10)]for j in range(10)]
entradas = [[1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1],
            [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0],
            [1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1],
            [1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1],
            [1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1],
            [1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1],
            [1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1],
            [1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
            [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1],
            [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1]]
promedio_errores_cuadrados=1
i=0
while promedio_errores_cuadrados > 0.0005:
    oculta, salida, error0 = backpropagation(xor_nn,[x*2-1 for x in entradas[0]], objetivos[0])
    xor_nn = [oculta, salida]
    oculta, salida, error1 = backpropagation(xor_nn,[x*2-1 for x in entradas[1]], objetivos[1])
    xor_nn = [oculta, salida]
    oculta, salida, error2 = backpropagation(xor_nn,[x*2-1 for x in entradas[2]], objetivos[2])
    xor_nn = [oculta, salida]
    oculta, salida, error3 = backpropagation(xor_nn,[x*2-1 for x in entradas[3]], objetivos[3])
    xor_nn = [oculta, salida]
    oculta, salida, error4 = backpropagation(xor_nn,[x*2-1 for x in entradas[4]], objetivos[4])
    xor_nn = [oculta, salida]
    oculta, salida, error5 = backpropagation(xor_nn,[x*2-1 for x in entradas[5]], objetivos[5])
    xor_nn = [oculta, salida]
    oculta, salida, error6 = backpropagation(xor_nn,[x*2-1 for x in entradas[6]], objetivos[6])
    xor_nn = [oculta, salida]
    oculta, salida, error7 = backpropagation(xor_nn,[x*2-1 for x in entradas[7]], objetivos[7])
    xor_nn = [oculta, salida]
    oculta, salida, error8 = backpropagation(xor_nn,[x*2-1 for x in entradas[8]], objetivos[8])
    xor_nn = [oculta, salida]
    oculta, salida, error9 = backpropagation(xor_nn,[x*2-1 for x in entradas[8]], objetivos[8])
    xor_nn = [oculta, salida]
    promedio_errores_cuadrados = (error1+error2+error3+error4+error5+error6+error7+error8+error0+error9)/10
    i = i + 1
    if(i%100==0):
        print("Iteración:",i)
        print("Promedio errores cuadrados:", promedio_errores_cuadrados)
    if(promedio_errores_cuadrados>0.0005):
        print("Iteracion final",i)
        print("Promedio errores cuadrados:", promedio_errores_cuadrados)
        

    #Resultados
print("Los pesos de la red neuronal son los siguientes:")
print(xor_nn)
print("Al ingresar el digito 0, las similitudes ordenadas de 0-9 son las siguientes")
print(ffnn(xor_nn, [x*2-1 for x in entradas[0]])[-1])
print("Al ingresar el digito 1, las similitudes ordenadas de 0-9 son las siguientes")
print(ffnn(xor_nn, [x*2-1 for x in entradas[1]])[-1])
print("Al ingresar el digito 2, las similitudes ordenadas de 0-9 son las siguientes")
print(ffnn(xor_nn, [x*2-1 for x in entradas[2]])[-1])
print("Al ingresar el digito 3, las similitudes ordenadas de 0-9 son las siguientes")
print(ffnn(xor_nn, [x*2-1 for x in entradas[3]])[-1])
print("Al ingresar el digito 4, las similitudes ordenadas de 0-9 son las siguientes")
print(ffnn(xor_nn, [x*2-1 for x in entradas[4]])[-1])
print("Al ingresar el digito 5, las similitudes ordenadas de 0-9 son las siguientes")
print(ffnn(xor_nn, [x*2-1 for x in entradas[5]])[-1])
print("Al ingresar el digito 6, las similitudes ordenadas de 0-9 son las siguientes")
print(ffnn(xor_nn, [x*2-1 for x in entradas[6]])[-1])
print("Al ingresar el digito 7, las similitudes ordenadas de 0-9 son las siguientes")
print(ffnn(xor_nn, [x*2-1 for x in entradas[7]])[-1])
print("Al ingresar el digito 8, las similitudes ordenadas de 0-9 son las siguientes")
print(ffnn(xor_nn, [x*2-1 for x in entradas[8]])[-1])
print("Al ingresar el digito 9, las similitudes ordenadas de 0-9 son las siguientes")
print(ffnn(xor_nn, [x*2-1 for x in entradas[9]])[-1])


