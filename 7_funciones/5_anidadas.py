def operacion():

    def deposito(cantidad, balance):
        return cantidad + balance


    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            return None

    print (deposito(10,20), retiro(50,80))

operacion()