
palabras = []

respuesta= 1

insertarPalabra = lambda valor: palabras.append(valor)


while respuesta==1:
    nuevoValor = input('Digite la nueva palabra que desea ingresar: ')
    confirmar = int(input(f'Se va a ingresar la palabra : {nuevoValor} \n digite 1 para confirmar ó 2 para digitar nuevo valor '))
    if confirmar==1 :
        insertarPalabra(nuevoValor)
    else:
        pass
    reiniciar = int(input('Desea ingresar una nueva palabra? 1.Si 2.No '))

    if reiniciar==1:
        pass
    else:
        print('Finalizando palabras')
        respuesta=2


lista_ordenada = sorted(palabras, key=lambda palabra: len(palabra))


print(lista_ordenada)


