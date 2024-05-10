numeros = (1, 2, 3, 4, 5, 6, 7, 8)
# asignamos los valores de la tupla a las variables
# estos valores se asignan en vale al orden de las variables y el orden de los items de la lista
# de no ser asi los guardamos en resto valores
# si queremos otimir resto valores usamos  *_ esto omite el resto de valores 
uno, dos, tres, *resto_valores = numeros

print(uno)
print(dos)
print(tres)
print(resto_valores)

