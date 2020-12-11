def validarNombreArchivo(nombreArchivo):
    """ Valida si un nombre de archivo tiene la extension correspondiente"""
    if len(nombreArchivo) >= 3 and nombreArchivo[-3:] == '.py':
        return nombreArchivo
    return nombreArchivo + '.py'

print(validarNombreArchivo(input("ingresar nombre archivo : ")))
print(validarNombreArchivo(input("ingresar segundo nombre archivo : ")))