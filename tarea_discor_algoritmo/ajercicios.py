# Ejercicio Uno: 
# > Escribir un programa para una empresa que tiene salas de juegos para todas las edades
# y quiere calcular de forma automatica el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
# Si el cliente es menor de 4 puede entrar gratis, si tiene entre 4 y 18 debe pagar 5 soles, y 
# si es mayor de 18 deberá pagar 10 soles.

# Solicitar la edad del cliente al usuario
edad = int(input("Ingrese la edad del cliente: "))

# Calcular el precio de la entrada según la edad
if edad < 4:
    precio = 0
elif 4 <= edad <= 18:
    precio = 5
else:
    precio = 10

# Mostrar el precio de la entrada por terminal
print("El precio de la entrada es:", precio, "soles")
 
## Ejercicio Dos:
# > Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces

# Solicitar al usuario una palabra
palabra = input("Ingresa una palabra: ")

# Mostrar la palabra 10 veces por terminal
for _ in range(10):
    print(palabra)
 
 
## Ejercicio Tres: 
#  > Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
# todos los números impares desde 1 hasta ese número separados por comas.

# Solicitar al usuario un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Mostrar los números desde 1 hasta el número dado
print("Números desde 1 hasta", numero, ":")
for i in range(1, numero + 1):
    print(i, end=" ")
 
## Ejercicio Cuatro: 
# > Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10. 

# Mostrar la tabla de multiplicar del 1 al 10
for i in range(1, 11):
    print(f"Tabla de multiplicar del {i}:")
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
    print()
 
 
## Ejercicio Cinco: 
# > Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una
# a una las letras de la palabra introducida empezando por la última.

# Solicitar al usuario una palabra
palabra = input("Ingresa una palabra: ")

# Mostrar las letras de la palabra introducida empezando por la última
for letra in reversed(palabra):
    print(letra)
 
 
## Ejercicio Seis: 
# > Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
# rectángulo como el de la imagen adjunta. 
# 1
# 31
# 531
# 7531
# 97531
 
# Solicitar al usuario un número entero
numero = int(input("Ingrese un número entero: "))

# Mostrar un triángulo rectángulo con números en el patrón dado
for i in range(1, numero + 1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()
 
## Ejercicio Siete:
# > Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por
# pantalla el número de veces que aparece la letra en la frase.

# Solicitar al usuario una frase y una letra
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

# Contar el número de veces que aparece la letra en la frase
contador = frase.count(letra)
print(f"La letra '{letra}' aparece {contador} veces en la frase.")

## Ejercicio Ocho:
# > Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las 
# letras de la palabra introducida empezando por la última.

# Solicitar al usuario una frase y una letra
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

# Contar el número de veces que aparece la letra en la frase
contador = frase.count(letra)
print(f"La letra '{letra}' aparece {contador} veces en la frase.")


## Ejercicio Nueve:
# > Escriba un programa que pregunte cuántos números se van a introducir, luego pida esos números, y
# muestre un mensaje cada vez que un número no sea mayor que el anterior.

cantidad_numeros = int(input("¿Cuántos números vas a introducir? "))

if cantidad_numeros > 0:
    numero_anterior = int(input("Introduce el primer número: "))
    for i in range(1, cantidad_numeros):
        numero_actual = int(input("Introduce el siguiente número: "))
        if numero_actual <= numero_anterior:
            print("El número introducido no es mayor que el anterior.")
        numero_anterior = numero_actual
else:
    print("No se han introducido números.")


## Ejercicio Diez:
# > Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla 
# el número de veces que aparece la letra en la frase.

# Solicitar al usuario una frase y una letra
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

# Contar el número de veces que aparece la letra en la frase
contador = frase.count(letra)
print(f"La letra '{letra}' aparece {contador} veces en la frase.")

## Ejercicio Once:
# > Escriba un programa que pregunte cuantos números se van a introducir, pida los esos números (que puedan ser decimales)
# y calcule su suma, mostrar por terminal la suma de los números introducidos.

# Solicitar al usuario cuántos números va a introducir
cantidad_numeros = int(input("¿Cuántos números vas a introducir? "))

# Inicializar la variable para almacenar la suma de los números
suma = 0

# Pedir los números al usuario y calcular la suma
for i in range(cantidad_numeros):
    numero = float(input("Introduce un número: "))
    suma += numero

# Mostrar la suma de los números introducidos por terminal
print("La suma de los números introducidos es:", suma)

## Ejercicio Doce:
# > Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos 
# negativos ha introducido.

# Pedir al usuario cuántos números se van a introducir
num_numeros = int(input("¿Cuántos números vas a introducir? "))

# Inicializar contador de números negativos
contador_negativos = 0

# Pedir los números al usuario y contar los negativos
for i in range(num_numeros):
    numero = int(input(f"Introduce el número {i+1}: "))
    if numero < 0:
        contador_negativos += 1

# Mostrar la cantidad de números negativos introducidos
print(f"Has introducido {contador_negativos} números negativos.")




