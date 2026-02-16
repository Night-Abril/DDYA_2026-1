# Ejercicio: Función mistery

## Descripción del ejercicio

El ejercicio consiste en analizar el comportamiento de la función `mistery`, determinando su costo computacional en función del tamaño de la entrada. Para ello, se realiza el conteo de operaciones y se establece la notación Big-O correspondiente.

## Análisis de la función

La función `mistery` recibe como entrada un valor entero `n` y ejecuta un ciclo que itera desde 0 hasta `n`.

Durante cada iteración del ciclo se realiza una operación constante, por lo que el número total de operaciones crece de manera proporcional al tamaño de la entrada.

## Conteo de operaciones

- Inicialización de variables: 1 operación
- Comparación del ciclo: n veces
- Incremento del ciclo: n veces
- Operación interna del ciclo: n veces

El número total de operaciones es proporcional a `n`.

## Complejidad temporal

La complejidad temporal de la función es:

**O(n)**

Esto se debe a que el número de operaciones crece linealmente conforme aumenta el tamaño de la entrada.

## Conclusión

La función `mistery` presenta un crecimiento lineal en su costo computacional, lo que la hace eficiente para valores pequeños y medianos de entrada, pero su tiempo de ejecución aumenta proporcionalmente a medida que crece `n`.
