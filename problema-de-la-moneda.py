import sys

# Aumentamos el límite de recursión por si acaso (para casos grandes en PD)
sys.setrecursionlimit(2000)

# --- 1. FUERZA BRUTA RECURSIVA (FBR) ---


def cambioFBR(cantidad, monedas):
    global op
    op += 1

    # Caso base: Si la cantidad es 0, se necesitan 0 monedas
    if cantidad == 0:
        return 0

    # Caso recursivo
    min_monedas = float('inf')

    for moneda in monedas:
        # Solo intentamos si la moneda no excede la cantidad actual
        if cantidad - moneda >= 0:
            res = cambioFBR(cantidad - moneda, monedas)
            if res != float('inf'):
                min_monedas = min(min_monedas, res + 1)

    return min_monedas

# --- 2. PROGRAMACIÓN DINÁMICA TOP-DOWN RECURSIVA (PDTDR) ---


def cambioPDTDR(cantidad, monedas, arreglo):
    global op
    op += 1

    # 1. Verificar si ya existe el cálculo en el arreglo (MEMORIA)
    if arreglo[cantidad] != -1:
        return arreglo[cantidad]

    # 2. Casos Base
    elif cantidad == 0:
        arreglo[cantidad] = 0
        return arreglo[cantidad]

    # 3. Caso Recursivo con Memorización
    else:
        min_monedas = float('inf')
        for moneda in monedas:
            if cantidad - moneda >= 0:
                res = cambioPDTDR(cantidad - moneda, monedas, arreglo)
                if res != float('inf'):
                    min_monedas = min(min_monedas, res + 1)

        # Guardamos el resultado en el arreglo antes de retornarlo
        arreglo[cantidad] = min_monedas
        return arreglo[cantidad]

# --- BLOQUE PRINCIPAL (MAIN) ---


# Configuración del caso de prueba
# Puedes cambiar estos valores para probar
monedas = [1, 3, 4]  # Denominaciones disponibles
# Cantidad a cambiar (¡No pongas un número muy grande para Fuerza Bruta!)
n = 30

print(f"--- ANALIZANDO PARA CANTIDAD: {n} ---")
print(f"--- MONEDAS DISPONIBLES: {monedas} ---\n")

# Ejecución Programación Dinámica
arreglo = [-1] * (n + 1)
op = 0
res_pd = cambioPDTDR(n, monedas, arreglo)
print(f"Programación Dinámica: {res_pd} monedas (Operaciones: {op})")

# Ejecución Fuerza Bruta
op = 0
# ADVERTENCIA: Si n > 50, Fuerza Bruta puede tardar mucho
res_fb = cambioFBR(n, monedas)
print(f"Fuerza Bruta:        {res_fb} monedas (Operaciones: {op})")
