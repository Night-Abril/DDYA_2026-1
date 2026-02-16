# Ejercicio: Insertion Sort Descendente

## Descripción del ejercicio

El ejercicio consiste en analizar el algoritmo de ordenamiento Insertion Sort aplicado de forma descendente, determinando su funcionamiento y su complejidad temporal.

## Descripción del algoritmo

Insertion Sort es un algoritmo de ordenamiento que construye la lista ordenada de manera incremental, tomando un elemento a la vez e insertándolo en la posición correcta dentro de la parte ya ordenada del arreglo.

En la versión descendente, los elementos se organizan de mayor a menor.

## Funcionamiento general

El algoritmo recorre el arreglo desde el segundo elemento hasta el final.  
En cada iteración, se compara el elemento actual con los anteriores y se desplaza hacia la izquierda hasta encontrar la posición correcta según el orden descendente.

## Complejidad temporal

- **Mejor caso:**  
  O(n), cuando el arreglo ya se encuentra ordenado de forma descendente.

- **Peor caso:**  
  O(n²), cuando el arreglo se encuentra ordenado de forma ascendente y cada elemento debe desplazarse completamente.

## Conclusión

Insertion Sort descendente es un algoritmo sencillo y fácil de implementar, adecuado para arreglos pequeños. Sin embargo, su rendimiento disminuye considerablemente para entradas grandes debido a su complejidad cuadrática en el peor caso.
