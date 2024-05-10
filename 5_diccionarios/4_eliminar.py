diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4,}

# eliminar elementos de un diccionario usando del
del diccionario['a']
print(diccionario)

# eliminar haciendo uso de pop()
valor = diccionario.pop('b')
print(diccionario)
print(valor)

#eliminar todos los elementos del diccionario
diccionario.clear()
print(diccionario)