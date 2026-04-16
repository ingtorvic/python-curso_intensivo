invitados = ['José', 'Mario', 'Euclides', 'Rosa Marina']
print(f'Hola {invitados[0].title()} te invito a cenar')
print(f'Hola {invitados[1].title()} te invito a cenar')
print(f'Hola {invitados[2].title()} te invito a cenar')
print(f'Hola {invitados[-1].title()} te invito a cenar')
print("-----------------------------------------------")
print(f"{invitados[1].title()} no puede asistir")
print("-----------------------------------------------")
invitados[1] = 'Regina'
print(f'Hola {invitados[0].title()} te invito a cenar')
print(f'Hola {invitados[1].title()} te invito a cenar')
print(f'Hola {invitados[2].title()} te invito a cenar')
print(f'Hola {invitados[-1].title()} te invito a cenar')
