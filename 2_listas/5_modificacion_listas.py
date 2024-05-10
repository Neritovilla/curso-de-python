
lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java']

# Agregar elementos nuevos a la lista usando -> append(), agrega elementos alfinal de la lista
lista_cursos.append('MongoDB')
lista_cursos.append('C#')
print(lista_cursos)

# Conocer la longuitud de la lista usamos -> len()
print(len(lista_cursos))

# Agregar un elemento a partir de una pocicion en concreto usamos -> insert()
# la estructura de insert() es la sioguiente insert(indice, valor)
lista_cursos.insert(1, 'Rails')
print(lista_cursos)

# Agregar elementos de una lista a otra
lista_cursos_dos = ['Angular', 'React']
# usamos extend()
lista_cursos.extend(lista_cursos_dos)
print(lista_cursos)

# eliminar registro de la lista usando un valor
# usamos -> remove(valor)
lista_cursos.remove('MongoDB')
print(lista_cursos)

# eliminar registro de la lista usando un indice
# usamos -> del lista[indice]
del lista_cursos[0]
print(lista_cursos)

# eliminar todos los registro de la lista
# usamos -> clear()
lista_cursos.clear()
print(lista_cursos)