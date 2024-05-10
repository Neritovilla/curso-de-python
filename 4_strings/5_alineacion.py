mensaje = 'Hola mundo'

# ljust -> justificar a la izquierda
mensaje = mensaje.ljust(20) # cantidad de espacios al string (numero)
print(mensaje + ' .') 

# rjust -> justificar a la derecha
mensaje = mensaje.rjust(20) # cantidad de espacios al string (numero)
print(mensaje + ' .')

# center -> centar el texto
mensaje = mensaje.center(20)# cantidad de espacios al string (numero) 
print('. ' + mensaje + ' .')