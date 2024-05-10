lista = [1, 2, 3, 4, 5]
tupla = (10, 20, 30,40 ,50)
#comprimimos los valores de la lista y la tupla, esto los une y nos devuevle un zip
resultado = zip(lista, tupla)

#convertimos el zip en tuplas
resultado = tuple(resultado)
print(resultado)

#convertimos el zip en listas
resultado = list(resultado)
print(resultado)