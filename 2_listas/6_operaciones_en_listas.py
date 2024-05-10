lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]

# ordenar una lista

# usando sort()
# esta funcion ordena la lista de manera ascendente(menor a mayor)
lista.sort()
print(lista)
#obtenemos la siguiente lista lista = [1, 3, 4, 5, 8, 44, 90, 132, 600]
#usando reverse ordenamos de manera descendente
lista.sort(reverse= True)
print(lista)
#obtenemos la siguiente lista lista = [600, 132, 90, 44, 8, 5, 4, 3, 1]

# obtener el numero mayor y menor de una lista 
numero_mayor = max(lista)
numero_menor = min(lista)

print('numero mayor: ' + str (numero_mayor))
print('numero menor: ' + str (numero_menor))

# verificar si un elemento existe en la lista
# usamos in
valor_buscado = 5 in lista # retorna un true  o false
print(valor_buscado)
# podemos negar la busqueda usando el not
valor_buscado = 5 not in lista 

#obtener la posicion de un elemento
#usamos index(valor)
index = lista.index(5) # retorna el primer indice encontrado en caso de existir mas registros con este valor
print(index)