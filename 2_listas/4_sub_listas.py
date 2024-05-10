#                  0          1        2       3        4
#                 -5         -4       -3      -2       -1
lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java']

#creamos una sublista usando un indice de inicio y uno final para llenar la nueva lista  [inicio : final]

sub_lista = lista_cursos[0:2]

print(sub_lista)
# nuestra lista se veria d ela siguiente manera:
# sub_lista = ['Python', 'Django']

# ------------------------------------------------------------------------------------------------------------------------#
#obtener todos los registros de la lista desde un indice inicial  [inicio:]

sub_lista_dos = lista_cursos[2:] # al solo colocar  2: estoy diciendo que quiero todos los regiustros desde el indice 2 

print(sub_lista_dos)

# mi lista se veria de la siguiente forma:
# sub_lista_dos = ['Flask', 'Ruby', 'Java']

# ------------------------------------------------------------------------------------------------------------------------#

# obtener los primeros registros de una lista hasta un indice en concreto [:final]

sub_lista_tres = lista_cursos[:3] # enn este caso quiero obtener los primeros 3 registros de la lista

print(sub_lista_tres)

# mi lista se veria de la siguiente forma:
# sub_lista_dos = ['Python', 'Django', 'Flask']

# ------------------------------------------------------------------------------------------------------------------------#

# obtener una lista con saltos, ejemplo quiero todos los registros pero ocn un salto de 2 registros entre cada uno
# hago uso de [inicio:fin:salto]

sub_lista_cuatro = lista_cursos[0:4:2]
print(sub_lista_cuatro)

# mi lista se veria de la siguiente forma:
# sub_lista_dos = ['Python', 'Flask']

# ------------------------------------------------------------------------------------------------------------------------#

# invertir el orden de la lista
sub_lista_cuatro = lista_cursos[::-1]
print(sub_lista_cuatro)

# mi lista se veria de la siguiente forma:
# sub_lista_dos = ['Java', 'Ruby', 'Flask', 'Django', 'Python']