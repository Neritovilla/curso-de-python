diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4,}

# obtener el valor de un registro del diccionario meduiante su llave
valor = diccionario['a']
print(valor)

# verificar si existe en el diccioanrio
consultar = 'a' in diccionario # devuelve un boolean
print(consultar)

#get
valor = diccionario.get('b') # devuelve none(un valor null) en caso de q no exista
print(consultar)