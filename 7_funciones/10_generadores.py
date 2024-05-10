# 

def pares(): # una iteracion peresoza 
    for numero in range(0, 100, 2):
        yield numero # pausa la ejecucion y la reanuda, asi podemos retornar valores 


generador = pares()

while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print('El generador finalizo')
        break