asignaturas = ['Informática', 'Religión', 'Artística', 'Ciencias Naturales', 'Matemáticas', 'Inglés']
print(asignaturas)
# Cambiar el valor de un elemento de la lista
asignaturas[0] = 'Tecnología e Informática'
print(asignaturas)
# Agregar un elemento al final de la lista
asignaturas.append('Castellano')
print(asignaturas)
# Insertar un elemento en una posición determinada
asignaturas.insert(-2, 'Estadística')
print(asignaturas)
# Eliminar determinado un elemento de la lista
del asignaturas[1]
print(asignaturas)
# Eliminar el último elemento de la lista
asignatura = asignaturas.pop()
print(f'La asignatura {asignatura} fue eliminada')
# Eliminar un elemento de la lista por el contenido de esta
asignatura = 'Artística'
asignaturas.remove(asignatura)
print(asignaturas)
# Ordenar la lista de manera temporal sorted()
print(sorted(asignaturas))
print(asignaturas)
# Ordenar la lista de forma permanente
asignaturas.sort()
print(asignaturas)
# Ordenar la lista de forma permanente al revés
asignaturas.sort(reverse=True)
print(asignaturas)
# Imprimir la lista en orden inverso
asignaturas.reverse()
print(asignaturas)
# Longitud de una lista
print(f'La longitud de la lista es: {len(asignaturas)}')