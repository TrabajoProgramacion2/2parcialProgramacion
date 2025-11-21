import csv
from datos import niveles


def generar_archivo_partidas():
    """
    Genera el archivo 'partidas.csv' a partir de la estructura de datos en 'niveles'.

    Se espera que 'niveles' sea un diccionario con la siguiente forma:
        {
            1: [
                {"letras": [...], "palabras": [...]},
                ...
            ],
            2: [...],
            ...
        }

    Esta función sobrescribe el archivo si ya existe.
    """

    with open("partidas.csv", "w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)

        writer.writerow(["nivel", "letras", "palabras"])

        for nivel, partidas in niveles.items():
            for p in partidas:
                letras = " ".join(p["letras"])
                palabras = "|".join(p["palabras"])

                writer.writerow([nivel, letras, palabras])

    print("✔ Archivo partidas.csv generado correctamente.")


generar_archivo_partidas()
