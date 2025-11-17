import json
import os

ARCHIVO = "usuarios.json"


# Cargar el archivo JSON
def crear_archivo():
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, "w") as archivo:
            archivo.write('{"usuarios": []}')


def leer_archivo():
    with open(ARCHIVO, "r") as archivo:
        contenido = archivo.read()
        datos = json.loads(contenido)
        return datos


def escribir_archivo(datos):
    texto = json.dumps(datos, indent=4)
    with open(ARCHIVO, "w") as archivo:
        archivo.write(texto)


def registrar_usuario(usuario, password):
    datos = leer_archivo()

    for u in datos["usuarios"]:
        if u["usuario"] == usuario:
            print("El usuario ya existe")
            return

    nuevo_usuario = {
        "usuario": usuario,
        "password": password,
        "estadisticas": {"partidas_jugadas": 0, "victorias": 0, "derrotas": 0},
    }

    datos["usuarios"].append(nuevo_usuario)
    escribir_archivo(datos)

    print("Usuario registrado con éxito")


def login_usuario(usuario, password):
    datos = leer_archivo()

    for u in datos["usuarios"]:
        if u["usuario"] == usuario and u["password"] == password:
            print("Inicio de sesión exitoso")
            return

    print("Credenciales incorrectas")
    return False
