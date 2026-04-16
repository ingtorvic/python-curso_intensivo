cars = ['bmw', 'audi', 'toyota', 'subaru']
# Ordena alfabeticamente la lista
cars.sort()
print(cars)
# Ordena alfabeticamente la lista de manera inversa
cars.sort(reverse=True)
print(cars)
print("-----------------------------------------------")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("-----------------------------------------------")
print("\nHere is the sorted list:")
print(sorted(cars))
print("-----------------------------------------------")
print("\nHere is the original list again:")
print(cars)

# Imprimir una lista en orden inverso
cars.reverse()
print(cars)
# Volver a la lista original usando nuevamente el mismo metodo
cars.reverse()
print(cars)

# Longitud de una lista
print(len(cars))