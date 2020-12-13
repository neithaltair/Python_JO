# Ejercicio 28: Calcular la diferencia de conjuntos

listaUno = ['amarillo', 'azul', 'rojo', 'fucsia', 'verde', 'negro', 'blanco']
listaDos = ['amarillo', 'azul', 'rojo', 'negro', 'plateado']

# Set es un metodo que contiene la funcion difference.
conjuntoUno = set(listaUno)
conjuntoDos = set(listaDos)

diferencia = conjuntoUno.difference(listaDos)
contiene = conjuntoDos.difference(listaUno)
opcion1 = conjuntoUno.union(listaDos)

print(diferencia); print(contiene); print(opcion1)