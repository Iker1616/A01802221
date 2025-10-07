#ejercicio 1
temperaturas = [22,24,19,25,23,21,26]
promedio = sum(temperaturas)/len(temperaturas)
for temp in temperaturas:
    if temp > promedio: print(temp, "arriba")
    elif temp < promedio: print(temp, "abajo")
    else: print(temp, "igual")

#ejercicio 2
alumnos = ["Reymundo","Iker","Giovani","Santiago"]
calificaciones = [50,60,40,28]

reprobados = [alumnos[i] for i in range(len(calificaciones)) if calificaciones[i]<70]
print("Alumnos reprobados:", reprobados)

#ejercicio 3
articulos = ["Leche","Pan","Huevos","Manzanas","Arroz"]
comprado = [True,False,False,True,False]
for i in range(len(articulos)):
    if not comprado[i]:
        r = input("¿Ya compraste "+articulos[i]+"? (s/n): ")
        if r.lower()=="s": comprado[i]=True
for i in range(len(articulos)):
    print(articulos[i], "Comprado" if comprado[i] else "Pendiente")

#ejercicio 4
numeros = [45,12,89,33,7,56,21]

numero_maximo = max(numeros)
numero_minimo = min(numeros)
numeros_ordenados = sorted(numeros)

print("Máximo:", numero_maximo)
print("Mínimo:", numero_minimo)
print("Ordenados:", numeros_ordenados)

#ejercicio 5
numeros = [10,15,22,33,40,7,9,18]

numeros_pares = [num for num in numeros if num % 2 == 0]
numeros_impares = [num for num in numeros if num % 2 != 0]

print("Pares:", numeros_pares)
print("Impares:", numeros_impares)

#ejercicio 6
usuarios = ["Juan","Ana","Pedro","Lucía","Carlos"]
while True:
    nuevo_usuario = input("Nuevo usuario: ")
    if nuevo_usuario not in usuarios:
        usuarios += [nuevo_usuario]
        break
    print("Ese nombre ya existe")
print("Usuarios:", usuarios)

