# Ejercicio: Función pesky

## Descripción del ejercicio

El ejercicio consiste en analizar el comportamiento de la función `pesky`, identificando el número de operaciones que realiza y determinando su complejidad temporal en notación Big-O.

## Análisis de la función

La función `pesky` recibe como entrada un valor entero `n` y contiene dos ciclos anidados que dependen del tamaño de la entrada.

El ciclo externo se ejecuta `n` veces y, por cada iteración, el ciclo interno también se ejecuta `n` veces, realizando una operación constante en cada repetición.

## Conteo de operaciones

- Inicialización de variables: 1 operación
- Ciclo externo: n iteraciones
- Ciclo interno: n iteraciones por cada ciclo externo
- Operación interna constante: n × n veces

El número total de operaciones es proporcional a `n²`.

## Complejidad temporal

La complejidad temporal de la función es:

**O(n²)**

Esto se debe a la presencia de dos ciclos anidados que dependen directamente del tamaño de la entrada.

## Conclusión

La función `pesky` presenta un crecimiento cuadrático en su costo computacional, lo que implica que su tiempo de ejecución aumenta significativamente a medida que el tamaño de la entrada crece.
