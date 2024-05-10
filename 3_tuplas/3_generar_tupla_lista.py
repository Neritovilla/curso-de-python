

# Generar una tupla en base a una lista
lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'java']
# Usamos la funcion tuple para convertir una lista en tupla
cursos_tupla = tuple(lista_cursos)
print(cursos_tupla)
print(type(cursos_tupla))



# Generar  una lista en base a una tupla
niveles = ('Básico', 'Intermedio', 'Avanzado')
# Usamos list()
niveles_lista = list(niveles)
print(niveles_lista)
print(type(niveles_lista))