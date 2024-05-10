# una clase hija puede modificar el comportamiento d euna clase padre

class Animal():

    def comer(self):
        print('el animal come')


    def dormir(self):
        print('el animal duerme')


class Mascota(Animal): # clase padre    
    def comer(self):# sobrecargamos el metodo comer
        print('la mascota come')

class Felino:
    
    def cazar():
        print('El felino caza')

# herencia multiple de varias clases
class Gato(Mascota, Felino): # clase hij@
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):# sobrecargamos el metodo 
        print(f'{self.nombre} come.')
            
    def dormir(self):# sobrecargamos el metodo 
        print(f'{self.nombre} duerme.')




pelusa = Gato('Pelusa')
pelusa.comer()
pelusa.dormir()