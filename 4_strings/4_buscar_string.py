titulo_curso = 'Curso de Python'

# buscar un string dentro de otro usando count
contador = titulo_curso.count('Python')# este metodo devuelve el nuemro de coincidencias
print(contador)

# usando in()
buscador = 'Python' in titulo_curso # nos devuelve un valor boolean, toma en cuenta mayuscula y miniscula
print(buscador)

# usando startwith
# busca en el inicio del string
buscador = titulo_curso.startswith('Python') # devuelve un boolean

# usando endtwith
# busca en el final del string
buscador = titulo_curso.endswith('Python') # devuelve un boolean