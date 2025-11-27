import time


def cargar_puntuacion(ingreso: str) -> int:
    """Calcula la puntuación basada en la longitud de la palabra."""
    return len(ingreso)


def mostrar_letras(letras: list) -> str:
    """Convierte una lista de letras en una cadena separada por espacios."""
    return " ".join(letras)


def calcular_tiempo(limite: int, inicio):
    """Calcula el tiempo restante de la ronda."""
    return limite - (time.time() - inicio)
