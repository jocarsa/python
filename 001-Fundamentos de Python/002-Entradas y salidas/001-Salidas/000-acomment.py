En Python, la función `print()` se utiliza para mostrar salidas en la consola. Esta función toma uno o más argumentos y los muestra en la pantalla del usuario.

Sintaxis básica de `print()`:
```python
print(valor1, valor2, valor3, ..., valorN)
```

Donde `valor1`, `valor2`, ..., `valorN` son los valores que deseas mostrar en la consola. Estos valores pueden ser cadenas de texto, números, variables, resultados de expresiones, etc. Los valores separados por comas se mostrarán en la misma línea y se separarán por un espacio por defecto.

Ejemplo:

```python
nombre = "Juan"
edad = 30
print("Hola,", nombre, "tienes", edad, "años.")
```

Este código producirá la siguiente salida en la consola:

```
Hola, Juan tienes 30 años.
```

Además de la sintaxis básica, Python ofrece varias formas para formatear la salida usando la función `print()`:

1. Usando cadenas de formato con el método `format()`:

```python
nombre = "María"
edad = 25
print("Nombre: {}, Edad: {}".format(nombre, edad))
```

2. Usando f-strings (formatted string literals) en Python 3.6+:

```python
nombre = "Carlos"
edad = 35
print(f"Nombre: {nombre}, Edad: {edad}")
```

3. Especificando el separador entre los valores mediante el argumento `sep` de la función `print()`:

```python
nombre = "Ana"
edad = 28
print("Nombre:", nombre, "Edad:", edad, sep="-")
```

Estos son solo algunos ejemplos de cómo puedes utilizar la función `print()` en Python para mostrar resultados y mensajes en la consola. La función `print()` es una herramienta valiosa para depurar, mostrar información relevante al usuario y comunicar el progreso o resultados de un programa.