# Ejercicio: Función prestiferous

## Descripción del ejercicio

El ejercicio consiste en analizar el comportamiento de la función `prestiferous`, determinando su costo computacional y estableciendo la notación Big-O correspondiente.

## Análisis de la función

La función `prestiferous` recibe como entrada un valor entero `n` y ejecuta un ciclo que itera desde 1 hasta `n`.  
Dentro del ciclo se realizan operaciones aritméticas simples que no dependen del tamaño de la entrada.

## Conteo de operaciones

- Inicialización de variables: 1 operación
- Comparación del ciclo: n veces
- Incremento del ciclo: n veces
- Operaciones internas constantes: n veces

El número total de operaciones es proporcional a `n`.

## Complejidad temporal

La complejidad temporal de la función es:

**O(n)**

Esto se debe a que el número de operaciones aumenta de forma lineal con respecto al tamaño de la entrada.

## Conclusión

La función `prestiferous` presenta un crecimiento lineal en su costo computacional, por lo que su ejecución es eficiente para tamaños de entrada moderados.
