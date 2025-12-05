import sys
import time

sys.setrecursionlimit(3000)


def cambio_fuerza_bruta(cantidad, monedas, operaciones):
    """
    Resuelve el problema del cambio de moneda usando Fuerza Bruta.
    Explora TODAS las combinaciones posibles.
    """
    operaciones[0] += 1

    if cantidad == 0:
        return 0

    if cantidad < 0:
        return float('inf')

    min_monedas = float('inf')

    for moneda in monedas:

        res = cambio_fuerza_bruta(cantidad - moneda, monedas, operaciones)

        if res != float('inf'):

            min_monedas = min(min_monedas, res + 1)

    return min_monedas


if __name__ == "__main__":
    print("=== ALGORITMO DE FUERZA BRUTA ===")

    monedas = [1, 3, 4]
    cantidad_objetivo = 25
    ops = [0]

    print(f"Calculando cambio para: {cantidad_objetivo}")
    print(f"Monedas disponibles: {monedas}")

    inicio = time.time()
    resultado = cambio_fuerza_bruta(cantidad_objetivo, monedas, ops)
    fin = time.time()

    print("\n--- RESULTADOS ---")
    print(f"Mínimo de monedas: {resultado}")
    print(f"Operaciones realizadas: {ops[0]}")
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
