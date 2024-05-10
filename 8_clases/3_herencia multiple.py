
class Mascota: # clase padre
    
    def comer(selft):
        print('la mascota come')


    def dormir(selft):
        print('la mascota duerme')


class Felino:
    
    def cazar():
        print('El felino caza')

# herencia multiple de varias clases
class Gato(Mascota, Felino): # clase hij@
    pass


pelusa = Gato()
pelusa.cazar()  # hereda de felino
pelusa.dormir() # hereda de mascota