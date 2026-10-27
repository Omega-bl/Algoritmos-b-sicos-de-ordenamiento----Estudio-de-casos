# Práctica 4: buscar un precio revisando uno por uno.
# Tiempo: mejor O(1), promedio y peor O(n).


def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        print("Reviso el índice", i, "con el valor", lista[i])

        if lista[i] == objetivo:
            # Devolver el índice donde se encontró el dato.
            return i

    # -1 indica que el dato no aparece en la lista.
    return -1


if __name__ == "__main__":
    # La búsqueda lineal funciona con datos desordenados.
    precios = [40, 20, 50, 10, 30]
    objetivo = 50  # Cambia a 99 para probar un dato ausente.

    print("BÚSQUEDA LINEAL")
    print("Precios:", precios)
    print("Precio que se busca:", objetivo, "\n")

    # Aquí se llama a la función de búsqueda.
    posicion = busqueda_lineal(precios, objetivo)

    if posicion == -1:
        print("\nEl precio no se encontró.")
    else:
        # Los índices empiezan en 0.
        print("\nEncontrado en el índice:", posicion)
