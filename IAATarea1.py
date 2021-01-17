import xlrd
 
documento = xlrd.open_workbook("example.xlsx")
 
datos = documento.sheet_by_index(0)
#for i in range(datos.nrows - 1):
#    for j in range(datos.ncols):
#       print("Iteracion n#")
#       print(i)
#       print("--------")

#Promedio X

X_bar = 0
n = 0 
for i in range(datos.nrows - 1):
    X_bar = X_bar + datos.cell_value(i+1,0)
    n = n + 1
X_bar = X_bar/n
#Promedio Y
Y_bar = 0
n = 0
for i in range(datos.nrows - 1):
    Y_bar = Y_bar + datos.cell_value(i+1,1)
    n = n + 1
Y_bar = Y_bar/n

T_A = 0
T_B = 0
for i in range(datos.nrows - 1):
        T_A = T_A + (datos.cell_value(i+1,0) - X_bar)*(datos.cell_value(i+1,1) - Y_bar)
        T_B = T_B + (datos.cell_value(i+1,0) - X_bar)*(datos.cell_value(i+1,0) - X_bar)
T= T_A/T_B

T2 = Y_bar - T*X_bar
print("La funcion quedaria de la siguiente forma:")
print("y = ", T2, " + ",T,"X1",sep = "")
        
#Evaluar Modelo
avr = 0
n = 0
for i in range(datos.nrows - 1):
    yr = datos.cell_value(i+1,1)
    ym = T2 + T*datos.cell_value(i+1,0)
    avr = avr + (yr - ym)
    n = n + 1
avr = avr/n
print("El error del modelo es de ", avr)
