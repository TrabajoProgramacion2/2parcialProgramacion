from juego import jugar_niveles
from ingresos import pedir_entero, pedir_cadena
from usuarios import login_usuario, registrar_usuario

while True:
    print("===================================")
    print("🎮  BIENVENIDO AL JUEGO DE PALABRAS  🎮")
    print("===================================\n")
    print("🔹 Reglas:")
    print(" - Inicie sesion o registrese Para poder jugar.")
    print(" - Arma palabras con las letras que se te muestren.")
    print(" - Cuanto mas larga la palabra, mas puntos sumas.")
    print(" - Escribi 'salir' en cualquier momento para terminar la ronda o el juego.")
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
            password = input("Ingrese su contraseña: ")
            login_usuario(usuario, password)
        case 2:
            usuario = input("Ingrese su usuario: ")
            password = input("Ingrese su contraseña: ")
            registrar_usuario(usuario, password)
        case 3:
            jugar_niveles(pedir_cadena)
        case 4:
            print("Saliendo del juego...")
            break
