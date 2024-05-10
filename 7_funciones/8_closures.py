def saludar(username):
    def mostrar_mensaje():
        print(f'hola, {username}')
    return mostrar_mensaje

username = 'Cody'
respuesta = saludar(username)

respuesta()