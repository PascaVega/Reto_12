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
    <td style="color:#141414" align="center">Procesar el archivo y extraer:
      <ul>
        <li>Cantidad de vocales</li>
        <li>Cantidad de consonantes</li>
        <li>Listado de las 50 palabras que más se repiten</li>
      </ul>
    </td>
  </tr>
  
