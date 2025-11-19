#Cree una lista vacía  denominada aprendices y edades, llénelas solicitando los datos por teclado.
#Imprima las listas
#Muestre el aprendiz con la mayor edad
#Inserte el nombre de la instructora en la posición 1
#Cuente cuantos aprendices tienen 18 años
#Agregue un aprendiz “x” al final de la lista
#Borre el nombre de la instructora de la lista
#Indique un dato a buscar en la lista de aprendices
#Muestre los primeros 10 aprendices de la lista
#Muestre los 10 últimos aprendices de la lista
#Muestre del elemento 10 al elemento 20
#Muestre los elementos de la lista, cuyo índice sea par

# Crear listas vacías
aprendices = []
edades = []

# Llenar listas solicitando los datos por teclado
cantidad = int(input("cuantos aprendices desea ingresar? "))

for i in range(cantidad):
    nombre = input(f"ingrese el nombre del aprendiz: ")
    edad = int(input(f"ingrese la edad de: "))
    aprendices.append(nombre)
    edades.append(edad)

# Imprimir las listas
print(f"lista de aprendices:  {aprendices}")
print(f"lista de edades:  {edades}")

# Mostrar el aprendiz con la mayor edad
mayor_edad = max(edades)
posicion = edades.index(mayor_edad)
print(f"el aprendiz con mayor edad es {aprendices[posicion]} con {mayor_edad} años")

# Insertar el nombre de la instructora en la posicion 1
instructora = input("ingrese nombre de la instructora: ")
aprendices.insert(1, instructora)
print(f"lista con la instructora en la posicion 1: {aprendices}")

# Contar cuántos aprendices tienen 18 años
cantidad_18 = edades.count(18)
print(f"cantidad de aprendices con 18 años: {cantidad_18}")

# Agregar un aprendiz 'x' al final de la lista
aprendices.append("x")
print(f"lista con aprendiz 'x' agregado al final: {aprendices}")

# Borrar el nombre de la instructora de la lista
aprendices.remove(instructora)
print(f"lista sin la instructora: {aprendices}")

# Buscar un dato en la lista de aprendices
buscar = input("ingrese un nombre para buscar en la lista: ")
if buscar in aprendices:
    print(f"{buscar} si se encuentra en la lista")
else:
    print(f"{buscar} no se encuentra en la lista")

# Mostrar los primeros 10 aprendices
print(f"los primeros 10 aprendices: {aprendices[:10]}")

# Mostrar los ultimos 10 aprendices
print(f"los ultimos 10 aprendices: {aprendices[-10:]}")

# Mostrar del elemento 10 al 20
print(f"elementos de la posición 10 a la 20: {aprendices[10:21]}")

#  Mostrar los elementos con indice par
print("elementos con indice par: ")
aprendices = []
for i in range(10):
    if i % 2 == 0:
        aprendices.append(i)
print(aprendices)




