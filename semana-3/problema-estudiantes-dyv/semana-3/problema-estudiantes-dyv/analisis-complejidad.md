# Análisis de complejidad

## Enfoque anterior (Semana 2)

Las búsquedas se realizaban recorriendo toda la lista de estudiantes.

Complejidad:
- Búsqueda: O(n)
- Actualización: O(n)
- Eliminación: O(n)

## Nuevo enfoque: Divide y Vencerás

Se utiliza **búsqueda binaria**, la cual divide el problema en mitades en cada iteración.

Requisitos:
- La lista de estudiantes debe estar ordenada.

Complejidad:
- Búsqueda: O(log n)
- Actualización: O(log n) para encontrar + O(n) para desplazar elementos
- Eliminación: O(log n) para encontrar + O(n) para desplazar

## Mejor caso

El estudiante se encuentra en la posición central en la primera comparación.

Complejidad: O(1)

## Peor caso

Se realizan múltiples divisiones hasta reducir el espacio de búsqueda.

Complejidad: O(log n)

## Análisis propio

El uso de Divide y Vencerás mejora significativamente el tiempo de búsqueda en comparación con la búsqueda lineal.

Esto hace que el sistema sea más eficiente para grandes volúmenes de datos.
