def login():
    usuario=input("ingrese su usuario: ")
    contraseña=input("ingrese su contraseña: ")
    if usuario=="jhanet" and contraseña=="5824":
        return "usuario"
    elif usuario=="natsu" and contraseña=="3223":
        return "administrador"
    else:
        return "usuario o contraseña incorrectas"
def agregar_usuario():
    nick=input("ingrese nuevo usuario: ")
    password=input("ingrese nueva contraseña: ")
    return "nuevo usuario"
