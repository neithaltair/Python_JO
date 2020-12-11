def producto_cadena(cadena, repeticion):
    """Emula el funcionamiento de la tecla producto * """
    resultado = ""
    for i in range(repeticion):
        resultado += cadena
    print(resultado)

producto_cadena('Cadenas', 5)