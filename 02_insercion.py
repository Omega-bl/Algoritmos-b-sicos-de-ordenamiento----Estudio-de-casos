# Práctica 2: insertar cada precio en la parte ordenada.
# Tiempo sin mensajes: mejor O(n), promedio y peor O(n²).


def insercion(lista):
    # El primer elemento forma la parte ordenada inicial.
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        print("\nVoy a insertar:", actual)

        # Desplazar los mayores para abrir un espacio.
        while j >= 0 and lista[j] > actual:
            print("Desplazo a la derecha:", lista[j])
            lista[j + 1] = lista[j]
            j -= 1

        # Colocar el valor guardado en su lugar.
        lista[j + 1] = actual
        print("La lista queda:", lista)

    return lista


if __name__ == "__main__":
    # Cambia estos precios para probar otro ejemplo.
    precios = [40, 20, 50, 10, 30]
    print("INSERCIÓN")
    print("Precios originales:", precios)

    # Aquí se llama a la función de ordenamiento.
    resultado = insercion(precios)
    print("\nResultado final:", resultado)

    # Prueba [10, 20, 30]: no será necesario desplazar valores.
