#CREAR LISTA EN BASE A UN STRING    
lenguajes = 'Python Ruby Java Rust C++ C'
listado_lenguajes = lenguajes.split() # por defecto toma el espacio en blanco para generar la divicion
print(listado_lenguajes)


# crear string en bse a una lista
lenguajes =['Python', 'Ruby', 'Java', 'Rust', 'C++', 'C']
# usamos  'caracter de union'.join(lista)  
cadena = ' '.join(lenguajes)
print(cadena)