import csv
from datos import niveles


def generar_archivo_partidas():
    with open("partidas.csv", "w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["nivel", "categoria", "letras", "palabras"])

        for nivel, partidas in niveles.items():
            for p in partidas:
                categoria = p["categoria"]
                letras = " ".join(p["letras"])
                palabras = "|".join(p["palabras"])

                writer.writerow([nivel, categoria, letras, palabras])

    print("✔ Archivo partidas.csv generado correctamente.")


generar_archivo_partidas()
