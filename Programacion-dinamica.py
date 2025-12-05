import sys
import time


sys.setrecursionlimit(5000)


def cambio_dinamico(cantidad, monedas, memo, operaciones):
    """
    Resuelve el problema del cambio de moneda usando Programación Dinámica
    (Top-Down con Memoización).
    """

    operaciones[0] += 1

    if cantidad in memo:
        return memo[cantidad]

    if cantidad == 0:
        return 0
    if cantidad < 0:
        return float('inf')

    min_monedas = float('inf')

    for moneda in monedas:
        res = cambio_dinamico(cantidad - moneda, monedas, memo, operaciones)

        if res != float('inf'):
            min_monedas = min(min_monedas, res + 1)

    memo[cantidad] = min_monedas
    return min_monedas


if __name__ == "__main__":
    print("=== ALGORITMO DE PROGRAMACIÓN DINÁMICA ===")

    monedas = [1, 3, 4]
    cantidad_objetivo = 25
    ops = [0]
    memoria = {}

    print(f"Calculando cambio para: {cantidad_objetivo}")
    print(f"Monedas disponibles: {monedas}")

    inicio = time.time()
    resultado = cambio_dinamico(cantidad_objetivo, monedas, memoria, ops)
    fin = time.time()

    print("\n--- RESULTADOS ---")
    print(f"Mínimo de monedas: {resultado}")
    print(f"Operaciones realizadas: {ops[0]}")
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
