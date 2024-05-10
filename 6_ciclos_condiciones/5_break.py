titlo_curso = 'Curso de Python'

for caracter in titlo_curso:

    if caracter == ' ':
        break # usado para terminar el proceso
    print(caracter)


for caracter in titlo_curso:

    if caracter == ' ':
        continue # usado para saltar a la proxima iteracion
    print(caracter)