# biografia y datos mas importantes de su persona, ademas de incorporar un menu en el cual se
# pueda o volver a imprimir o salir del mismo.
bibliografia = {
            'Nombre': 'Jose Ignacio Duran Daza',
            'Fecha Nac.': '10/11/1996',
            'Edad': '25',
            'Carrera': 'Ing. Ciencias de la Computación'
        }
while True:
    print(f'Seleccione la opción.\n\
          Presiona 1 para Bibliografia\n\
          Presiona 2 para salir\n\
          ')
    opcion = int(input())
    if opcion == 1:
        print(bibliografia)
    if opcion == 2:
        break
    input("Que opcion desea realizar?.")
