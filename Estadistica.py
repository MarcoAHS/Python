#Anova
n=3 #Columnas (Bloques)
k=4 #Filas (Tratamientos)
Mat=[[3.4,2.6,2.8], #Los valores donde cada fila esun tratamiento
     [3,2.7,3.1],
     [3.3,3,3.4],
     [3.5,3.1,3.7]
     ]
F_v=[8.94,19.3] #Los valores de la tabla F con un alpha de 0.05 de tratamientos y bloques respectivamente
GL = [k-1,n-1,(k-1)*(n-1),(k-1)+(n-1)+((k-1)*(n-1))] #La columna GL de la tabla ANOVA
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
      
SS = [SS1,SS2,SS3,SS4]#La columna SS de la tabla ANOVA
MS = [SS1/GL[0],SS2/GL[1],SS3/GL[2]]#La columna MS de la tabla ANOVA
F = [MS[0]/MS[2],MS[1]/MS[2]]#La columna F de la tabla ANOVA

print("El valor F de los tratamientos es:")
print(F[0])
print("El valor F de los bloques es:")
print(F[1])

if F[0] > F_v[0]:
    print("[1]La hipotesis nula de los tratamientos se rechaza, entonces hay una diferencia considerable entre los tratamientos")
else:
        print("[1]La hipotesis nula no se puede rechazar para los tratamientos, entonces no existe diferencia notable en ellos")
if F[1] > F_v[1]:
    print("[2]La hipotesis nula de los bloques se rechaza, entonces hay una diferencia considerable entre los bloques")
else:
        print("[2]La hipotesis nula no se puede rechazar para los bloques, entonces no existe diferencia notable en ellos")
        
    
        
    

    



