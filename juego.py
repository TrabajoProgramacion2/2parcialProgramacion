import random
import time
from cargar_partidas import cargar_partidas_csv
from utilidades import cargar_puntuacion, mostrar_letras, calcular_tiempo

def _buscar_palabra_pendiente(pendientes):
    """Encuentra la primera palabra pendiente para el comodin."""
    if pendientes:
        return list(pendientes)[0]
    return None


def _manejar_comodin(comodin_usado: bool, palabras_pendientes: set) -> tuple[bool, set]:
    """
    Gestiona la activacion del comodin. Revela la palabra y la quita de pendientes, sin sumar puntos.
    Retorna: (comodin_usado_actualizado, palabras_pendientes_actualizadas)
    """
    if comodin_usado:
        print("⚠ Ya usaste el comodin.")
        return comodin_usado, palabras_pendientes

    palabra_revelar = _buscar_palabra_pendiente(palabras_pendientes)

    if palabra_revelar:
        print(f"✔ Palabra revelada: **{palabra_revelar}**")
        palabras_pendientes.remove(palabra_revelar)
        comodin_usado = True
    else:
        print("✖ No hay palabras pendientes para revelar.")

    return comodin_usado, palabras_pendientes


def jugar_ronda(datos_partida, comodin_usado, pedir_cadena_func):
    lista_datos_retornados = []
    tiempo_acabado = False
    puntos_totales = 0
    lista_ingresos = []
    salir = False
    errores = 0

    letras = datos_partida["letras"]
    palabras_validas = datos_partida["palabras"]
    palabras_pendientes = set(palabras_validas) - set(lista_ingresos)

    inicio = time.time()

    while True:
        tiempo_restante = calcular_tiempo(60, inicio)
        if tiempo_restante <= 0:
            tiempo_acabado = True
            break

        cadena_letras = mostrar_letras(letras)
        print(f"\nLetras disponibles: {cadena_letras}\n")

        palabra_ingresada = pedir_cadena_func(
            "Ingrese una palabra (ingresa 'comodin' para revelar una palabra, 'salir' para salir): ",
            "Error. Palabra fuera de rango (3 a 7 caracteres): ",
            7,
            3,
        )

        print(f"⏳ Tiempo restante: {tiempo_restante:.2f} segundos")

        if palabra_ingresada == "comodin":
            comodin_usado, palabras_pendientes = _manejar_comodin(
                comodin_usado, palabras_pendientes
            )
            continue

        if palabra_ingresada == "salir":
            salir = True
            break

        if palabra_ingresada in lista_ingresos:
            print("⚠ Esa palabra ya fue ingresada.")
            continue

        if palabra_ingresada in palabras_validas:
            print("✔ Palabra correcta!")
            lista_ingresos.append(palabra_ingresada)
            puntos_totales += cargar_puntuacion(palabra_ingresada)
            palabras_pendientes.discard(palabra_ingresada)

        else:
            errores = 1
            print("✖ Palabra incorrecta! Vida perdida.")
            break

        if not palabras_pendientes:
            print("🎉 ¡Usted ganó la ronda!")
            break

    print("-" * 40)
    lista_datos_retornados += [
        salir,
        errores,
        puntos_totales,
        tiempo_acabado,
        comodin_usado,
    ]
    return lista_datos_retornados


def jugar_partidas(nivel: int, niveles: dict, pedir_cadena_func):
    partida = 0
    puntos_nivel = 0
    reinicio = 0
    comodin_usado = False

    rondas_mezcladas = niveles[nivel][:]
    random.shuffle(rondas_mezcladas)

    while partida < 3:

        if reinicio >= 3:
            print("\n💀 Perdiste las 3 vidas del nivel. Nivel reiniciado.")
            return False

        print(f"\n--------------Partida {partida + 1}--------------")

        lista_retornada = jugar_ronda(
            rondas_mezcladas[partida], comodin_usado, pedir_cadena_func
        )

        salir = lista_retornada[0]
        error_en_ronda = lista_retornada[1]
        puntos_nivel += lista_retornada[2]
        tiempo_acabado = lista_retornada[3]
        comodin_usado = lista_retornada[4]

        if salir:
            return None

        if tiempo_acabado or error_en_ronda == 1:
            reinicio += 1

            if tiempo_acabado:
                print("\n⏳ Se acabo el tiempo. Vida perdida.")
            else:
                print("\n✖ Palabra incorrecta! Vida perdida.")

            print(f"Te quedan {3 - reinicio} vidas.")

            if reinicio >= 3:
                print("\n💀 ¡Game Over! El nivel se reiniciara.")
                return False

            continue

        partida += 1

        if partida == 3:
            print(f"Puntos obtenidos en el nivel: {puntos_nivel}")
            print("\n🎉 Usted paso de nivel!!")
            return True


def jugar_niveles(pedir_cadena_func):
    niveles = cargar_partidas_csv()
    nivel = 1
    reinicios_totales = 0

    while nivel < 6:
        print(f"\n🔵 NIVEL {nivel}")

        resultado = jugar_partidas(nivel, niveles, pedir_cadena_func)

        if resultado is True:
            nivel += 1
            reinicios_totales = 0

        elif resultado is False:
            reinicios_totales += 1
            print(
                f"El nivel se ha reiniciado. Llevas {reinicios_totales} de 3 reinicios permitidos."
            )

            if reinicios_totales >= 3:
                print("\n💀💀💀 Has agotado los 3 reinicios permitidos.")
                print("Reiniciando la partida completa al Nivel 1.")
                nivel = 1
                reinicios_totales = 0

            continue

        else:
            print("\nSaliste del juego")
            break
