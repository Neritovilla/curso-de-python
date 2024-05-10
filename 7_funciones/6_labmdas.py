# llamar una funcion mediante una variable

def centigrados_a_farhenheit(grados):
    return grados * 1.8 + 32

mi_funcion = centigrados_a_farhenheit
print(mi_funcion(10))


# labmda
#                lambda <parametos> : <cuerpo de funcion>
funcion_grados = lambda grados : grados * 1.8 + 32
print(funcion_grados(10))
