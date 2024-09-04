#RETO 12 - Parte 2
#Procear el archivo y extraer: candidad de vocales y consonantes, y un listado de las 50 palabras que más se repiten

def numero_vocales_consonantes(texto : str)-> tuple:
    #Se definen las vocales y las consonantes
    vocales : str = "aeiouáéíóúü"
    consonantes : str = "bcdfghjklmnñpqrstvwxyz"
    
    #Se definene los contadores
    total_vocales : int = 0
    total_consonantes : int = 0

    #Se cuentan cada una
    for caracter in texto:
        if caracter in vocales:
            total_vocales += 1
        elif caracter in consonantes:
            total_consonantes += 1
    
    return total_vocales,total_consonantes

def palabras_repetidas(texto : str)-> list:
    #Se quitan los caracteres no deseados   
    caracteres_no_deseados : list = ['.', ',', ';', ':', '!', '?', '"', '(', ')', '[', ']', '{', '}', '-', '_', '“', '”', '\n', '\r', '\t']
    for caracter in caracteres_no_deseados:
        texto = texto.replace(caracter, ' ')

    #Se dividen las palabras
    palabras = texto.split()

    #Se cuenta la frecuencia de las palabras
    frecuencia_palabras : dict = {}
    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1

    #Se ordenan las palabras por su frecuencia
    palabras_ordenadas = sorted(frecuencia_palabras.items(), key=lambda item: item[1], reverse=True)

    #Se separan las 50 palabras más repetidas
    palabras_50 = []
    for i in range (50):
        palabras_50 += palabras_ordenadas[i]

    return palabras_50

if __name__ == "__main__":

    #Inicia el programa
    print("Programa para procesar el archivo")

    #Procesar el archivo

    #Se debe poner la dirección del archivo a procesar
    archivo = 'C:/Users/Angyp/OneDrive/Documentos/Universidad/Programación de Computadores/RETO 12/archivo.txt'  

    #Se lee el archivo
    file = open(archivo, 'r', encoding='utf-8')
    texto = file.read()

    #Se cuentas las vocales y consonantes
    num_vocales, num_consonantes= numero_vocales_consonantes(texto)
    print(f"Número de vocales: {num_vocales}")
    print(f"Número de consonantes: {num_consonantes}")

    #Se encuentran las palabras repetidas
    palabras_50 = palabras_repetidas(texto)
    print("Palabras más repetidas:")
    j : int = 1
    for _ in range(50):
        print(f"{j}. {palabras_50[j]}")
        j += 1

    file.close()


# ! /\|=\/