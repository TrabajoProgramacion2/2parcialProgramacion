from funciones import *
from ingresos import *
from usuarios import *


while True:
    print("===================================")
    print("🎮  BIENVENIDO AL JUEGO DE PALABRAS  🎮")
    print("===================================\n")
    print("🔹 Reglas:")
    print(" - Inicie sesion o registrese Para poder jugar.")
    print(" - Armá palabras con las letras que se te muestren.")
    print(" - Cuanto más larga la palabra, más puntos sumás.")
    print(" - Escribí 'salir' en cualquier momento para terminar la ronda.")
    print("-----------------------------------\n")

    ingreso = pedir_entero(
        "\n1_Iniciar Sesion\n2_registrarse\n3_jugar \n4_salir. \nIngrese una opcion: ",
        "ERROR. Opcion invalida: ",
        1,
        4,
    )
    match ingreso:
        case 1:
            usuario = input("Ingrese su usuario: ")
            password = input("Ingrese su contraseña: ")
            login_usuario(usuario, password)
        case 2:
            usuario = input("Ingrese su usuario: ")
            password = input("Ingrese su contraseña: ")
            registrar_usuario(usuario, password)
        case 3:
            jugar_niveles()
            pass
        case 4:
            print("Saliendo del juego...")
            break
