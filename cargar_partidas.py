import csv


def cargar_partidas_csv():
    """
    Carga los datos de las partidas desde el archivo 'partidas.csv' y los organiza por nivel.

    El CSV debe tener el siguiente formato:
        nivel,letras,palabras
        1,C A S E A R,casera|casa|sera
        2,L I B R O S,libro|sol|rio|rol|bol

    La función transforma estos valores en estructuras Python y devuelve un
    diccionario donde cada clave es un nivel, y su valor es una lista de rondas
    posibles para ese nivel.

    Ejemplo de estructura retornada:
        {
            1: [
                {
                    "letras": ["C", "A", "S", "E", "A", "R"],
                    "palabras": ["casera", "casa", "sera"]
                }
            ],
            2: [
                {
                    "letras": ["L", "I", "B", "R", "O", "S"],
                    "palabras": ["libro", "sol", "rio", "rol", "bol"]
                }
            ]
        }

    Returns:
        dict: Diccionario con niveles como claves y listas de configuraciones
              de partida como valores.
    """
    niveles = {}

    with open("partidas.csv", "r", encoding="utf-8") as archivo:
        reader = csv.DictReader(archivo)

        for fila in reader:
            nivel = int(fila["nivel"])
            letras = fila["letras"].split(" ")
            palabras = fila["palabras"].split("|")

            if nivel not in niveles:
                niveles[nivel] = []

            niveles[nivel].append({"letras": letras, "palabras": palabras})

    return niveles
