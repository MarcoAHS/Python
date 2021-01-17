#Anova
n=3 #Columnas (Bloques)
k=4 #Filas (Tratamientos)
Mat=[[3.4,2.6,2.8], #Los valores donde cada fila esun tratamiento
     [3,2.7,3.1],
     [3.3,3,3.4],
     [3.5,3.1,3.7]
     ]
FTB = [8.94,19.3] #Los valores de la tabla F con un alpha de 0.05 de tratamientos y bloques respectivamente
FTU1 = 8.85 #Valor de la tabla F con alpha 0.05, con error 8 y grados de libertad de 3
FTU2 = 19.38 #Valor de la tabla F con alpha 0.05, con error 9 y grados de libertad de 2
GL1F = [k-1,k*(n-1),k*n-1]
GL1C = [n-1,n*(k-1),n*k-1]
GL2 = [k-1,n-1,(k-1)*(n-1),(k-1)+(n-1)+((k-1)*(n-1))] #La columna GL de la tabla ANOVA de dos direcciones
#Suma de todos los datos
SumaTotal = 0
for i in range(k):
    for j in range(n):
        SumaTotal = SumaTotal + Mat[i][j]
#Suma por tratamiento
SumaTrat = [0,0,0,0]
for i in range(k):
    for j in range(n):
        SumaTrat[i] = SumaTrat[i] + Mat[i][j]
#Suma por bloque
SumaBloq = [0,0,0]
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
      
SSB = [SS1,SS2,SS3,SS4]#La columna SS de la tabla ANOVA (Bidireccional)
MSB = [SS1/GL2[0],SS2/GL2[1],SS3/GL2[2]]#La columna MS de la tabla ANOVA (Bidireccional)
FB = [MSB[0]/MSB[2],MSB[1]/MSB[2]]#La columna F de la tabla ANOVA (Bidireccional)

AnovaB= [[GL2[0],SSB[0],MSB[0],FB[0]],
         [GL2[1],SSB[1],MSB[1],FB[1]],
         [GL2[2],SSB[2],MSB[2],"-----------"],
         [GL2[3],SSB[3],"-----------------" , "----------"]] #Tabla Anova (Bidireccional)

aux = SS4 - SS1
SSU1 = [SS1,aux,SS4] #Columna SS de una direccion para filas (Tratamientos)
MSU1 = [SS1/GL1F[0],aux/GL1F[1]]
FU1 = MSU1[0]/MSU1[1]

AnovaUF = [[GL1F[0],SSU1[0],MSU1[0],FU1],
         [GL1F[1],SSU1[1],MSU1[1],"---------"],
         [GL1F[2],SSU1[2],"----------------" , "-----------"]] #Tabla Anova (Unidireccional con Filas)

aux = SS4 - SS2
SSU2 = [SS2,aux,SS4] #Columna SS de una direccion para columnas (Bloques)
MSU2 = [SS2/GL1C[0],aux/GL1C[1]]
FU2 = MSU2[0]/MSU2[1]

AnovaUC = [[GL1C[0],SSU2[0],MSU2[0],FU2],
         [GL1C[1],SSU2[1],MSU2[1],"--------------"],
         [GL1C[2],SSU2[2],"---------------" , "-------------"]] #Tabla Anova (Unidireccional con Columnas)
print("Tabla Anova Bidireccional")
print("GL-------SS--------------------MS-----------------F-------")
print(AnovaB[0])
print(AnovaB[1])
print(AnovaB[2])
print(AnovaB[3])
print("")
print("Tabla Anova Unidireccional por Fila")
print("GL-------SS--------------------MS-----------------F--------")
print(AnovaUF[0])
print(AnovaUF[1])
print(AnovaUF[2])
print("")
print("Tabla Anova Unidireccional por Columna")
print("GL-------SS--------------------MS-----------------F--------")
print(AnovaUC[0])
print(AnovaUC[1])
print(AnovaUC[2])
print("")

print("Analsis Bidireccional:")
print("El valor sacado de la tabla en la Anova bidireccional para Tratamientos es: ",FTB[0])
if FB[0] > FTB[0]:
    print("[1]Se rechaza la hipotesis nula de los tratamientos en el analisis bidireccional, por lo tanto hay diferencia entre los tratamientos")
else:
    print("[1]No se rechaza la hipotesis nula de los tratamientos en el analisis bidireccional, por lo tanto no hay diferencias entre los tratamientos")
print("El valor sacado de la tabla en la Anova bidireccional para Bloques es: ",FTB[1])
if FB[1] > FTB[1]:
    print("[2]Se rechaza la hipotesis nula de los bloques en el analisis bidireccional, por lo tanto hay diferencia entre los bloques")
else:
    print("[2]No se rechaza la hipotesis nula de los bloques en el analisis bidireccional, por lo tanto no hay diferencias entre los bloques")
print("Analisis Unidireccional")
print("El valor sacado de la tabla Anova Unidireccional por filas es: ",FTU1)
if FU1 > FTU1:
    print("[3]Se rechaza la hipotesis nula de las filas (tratamientos), entonces existe una diferencia entre ellas")
else:
    print("[3]No se rechaza la hipotesis nula de las filas (tratamientos), entonces no existe una diferencia entre ellas")
print("El valor sacado de la tabla Anova Unidireccional por columnas es: ",FTU2)
if FU1 > FTU1:
    print("[4]Se rechaza la hipotesis nula de las columnas (bloques), entonces existe una diferencia entre ellas")
else:
    print("[4]No se rechaza la hipotesis nula de las columnas (bloques), entonces no existe una diferencia entre ellas")

from scipy.stats import f

val = f.pdf(0.05,3,6)
print(val)




