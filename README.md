# Reto 12
| Nombre                 | Identificación | Grupo | Trabajo          |
|------------------------|----------------|-------|------------------|
| Angélica Pascagaza Vega| 1031652163     |   5   | Trabajo individual |

## Solución del reto
<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 12 - Parte 1</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Consulte que hacen los siguientes métodos de strings en python: endswith, startswith, isalpha, isalnum, isdigit, isspace, istitle, islower, isupper.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center"><b>Los métodos de cadenas (strings)</b> son funciones integradas que se puden usar para realizar diversas operaciones en objetos de cadena.</td>
  </tr>
</table>

### Endswith
Este método verifica si una cadena termina con un sufijo especificado.

**Sintaxis**
```python
str.endswith(suffix[, start[, end]])
```

**Ejemplo**
```python
texto = "Hola mundo"
print(texto.endswith("mundo"))  # True
```

### Startswith
Este método verifica si una cadena comienza con un prefijo especificado.

**Sintaxis**
```python
str.startswith(prefix[, start[, end]])
```

**Ejemplo**
```python
texto = "Hola mundo"
print(texto.startswith("Hola"))  # True
```

### Isalpha
Este método devuelve True si todos los caracteres de la cadena son letras y hay al menos un carácter.

**Sintaxis**
```python
str.isalpha()
```

**Ejemplo**
```python
texto = "Hola"
print(texto.isalpha())  # True
```

### Isalnum
Este método devuelve True si todos los caracteres de la cadena son alfanuméricos (letras y números) y hay al menos un carácter.

**Sintaxis**
```python
str.isalnum()
```

**Ejemplo**
```python
texto = "Hola123"
print(texto.isalnum())  # True
```

### Isdigit
Este método devuelve True si todos los caracteres de la cadena son dígitos y hay al menos un carácter.

**Sintaxis**
```python
str.isdigit()
```

**Ejemplo**
```python
texto = "12345"
print(texto.isdigit())  # True
```

### Isspace
Este método devuelve True si todos los caracteres de la cadena son espacios en blanco y hay al menos un carácter.

**Sintaxis**
```python
str.isspace()
```

**Ejemplo**
```python
texto = "   "
print(texto.isspace())  # True
```

### Istitle
Este método devuelve True si la cadena sigue las reglas de un título (cada palabra empieza con una letra mayúscula y el resto de las letras son minúsculas).

**Sintaxis**
```python
str.istitle()
```

**Ejemplo**
```python
texto = "Hola Mundo"
print(texto.istitle())  # True
```

### Islower
Este método devuelve True si todos los caracteres de la cadena son letras minúsculas y hay al menos un carácter.

**Sintaxis**
```python
str.islower()
```

**Ejemplo**
```python
texto = "hola mundo"
print(texto.islower())  # True
```

### Isupper
Este método devuelve True si todos los caracteres de la cadena son letras mayúsculas y hay al menos un carácter.

**Sintaxis**
```python
str.isupper()
```

**Ejemplo**
```python
texto = "HOLA MUNDO"
print(texto.isupper())  # True
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 12 - Parte 2</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Procesar el <a href="https://github.com/PascaVega/Reto_12/blob/main/archivo.txt">archivo</a> y extraer:
      <ul>
        <li>Cantidad de vocales</li>
        <li>Cantidad de consonantes</li>
        <li>Listado de las 50 palabras que más se repiten</li>
      </ul>
    </td>
  </tr>
</table>

**Desarrollo del ejercicio**
```python
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
```
