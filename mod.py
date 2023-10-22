nombre_archivo = "rockyou-mod.dic"

try:
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        numero_de_lineas = len(lineas)
        print(f"El archivo '{nombre_archivo}' tiene {numero_de_lineas} líneas.")
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no se encuentra.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
