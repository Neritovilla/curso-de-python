#solicitamos un  valor
valor_entrada = input('ingrese su edad: ')
valor_entrada_dos = input('ingrese tu altura: ')
valor_entrada_tres = input('autorizas el programa? (si/no) ')

#convertimos en string en int haciendo uso de la funcion int()
edad = int(valor_entrada)

#convertimos en string en float haciendo uso de la funcion float()
altura = float(valor_entrada_dos)

#convertimos el valor a boolean haciendo uso del operador lógico
autorizacion = valor_entrada_tres == 'si'