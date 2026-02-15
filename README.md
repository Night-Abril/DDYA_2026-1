# Semana 3 – Diseño de Datos y Análisis de Algoritmos

## Descripción del proyecto
Sistema de gestión de estudiantes que permite:

- Registrar estudiantes
- Buscar estudiantes (Divide y Conquista – Búsqueda binaria)
- Actualizar información
- Eliminar estudiantes
- Calcular promedio (Programación Dinámica)

El sistema está optimizado para mejorar el rendimiento en operaciones de búsqueda y cálculo de promedios.

---

## Estrategias algorítmicas utilizadas

### Divide y Conquista
Se implementa en la búsqueda binaria para localizar estudiantes en una lista ordenada.

Complejidad:
- Mejor caso: O(1)
- Peor caso: O(log n)

---

### Programación Dinámica
Se utiliza para almacenar la suma acumulada de las notas y calcular el promedio en tiempo constante.

Complejidad:
- Con DP: O(1)
- Sin DP: O(n)

---

## Análisis de complejidad del sistema

| Operación | Complejidad |
|----------|------------|
Registrar estudiante | O(1) |
Buscar estudiante | O(log n) |
Actualizar estudiante | O(log n) |
Eliminar estudiante | O(n) |
Calcular promedio | O(1) |

Complejidad global (peor caso): **O(n)**



