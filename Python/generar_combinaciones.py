import itertools

def generar_combinaciones():
    digitos = '0123456789'
    longitud = 8
    combinaciones = [''.join(p) for p in itertools.product(digitos, repeat=longitud)]
    return combinaciones

def guardar_combinaciones_en_archivo(combinaciones, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for combinacion in combinaciones:
            archivo.write(combinacion + '\n')

if __name__ == "__main__":
    combinaciones = generar_combinaciones()
    nombre_archivo = "digitos.txt"
    guardar_combinaciones_en_archivo(combinaciones, nombre_archivo)
    print(f"Se generaron todas las combinaciones y se guardaron en el archivo {nombre_archivo}.")
