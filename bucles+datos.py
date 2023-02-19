# Bucles+Datos
# Ejercicio1 
'''asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

for asignatura in asignaturas:
    nota = float(input("Introduce tu nota en " + asignatura + ": "))
    notas.append(nota)

for i, asignatura in enumerate(asignaturas):
    print("En " + asignatura + " has sacado " + str(notas[i]))'''

#Ejercicio2

'''numeros_ganadores = []

print("Introduce los números ganadores de la lotería primitiva:")
for i in range(6):
    numero = int(input("Introduce el número %d: " % (i+1)))
    numeros_ganadores.append(numero)

numeros_ganadores.sort()

print("Los números ganadores ordenados de menor a mayor son:")
print(numeros_ganadores)'''

# Ejercicio3

'''asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

for asignatura in asignaturas:
    nota = float(input(f"Introduce tu nota en {asignatura}: "))
    notas.append(nota)

asignaturas_aprobadas = [asignaturas[i] for i in range(len(asignaturas)) if notas[i] >= 5]

for asignatura_aprobada in asignaturas_aprobadas:
    asignaturas.remove(asignatura_aprobada)

if asignaturas:
    print("Tienes que repetir las siguientes asignaturas:")
    for asignatura in asignaturas:
        print(asignatura)
else:
    print("¡Has aprobado todas las asignaturas!")'''

#Ejercicio4

'''palabra = input("Introduce una palabra: ")

es_palindromo = True
longitud = len(palabra)

for i in range(longitud // 2):
    if palabra[i] != palabra[longitud - i - 1]:
        es_palindromo = False
        break

if es_palindromo:
    print(f"{palabra} es un palíndromo")
else:
    print(f"{palabra} no es un palíndromo")'''

#Ejercicio5

'''palabra = input("Introduce una palabra: ")
vocales = "aeiou"

contadores = {vocal: 0 for vocal in vocales}

for letra in palabra:
    if letra in vocales:
        contadores[letra] += 1

for vocal, contador in contadores.items():
    if contador:
        print(f"La vocal '{vocal}' aparece {contador} veces en la palabra")'''


#Ejercicio6

'''palabra = input("Introduce una palabra: ")
vocales = "aeiouáéíóú"

contadores = {vocal: 0 for vocal in vocales}

for letra in palabra:
    if letra in vocales:
        contadores[letra] += 1

for vocal, contador in contadores.items():
    if contador:
        print(f"La vocal '{vocal}' aparece {contador} veces en la palabra")'''


#Ejercicio7

facturas_pendientes = {}
cobrado = 0

while True:
    accion = input("¿Qué acción desea realizar? (Añadir/Pagar/Terminar): ")

    if accion.lower() == "terminar":
        break
    elif accion.lower() == "añadir":
        numero_factura = input("Número de factura: ")
        coste = int(input("Coste de la factura: "))
        facturas_pendientes[numero_factura] = coste
    elif accion.lower() == "pagar":
        numero_factura = input("Número de factura: ")
        if numero_factura in facturas_pendientes:
            cobrado += facturas_pendientes[numero_factura]
            del facturas_pendientes[numero_factura]
        else:
            print("La factura no existe.")

    print("Cantidad cobrada: ", cobrado)
    print("Cantidad pendiente de cobro: ", sum(facturas_pendientes.values()))











