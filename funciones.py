from datos import *
from ingresos import *
from usuarios import *
import time
import random


def iniciar_sesion():
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if login_usuario(usuario, contraseña):
        print("Inicio de sesión exitoso.")
        return usuario
    else:
        print("Usuario o contraseña incorrectos.")
        return None


def registrarse():
    usuario = input("Cree un nombre de usuario: ")
    contraseña = input("Cree una contraseña: ")

    registrar_usuario(usuario, contraseña)
    return usuario


def cargar_puntuacion(ingreso: str) -> int:
    puntos = len(ingreso)
    return puntos


def mostrar_letras(letras: list) -> str:
    texto = ""
    for letra in letras:
        texto += letra + " "
    return texto


def calcular_tiempo(limite: int, inicio):
    tiempo_transcurrido = time.time() - inicio
    tiempo_restante = limite - tiempo_transcurrido
    return tiempo_restante


def jugar_niveles():
    nivel = 1

    while nivel < 6:
        print(f"\nNIVEL -> {nivel:25}")

        nivel_pasado = jugar_partidas(nivel, niveles)

        if nivel_pasado:
            nivel += 1
        else:
            print("\nSaliste del juego")
            break

def jugar_partidas(nivel: int, niveles: dict):
    partida = 0
    errores_nivel = 0
    puntos_nivel = 0
    reinicio = 0

    categorias_mezcladas = niveles[nivel][:]
    random.shuffle(categorias_mezcladas)

    while partida < 3:

        print(f"\n--------------Partida {partida + 1}--------------")

        lista_retornada = jugar_ronda_con_categoria(categorias_mezcladas[partida])

        salir = lista_retornada[0]
        errores_nivel += lista_retornada[1]
        puntos_nivel += lista_retornada[2]
        tiempo_acabado = lista_retornada[3]

        if salir:
            return False

        if tiempo_acabado:
            reinicio += 1
            partida = 0
            print("\n⏳ Se acabó el tiempo. Nivel reiniciado.")
            continue

        partida += 1 

        if reinicio == 3:
            print("\n💀 Perdió las 3 vidas del nivel.")
            return False

        if partida == 3:
            print(f"Puntos obtenidos en el nivel: {puntos_nivel}")
            print(f"Cantidad de errores : {errores_nivel}")
            print("\n🎉 Usted pasó de nivel!!")
            return True


def jugar_ronda_con_categoria(datos_partida):
    lista_datos_retornados = []
    tiempo_acabado = False
    puntos_totales = 0
    lista_ingresos = []
    salir = False
    errores = 0

    categoria = datos_partida["categoria"]
    letras = datos_partida["letras"]
    palabras_validas = datos_partida["palabras"]

    inicio = time.time()

    while True:
        tiempo_restante = calcular_tiempo(10, inicio)
        if tiempo_restante <= 0:
            tiempo_acabado = True
            break

        cadena_letras = mostrar_letras(letras)
        print(f"\nCategoria: {categoria}")
        print(f"Letras: {cadena_letras:>20}\n")

        palabra_ingresada = pedir_cadena(
            "Ingrese una palabra:",
            "Error. Palabra fuera de rango(3 a 6 caracteres): ",
            6,
            3,
        )

        print(f"⏳ Tiempo restante: {tiempo_restante:.2f} segundos")

        if palabra_ingresada == "salir":
            salir = True
            break

        if palabra_ingresada in lista_ingresos:
            print("Esa palabra ya fue ingresada.")
            continue

        if palabra_ingresada in palabras_validas:
            print("✔ Palabra correcta!")
            lista_ingresos.append(palabra_ingresada)
            puntos_totales += cargar_puntuacion(palabra_ingresada)
        else:
            errores += 1
            print("✖ Palabra incorrecta!")

        if set(lista_ingresos) >= set(palabras_validas):
            print("🎉 Usted ganó la ronda.")
            break

    print("-" * 40)
    lista_datos_retornados += [salir, errores, puntos_totales, tiempo_acabado]
    return lista_datos_retornados
