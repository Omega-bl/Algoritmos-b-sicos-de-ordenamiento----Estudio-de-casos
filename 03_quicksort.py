# Práctica 3: ordenar dividiendo la lista alrededor de un pivote.
# Tiempo sin mensajes: mejor y promedio O(n log n); peor O(n²).
# El promedio supone un orden aleatorio de valores distintos.


def particionar(lista, inicio, fin):
    # En este ejemplo, el último valor es el pivote.
    pivote = lista[fin]
    i = inicio - 1

    print("\nParte que se ordena:", lista[inicio:fin + 1])
    print("Pivote elegido:", pivote)

    for j in range(inicio, fin):
        if lista[j] <= pivote:
            # Reunir a la izquierda los valores menores o iguales.
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    # El pivote queda en su posición definitiva.
    lista[i + 1], lista[fin] = lista[fin], lista[i + 1]
    print("Después de particionar:", lista)
    print("El pivote quedó en el índice", i + 1)
    return i + 1


def quick_sort(lista, inicio, fin):
    # Una parte con cero o un elemento ya está ordenada.
    if inicio < fin:
        # Aquí se usa la función que coloca el pivote.
        posicion = particionar(lista, inicio, fin)

        # Llamadas recursivas: ordenar las dos partes.
        quick_sort(lista, inicio, posicion - 1)
        quick_sort(lista, posicion + 1, fin)

    return lista


if __name__ == "__main__":
    # Cambia estos precios para probar otro ejemplo.
    precios = [40, 20, 50, 10, 30]
    print("QUICKSORT")
    print("Precios originales:", precios)

    # Aquí se llama a QuickSort con el primer y el último índice.
    resultado = quick_sort(precios, 0, len(precios) - 1)
    print("\nResultado final:", resultado)

    # Prueba [10, 20, 30, 40] y observa las partes desiguales.
