# es una funcion que toma de valor una funcion y retorna otra

"""
a -> función principal
b -> función a decorar
c -> función decorada

a(b) -> c
"""

def funcion_a(funcion_b):
    def funcion_c(*args, **kwargs):
        print('>>>antes del llamado')
        resultado = funcion_b(*args, **kwargs)        
        print('>>>despues del llamado')
        return resultado
    return funcion_c


@funcion_a
def suma(num_uno, num_dos):
    return num_uno + num_dos

resultado = suma(10,20)
print(resultado)