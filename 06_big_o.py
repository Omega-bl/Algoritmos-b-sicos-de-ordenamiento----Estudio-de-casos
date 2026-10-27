# Práctica 6: observar cómo crece el trabajo al aumentar n.
# Contamos operaciones principales; no medimos segundos.
# Son ejemplos de crecimiento, no algoritmos de ordenamiento.


def constante(n):
    # Una operación, sin importar el valor de n.
    operaciones = 1
    return operaciones


def logaritmico(n):
    operaciones = 0
    pendiente = n

    # Reducir el tamaño a la mitad en cada vuelta.
    while pendiente > 1:
        pendiente //= 2
        operaciones += 1

    return operaciones


def lineal(n):
    operaciones = 0

    for i in range(n):
        operaciones += 1

    return operaciones


def lineal_logaritmico(n):
    operaciones = 0

    for i in range(n):
        pendiente = n
        while pendiente > 1:
            pendiente //= 2
            operaciones += 1

    return operaciones


def cuadratico(n):
    operaciones = 0

    # Cada una de las n vueltas repite otro ciclo de n vueltas.
    for i in range(n):
        for j in range(n):
            operaciones += 1

    return operaciones


if __name__ == "__main__":
    print("BIG-O: CONTEO DE OPERACIONES PRINCIPALES")

    # Cambia estos tamaños por otros números positivos.
    for cantidad in [4, 8, 16]:
        print("\nCantidad de datos:", cantidad)

        # Aquí se llama a cada función y se muestra su conteo.
        print("O(1):", constante(cantidad))
        print("O(log n):", logaritmico(cantidad))
        print("O(n):", lineal(cantidad))
        print("O(n log n):", lineal_logaritmico(cantidad))
        print("O(n²):", cuadratico(cantidad))

    # Observa cuánto aumenta cada conteo al duplicar los datos.
