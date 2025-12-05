Algoritmo Proyecto_Cambio_Moneda
    // Definición de variables
    Definir monedas Como Entero
    Definir n_monedas, cantidad_objetivo, i, resultado_pd, resultado_fb, op Como Entero
    Definir memo Como Entero
	
    // --- DATOS DE ENTRADA ---
    n_monedas <- 3
    Dimension monedas[n_monedas]
    monedas[1] <- 1
    monedas[2] <- 3
    monedas[3] <- 4
	
    cantidad_objetivo <- 30 
	
    Escribir "--- DATOS DEL PROBLEMA ---"
    Escribir "Cantidad a cambiar: ", cantidad_objetivo
    Escribir "Monedas disponibles: [1, 3, 4]"
    Escribir "--------------------------"
    Escribir ""
	
    // --- EJECUCIÓN PROGRAMACIÓN DINÁMICA ---
    // Dimensionamos para (cantidad + 1) espacios. 
    // Usaremos índice 1 para representar la cantidad 0.
    Dimension memo[cantidad_objetivo + 1]
	
    // Inicializamos el arreglo con -1
    Para i <- 0 Hasta cantidad_objetivo Hacer
        memo[i + 1] <- -1  // CORRECCIÓN: Sumamos 1 al índice
    FinPara
	
    op <- 0
    resultado_pd <- CambioPDTDR(cantidad_objetivo, monedas, n_monedas, memo, op)
	
    Escribir ">>> RESULTADOS PROGRAMACIÓN DINÁMICA <<<"
    Escribir "Mínimo de monedas: ", resultado_pd
    Escribir "Operaciones realizadas (ops): ", op
    Escribir ""
	
    // --- EJECUCIÓN FUERZA BRUTA ---
    op <- 0 
    // Si la cantidad es muy grande (>40), la fuerza bruta tardará mucho
    resultado_fb <- CambioFBR(cantidad_objetivo, monedas, n_monedas, op)
	
    Escribir ">>> RESULTADOS FUERZA BRUTA <<<"
    Escribir "Mínimo de monedas: ", resultado_fb
    Escribir "Operaciones realizadas (ops): ", op
	
FinAlgoritmo

// -----------------------------------------------------------------
// FUNCIÓN 1: PROGRAMACIÓN DINÁMICA 
// -----------------------------------------------------------------
SubProceso retorno <- CambioPDTDR(cant, monedas, n_monedas, memo, op Por Referencia)
    Definir retorno, i, res_temp, min_monedas Como Entero
    op <- op + 1 
	
    // CORRECCIÓN: Accedemos a memo[cant + 1] en lugar de memo[cant]
    // para respetar los índices de PSeInt (1..N)
	
    // 1. Verificar memoria
    Si memo[cant + 1] <> -1 Entonces
        retorno <- memo[cant + 1]
    Sino
        // 2. Caso Base: Cantidad 0
        Si cant = 0 Entonces
            memo[cant + 1] <- 0
            retorno <- 0
        Sino
            // 3. Caso Recursivo
            min_monedas <- 999999 
			
            Para i <- 1 Hasta n_monedas Hacer
                Si cant - monedas[i] >= 0 Entonces
                    res_temp <- CambioPDTDR(cant - monedas[i], monedas, n_monedas, memo, op)
                    
                    Si res_temp <> 999999 Entonces
                        Si res_temp + 1 < min_monedas Entonces
                            min_monedas <- res_temp + 1
                        FinSi
                    FinSi
                FinSi
            FinPara
			
            // Guardar en memoria (con índice ajustado)
            memo[cant + 1] <- min_monedas
            retorno <- min_monedas
        FinSi
    FinSi
FinSubProceso

// -----------------------------------------------------------------
// FUNCIÓN 2: FUERZA BRUTA RECURSIVA (Sin cambios en índices, no usa array)
// -----------------------------------------------------------------
SubProceso retorno <- CambioFBR(cant, monedas, n_monedas, op Por Referencia)
    Definir retorno, i, res_temp, min_monedas Como Entero
    op <- op + 1 
	
    Si cant = 0 Entonces
        retorno <- 0
    Sino
        min_monedas <- 999999 
		
        Para i <- 1 Hasta n_monedas Hacer
            Si cant - monedas[i] >= 0 Entonces
                res_temp <- CambioFBR(cant - monedas[i], monedas, n_monedas, op)
				
                Si res_temp <> 999999 Entonces
                    Si res_temp + 1 < min_monedas Entonces
                        min_monedas <- res_temp + 1
                    FinSi
                FinSi
            FinSi
        FinPara
		
        retorno <- min_monedas
    FinSi
FinSubProceso