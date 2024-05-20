## ejercicio 12

# def main():
#     n = int(input("¿Cuántos números vas a introducir? "))
#     if n <= 0:
#         print("Por favor, introduce un número entero positivo.")
#         return

#     prev_number = float(input("Introduce el primer número: "))
#     for i in range(1, n):
#         current_number = float(input(f"Introduce el número {i+1}: "))
#         if current_number <= prev_number:
#             print("El número introducido no es mayor que el anterior.")
#         prev_number = current_number

# if __name__ == "__main__":
#    main()

# Solicitar al usuario cuántos números va a introducir
cantidad_numeros = int(input("¿Cuántos números vas a introducir? "))

# Inicializar el contador de números negativos
contador_negativos = 0

# Pedir los números al usuario y contar cuántos son negativos
for i in range(cantidad_numeros):
    numero = float(input("Introduce un número: "))
    if numero < 0:
        contador_negativos += 1

# Mostrar la cantidad de números negativos introducidos por terminal
print("Ha introducido", contador_negativos, "números negativos.")

## ejrcicio 9

# Solicitar al usuario cuántos números va a introducir
# cantidad_numeros = int(input("¿Cuántos números vas a introducir? "))

# # Inicializar la variable para almacenar el número anterior
# numero_anterior = None

# # Pedir los números al usuario y verificar si son mayores que los anteriores
# for i in range(cantidad_numeros):
#     numero = float(input("Introduce un número: "))
#     if numero_anterior is not None and numero <= numero_anterior:
#         print("El número introducido no es mayor que el anterior.")
#     numero_anterior = numero

# Ejercicio Uno: 
# > Escribir un programa para una empresa que tiene salas de juegos para todas las edades
# y quiere calcular de forma automatica el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
# Si el cliente es menor de 4 puede entrar gratis, si tiene entre 4 y 18 debe pagar 5 soles, y 
# si es mayor de 18 deberá pagar 10 soles.
## Ejercicio Dos:
# > Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces
## Ejercicio Tres: 
#  > Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
# todos los números impares desde 1 hasta ese número separados por comas.
## Ejercicio Cuatro: 
# > Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10. 
## Ejercicio Cinco: 
# > Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una
# a una las letras de la palabra introducida empezando por la última.
## Ejercicio Seis: 
# > Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
# rectángulo como el de la imagen adjunta. 
# 1
# 31
# 531
# 7531
# 97531
## Ejercicio Siete:
# > Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por
# pantalla el número de veces que aparece la letra en la frase.
## Ejercicio Ocho:
# > Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las 
# letras de la palabra introducida empezando por la última.
## Ejercicio Nueve:
# > Escriba un programa que pregunte cuántos números se van a introducir, luego pida esos números, y
# muestre un mensaje cada vez que un número no sea mayor que el anterior.
## Ejercicio Diez:
# > Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla 
# el número de veces que aparece la letra en la frase.
## Ejercicio Once:
# > Escriba un programa que pregunte cuantos números se van a introducir, pida los esos números (que puedan ser decimales)
# y calcule su suma, mostrar por terminal la suma de los números introducidos.
## Ejercicio Doce:
# > Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos 
# negativos ha introducido.