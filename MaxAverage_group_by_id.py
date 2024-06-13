def main():
    data = [[912, 410], [404, 410], [912, 410], [810, 410], [810, 410], [810, 410]]
    sumas = {}
    for dato in data:
        if dato[0] in sumas:
            sumas[dato[0]] = [sumas[dato[0]][0] + dato[1], sumas[dato[0]][1] + 1]
        else:
            sumas[dato[0]] = [dato[1], 1]
    promedios = {}
    for key in sumas:
        promedios[key] = [round(sumas[key][0]/sumas[key][1], 2), sumas[key][1]];
    result = (sorted(sorted(promedios.items(), key=lambda item: item[0]), key=lambda item: item[1], reverse=True))
    return result[0]
result = main()
print(f"El ID con el Promedio mas alto es {result[0]} con Promedio de {result[1][0]}")