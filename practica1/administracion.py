from funciones import (agregar_usuario)
def menu_administrador():
    while True:
        print("**MENU ADMINISTRADOR**")
        print("1. Agregar usuario")
        print("2. Eliminar usuario")
        print("3. Modificar usuario")
        print("4. Salir")
        opcion=input("Ingrese una opción: ")
        if opcion=="1":
            registro=menu_administrador()
            if registro=="nuevo usuario":
                agregar_usuario()
            print("agregando nuevo usuario")
        elif opcion=="2":
            print("eliminando usuario")
        elif opcion=="3":
            print("midificando usuario")
        elif opcion=="4":
            return "Saliendo del menú de administrador"
            break
        else:
            return "opcion invalida"