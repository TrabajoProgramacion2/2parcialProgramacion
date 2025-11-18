def pedir_entero(mensaje: str, mensaje_error: str, minimo = None, maximo = None,  reintentos = 100)-> int|None:
    """_summary_

    Args:
        mensaje (str): Texto que pide el dato a ingresar
        mensaje_error (str): Texto que pide el reingreso del dato
        minimo (_type_, optional): numero minimo a ingresar
        maximo (_type_, optional): numero maximo a ingresar
        reintentos (int, optional): numero de reintentos

    Returns:
        int|None: retorna el entero ingresado o None en caso de acabar con los reintentos
    """
    contador = 0
    ingreso = int(input(mensaje))
    while (minimo != None and ingreso < minimo) or (maximo != None and ingreso > maximo) :
        contador += 1
        
        if contador > reintentos:
            return None
        ingreso = int(input(mensaje_error))
    return ingreso



def pedir_cadena(mensaje: str, mensaje_error: str,maxima_longitud: int, minima_longitud: int )-> str:
    cadena = str(input(mensaje))
    longitud_ingreso = len(cadena)
    
    while longitud_ingreso > maxima_longitud or longitud_ingreso < minima_longitud:
        cadena = str(input(mensaje_error))
        longitud_ingreso = len(cadena)
    return cadena