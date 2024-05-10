nombre = 'Erick'
apellido = 'Villavicencio'

# concatenar 2 variables string usamos el +
nombre_completo = 'Mr. ' + nombre + ' ' +  apellido + '.'
print(nombre_completo)

# usando %s
nombre_completo = 'Mr. %s %s.' %(nombre, apellido)
print(nombre_completo)

# usando el metodo format
nombre_completo = 'Mr. {} {}.'.format(nombre,apellido)
print(nombre_completo)

# o usando parametros con metodo format 
nombre_completo = 'Mr. {nombre} {apellido}.'.format(
    nombre = nombre,
    apellido = apellido
    )
print(nombre_completo)

# f string
nombre_completo = f'Mr. {nombre} {apellido}.'
print(nombre_completo)