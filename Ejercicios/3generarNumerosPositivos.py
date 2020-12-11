# En caso de que el usuario no especifique el numero, tomara el valor de 100 por defecto
def generarNumPares( n = 100):
    pares = []

    contador = 0
    numero = 0

    while contador < n:
        if numero % 2 == 0:
            pares.append(numero)
            contador += 1
        numero += 1

    return pares

n = int(input('Escriba la cantidad de numeros pares positivos a generar: '))

if n > 0:
    pares = generarNumPares(n)

    print(pares)
    print('Cantidad de pares:', len(pares))
