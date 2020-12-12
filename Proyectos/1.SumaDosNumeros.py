def sumar(a , b):
    suma = a + b
    return suma

num1 = int(input('Ingrese num 1 :'))
num2 = int(input('Ingrese num 2 :'))

resultado = sumar(num1, num2)
print('El resultado de sumar {} con {} es = {}'.format(num1, num2, resultado))