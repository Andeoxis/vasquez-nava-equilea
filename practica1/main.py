from funciones import login
from administracion import menu_administrador
from usuario import menu_usuario
def main():
    print("**BIENVENIDO AL SISTEMA LOGIN**")
    tipo_de_cuenta=login()
    if tipo_de_cuenta=="administrador":
        menu_administrador()
    elif tipo_de_cuenta=="usuario":
        menu_usuario()
    else:
        print("error acceso denegado")
main()
