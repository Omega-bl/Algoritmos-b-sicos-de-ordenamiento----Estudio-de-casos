# Práctica 1: ordenar precios comparando elementos vecinos.
# Tiempo sin mensajes: mejor O(n), promedio y peor O(n²).


def burbuja(lista):
    n = len(lista)

    for i in range(n - 1):
        hubo_cambios = False
        print("\nPasada", i + 1)

        # Las últimas i posiciones ya están ordenadas.
        for j in range(n - 1 - i):
            print("Comparo", lista[j], "con", lista[j + 1])

            if lista[j] > lista[j + 1]:
                # Intercambiar los vecinos que están al revés.
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                hubo_cambios = True
                print("Intercambio:", lista)

        if not hubo_cambios:
            print("No hubo cambios. La lista ya está ordenada.")
            break

    return lista


if __name__ == "__main__":
    # Cambia estos precios para probar otro ejemplo.
    precios = [40, 20, 50, 10, 30]
    print("BURBUJA")
    print("Precios originales:", precios)

    # Aquí se llama a la función de ordenamiento.
    resultado = burbuja(precios)
    print("\nResultado final:", resultado)

    # Prueba también [10, 20, 30] y observa cuándo termina.
