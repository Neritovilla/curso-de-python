class Mascota: # clase padre
    
    def comer(selft):
        print('la mascota come')


    def dormir(selft):
        print('la mascota duerme')


class Perro(Mascota): # clase hij@
    pass


duke = Perro()
duke.comer()
duke.dormir()