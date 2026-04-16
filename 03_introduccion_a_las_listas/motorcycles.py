motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Añadir un elemento a la lista
motorcycles.append('honda')
print(motorcycles)

# Insertar elementos en una lista
motorcycles.insert(0, 'akt')
print(motorcycles)

# Eliminar un elemento con la sentencia del
del motorcycles[0]
print(motorcycles)

# Eliminar un elemento con el método pop()
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Sacar elementos de cualquier posición de una lista
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")

# Eliminar un elemento por valor
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)

too_expensive = 'honda'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")