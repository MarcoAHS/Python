# ANOVA

# modo lectura del txt con los datos
fileHandle = open('datos.txt', 'r')

# lista de lineas de nuestro txt
listaLineas = fileHandle.readlines()

# Dimensiones del array
# n = Columnas(Bloques) y k = Filas (Tratamientos)
n, k = (int(val) for val in listaLineas[0].split())

# Txt a array
Mat = [[float(val) for val in line.split()] for line in listaLineas[1:]]

# Los valores de la tabla F con un alpha de 0.05 de tratamientos y bloques respectivamente
F_v = [8.94, 19.3]
GL1F = [k-1, k*(n-1), k*n-1]
GL1C = [n-1, n*(k-1), n*k-1]
# La columna GL de la tabla ANOVA de dos direcciones
GL2 = [k-1, n-1, (k-1)*(n-1), (k-1)+(n-1)+((k-1)*(n-1))]
# Suma de todos los datos
SumaTotal = 0
for i in range(k):
    for j in range(n):
        SumaTotal = SumaTotal + Mat[i][j]
# Suma por tratamiento
SumaTrat = [0, 0, 0, 0]
for i in range(k):
    for j in range(n):
        SumaTrat[i] = SumaTrat[i] + Mat[i][j]
# Suma por bloque
SumaBloq = [0, 0, 0]
for j in range(n):
    for i in range(k):
        SumaBloq[j] = SumaBloq[j] + Mat[i][j]


def SumaCuadrados(Vector):
    aux = 0
    for i in Vector:
        aux = aux + i*i
    return aux


def SumaCuadrMatriz(Mat):
    aux = 0
    for i in range(k):
        for j in range(n):
            aux = aux + Mat[i][j]*Mat[i][j]
    return aux


SS1 = SumaCuadrados(SumaTrat)/n - (SumaTotal)*(SumaTotal)/(k*n)
SS2 = SumaCuadrados(SumaBloq)/k - (SumaTotal)*(SumaTotal)/(k*n)
SS4 = SumaCuadrMatriz(Mat) - (SumaTotal)*(SumaTotal)/(k*n)
SS3 = SS4 - SS2 - SS1

SSB = [SS1, SS2, SS3, SS4]  # La columna SS de la tabla ANOVA (Bidireccional)
# La columna MS de la tabla ANOVA (Bidireccional)
MSB = [SS1/GL2[0], SS2/GL2[1], SS3/GL2[2]]
# La columna F de la tabla ANOVA (Bidireccional)
FB = [MSB[0]/MSB[2], MSB[1]/MSB[2]]

AnovaB = [[GL2[0], SSB[0], MSB[0], FB[0]],
          [GL2[1], SSB[1], MSB[1], FB[1]],
          [GL2[2], SSB[2], MSB[2], "---"],
          [GL2[3], SSB[3], "---", "---"]]  # Tabla Anova (Bidireccional)

aux = SS4 - SS1
SSU1 = [SS1, aux, SS4]  # Columna SS de una direccion para filas (Tratamientos)
MSU1 = [SS1/GL1F[0], aux/GL1F[1]]
FU1 = MSU1[0]/MSU1[1]

AnovaUF = [[GL1F[0], SSU1[0], MSU1[0], FU1],
           [GL1F[1], SSU1[1], MSU1[1], "---"],
           [GL1F[2], SSU1[2], "---", "---"]]  # Tabla Anova (Unidireccional con Filas)

aux = SS4 - SS2
SSU2 = [SS2, aux, SS4]  # Columna SS de una direccion para columnas (Bloques)
MSU2 = [SS2/GL1C[0], aux/GL1C[1]]
FU2 = MSU2[0]/MSU2[1]

AnovaUC = [[GL1C[0], SSU2[0], MSU2[0], FU2],
           [GL1C[1], SSU2[1], MSU2[1], "---"],
           [GL1C[2], SSU2[2], "---", "---"]]  # Tabla Anova (Unidireccional con Columnas)
