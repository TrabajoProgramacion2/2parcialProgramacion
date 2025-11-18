import csv


def cargar_partidas_csv():
    niveles = {}

    with open("partidas.csv", "r", encoding="utf-8") as archivo:
        reader = csv.DictReader(archivo)

        for fila in reader:
            nivel = int(fila["nivel"])
            categoria = fila["categoria"]
            letras = fila["letras"].split(" ")
            palabras = fila["palabras"].split("|")

            if nivel not in niveles:
                niveles[nivel] = []

            niveles[nivel].append(
                {"categoria": categoria, "letras": letras, "palabras": palabras}
            )

    return niveles
