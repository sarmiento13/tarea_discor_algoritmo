
# Aquí te dejo un resumen de Python junto con 5 ejercicios simples para practicar:
 
# Resumen de Python:
 
# Python es un lenguaje de programación de alto nivel conocido por su sintaxis clara y legible. Algunas
# características importantes de Python incluyen:
 
# - Tipado dinámico: No es necesario declarar el tipo de variable.
# - Indentación: Utiliza la indentación para definir bloques de código.
# - Amplia biblioteca estándar: Proporciona módulos y funciones integradas para diversas tareas.
 
# Ejercicios de Python:
 
# 1. Saludo personalizado: Escribe un programa que solicite al usuario su nombre y luego imprima un saludo personalizado.
# 2. Suma de dos números: Crea un programa que pida al usuario dos números y muestre la suma de ambos.
# 3. Tabla de multiplicar: Diseña un programa que muestre la tabla de multiplicar de un número ingresado por el usuario.
# 4. Cálculo del área de un círculo: Solicita al usuario el radio de un círculo y calcula su área (fórmula: π * radio^2).
# 5. Contador de vocales: Desarrolla un programa que cuente el número de vocales en una frase ingresada por el usuario.
 
# Estos ejercicios son simples y pueden ayudarte a practicar los conceptos básicos de Python, como entrada de usuario,
# operaciones matemáticas, 
# bucles y condicionales. ¡Espero que te resulten útiles para consolidar tus conocimientos en Python!
def contar_comas(texto):
    contador = 0
    indices = []

    for indice, caracter in enumerate(texto):
        if caracter == ',':
            contador += 1
            indices.append(indice)

    return contador, indices

texto = "Hola, cómo estás, espero que bien."

cantidad_comas, indices_comas = contar_comas(texto)

print("La cantidad de comas en el texto es:", cantidad_comas)
print("Los índices de las comas en el texto son:", indices_comas)
