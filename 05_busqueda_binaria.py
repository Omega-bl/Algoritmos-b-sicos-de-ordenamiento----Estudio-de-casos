# Práctica 5: buscar un precio descartando mitades.
# Tiempo: mejor O(1), promedio y peor O(log n).
# Es obligatorio que la lista esté ordenada de menor a mayor.


def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        # // calcula una división entera para obtener un índice.
        medio = (izquierda + derecha) // 2
        print("Reviso el índice", medio, "con el valor", lista[medio])

        if lista[medio] == objetivo:
            return medio
        elif objetivo < lista[medio]:
            # Continuar en la mitad izquierda.
            derecha = medio - 1
            print("Continúo en la mitad izquierda.")
        else:
            # Continuar en la mitad derecha.
            izquierda = medio + 1
            print("Continúo en la mitad derecha.")

    return -1


if __name__ == "__main__":
    # Si cambias los precios, conserva el orden ascendente.
    precios = [10, 20, 30, 40, 50]
    objetivo = 50  # Cambia a 99 para probar un dato ausente.

    print("BÚSQUEDA BINARIA")
    print("Precios ordenados:", precios)
    print("Precio que se busca:", objetivo, "\n")

    # Aquí se llama a la función de búsqueda.
    posicion = busqueda_binaria(precios, objetivo)

    if posicion == -1:
        print("\nEl precio no se encontró.")
    else:
        # Este índice corresponde a la lista ordenada.
        print("\nEncontrado en el índice:", posicion)
