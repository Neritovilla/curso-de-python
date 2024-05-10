animal = 'leon' # variable global

def imprimir_animal():
    animal = 'ballena' # variable local 
    print (animal)

imprimir_animal()

 #para usar el mismo scope
def imprimir_animal_dos():
    global animal
    animal = 'ballena' # variable local 
    print (animal)