import time
estudiantes = []
print("=======GESTIÓN DE ESTUDIANTES=========")
while True:
    print("\nSeleccione una Opción:")
    print("1.Agregar estudiante")
    print("2.Mostrar estudiantes")
    print("3.Buscar estudiante")
    print("4.Eliminar estudiante")
    print("5.Ordenar estudiantes")
    print("6.Mostrar el total de estudianmtes")
    print("7.Salir del sistema")
    while True:
        try:
            opcion = int(input("Seelecciones una opción (1-7): "))
            break
        except ValueError:
            print("Ingrese correcatemte la opcion (1-7)")
            
    if opcion==1:
        #Agregar al estudiante
        nombre = input("Ingrese el nombre del estudiante: ")
        estudiantes.append(nombre)
        print(f"Estudiante {nombre} se agrego con éxito")
    elif opcion == 2:
        if estudiantes:
            print("\nLista de estudiantes")
            for estudiante in estudiantes:
                print(f"- {estudiante}")
            time.sleep(3) #Esperar 3 segundos
        else:
            print("No hay estudiantes en la lista")
    elif opcion == 3:
        nombre = input("Ingrese el nombre del estudiante a buscar: ")
        if nombre in estudiantes:
            print(f"El estudiante {nombre} esta en la lista")
        else:
            print(f"El estudiante {nombre} no esta la lista")
        time.sleep(3) #Esperar 3 segundos
    elif opcion == 4:
        nombre = input("Ingrese el nombre del estudiante a eliminar: ")
        if nombre in estudiantes:
            estudiantes.remove(nombre)
            print(f"El estudiante {nombre} eliminado con éxito")
        else:
            print(f"El estudiante {nombre} no esta la lista")
        time.sleep(3) #Esperar 3 segundos
    elif opcion == 5:
        estudiantes.sort()
        print("Lista ordenada correctamente")
        for estudiante in estudiantes:
            print(f"- {estudiante}")
            
        time.sleep(3) #Esperar 3 segundos
    elif opcion == 6:
        tlista = len(estudiantes)
        print(f"Total de estudiantes: {tlista}")
            
    elif opcion == 7:
        print("Saliendo del sistema....")
        for i in range(3,0,-1):
            print(f"Saliendo en: {i}")
            time.sleep(1)
        print("Hasta luego")
        break
    else:
        print("Opción invalida...Intente nuevamente")
    
   