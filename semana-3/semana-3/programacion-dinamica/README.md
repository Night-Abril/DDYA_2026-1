# Programación Dinámica en el Sistema de Estudiantes

## Idea principal

La programación dinámica se utiliza para evitar recomputaciones
almacenando resultados parciales.

En este sistema se aplica al cálculo del promedio de notas.

En lugar de recorrer toda la lista cada vez que se desea calcular el promedio,
se mantiene:

- suma acumulada de las notas
- cantidad de estudiantes

Esto permite calcular el promedio en tiempo constante.

## Comparación

Sin programación dinámica:
- Calcular promedio → O(n)

Con programación dinámica:
- Actualizar suma al registrar → O(1)
- Obtener promedio → O(1)

Esto reduce el costo computacional en consultas repetidas.
