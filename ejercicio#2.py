import random

bd = [
    {"departamento": "Amazonas", "capital": "Leticia"},
    {"departamento": "Antioquia", "capital": "Medellín"},
    {"departamento": "Arauca", "capital": "Arauca"},
    {"departamento": "Atlántico", "capital": "Barranquilla"},
    {"departamento": "Bolívar", "capital": "Cartagena"},
    {"departamento": "Boyacá", "capital": "Tunja"},
    {"departamento": "Caldas", "capital": "Manizales"},
    {"departamento": "Caquetá", "capital": "Florencia"},
    {"departamento": "Casanare", "capital": "Yopal"},
    {"departamento": "Cauca", "capital": "Popayán"},
    {"departamento": "Cesar", "capital": "Valledupar"},
    {"departamento": "Chocó", "capital": "Quibdó"},
    {"departamento": "Córdoba", "capital": "Montería"},
    {"departamento": "Cundinamarca", "capital": "Bogotá, D.C."},
    {"departamento": "Guainía", "capital": "Inírida"},
    {"departamento": "Guaviare", "capital": "San José del Guaviare"},
    {"departamento": "Huila", "capital": "Neiva"},
    {"departamento": "La Guajira", "capital": "Riohacha"},
    {"departamento": "Magdalena", "capital": "Santa Marta"},
    {"departamento": "Meta", "capital": "Villavicencio"},
    {"departamento": "Nariño", "capital": "Pasto"},
    {"departamento": "Norte de Santander", "capital": "Cúcuta"},
    {"departamento": "Putumayo", "capital": "Mocoa"},
    {"departamento": "Quindío", "capital": "Armenia"},
    {"departamento": "Risaralda", "capital": "Pereira"},
    {"departamento": "San Andrés y Providencia", "capital": "San Andrés"},
    {"departamento": "Santander", "capital": "Bucaramanga"},
    {"departamento": "Sucre", "capital": "Sincelejo"},
    {"departamento": "Tolima", "capital": "Ibagué"},
    {"departamento": "Valle del Cauca", "capital": "Cali"},
    {"departamento": "Vaupés", "capital": "Mitú"},
    {"departamento": "Vichada", "capital": "Puerto Carreño"}
]

#32
generarNumeroAleatorio = lambda: random.randint(1, len(bd) -1)

def terminarProceso():
    print('Finalizando proceso')
    


respuesta = int(input('Quieres empezar el concurso? 1.Si 2.No '))

if respuesta==1 :
    
    print('Empezando concurso....')
    while respuesta==1 :
        numero = generarNumeroAleatorio()
        intentos = 3
        print(f'Y el departamento ganador es {bd[numero]["departamento"]}')
        while True:

            
            respuestaUsuario  = input(f'digita la capital de {bd[numero]["departamento"]} Tienes {intentos} intentos: ' )
            

            if  respuestaUsuario == bd[numero]["capital"]:
                print("Has acertado!!")
                siguiente = input(f"¿Quieres seguir jugando? S/N ")

                if siguiente.lower()== 's':
                    break
                else:
                        respuesta=2
                        terminarProceso()
                        break
                    
            else :
                print('Respuesta incorrecta')
                intentos-= 1
                if intentos == 0 :
                    print('Has perdido todas las opciones')
                    siguienteRetry = input(f"¿Quieres seguir jugando? S/N ")

                    if siguienteRetry.lower()== 's':
                        break
                    else:
                        respuesta=2
                        terminarProceso()
                        break
                       
                        
                    
                    

        

else :
    print('Finalizando concurso')
    


