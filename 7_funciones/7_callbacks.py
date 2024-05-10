promedio = lambda *args : sum(args) / len(args)
print(promedio(10,10,8,1,7))  

aprobatorio = lambda calificacion : calificacion >= 7
print(aprobatorio(8))

# ----------------------------------------------------------  #
def mostrar_mensaje(func_promedio, func_aprobatorio, *args):
    promedio = func_promedio(*args)
    if func_aprobatorio(promedio):
        print(f'aprobaste con: {promedio}')
    else:
        print('no aprobaste')

mostrar_mensaje(promedio, aprobatorio, 10,10,7,8)