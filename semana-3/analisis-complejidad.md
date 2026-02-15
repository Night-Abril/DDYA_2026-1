# Análisis de Complejidad – Sistema de Gestión de Estudiantes

## Enfoque utilizado
Para esta versión del sistema se implementan dos estrategias algorítmicas:

- **Divide y Conquista**: utilizada en la búsqueda binaria para encontrar estudiantes de forma eficiente.
- **Programación Dinámica**: aplicada en el cálculo del promedio de notas almacenando resultados parciales para evitar recomputaciones.

Los estudiantes se almacenan en una lista ordenada por nombre para permitir la aplicación de búsqueda binaria.

---

## Costo computacional de las operaciones

### Registrar estudiante
Agregar un estudiante al final de la lista.

Complejidad temporal: **O(1)**

---

### Buscar estudiante (Búsqueda binaria – Divide y Conquista)

Se divide la lista en mitades sucesivas hasta encontrar el estudiante.

Complejidad temporal:
- Mejor caso: **O(1)** (cuando el elemento está en el centro)
- Peor caso: **O(log n)**

---

### Actualizar estudiante

1. Buscar estudiante con búsqueda binaria → **O(log n)**
2. Modificar datos → **O(1)**

Complejidad total: **O(log n)**

---

### Eliminar estudiante

1. Buscar estudiante → **O(log n)**
2. Eliminar de la lista → **O(n)** (por desplazamiento de elementos)

Complejidad total: **O(n)**

---

### Calcular promedio (Programación Dinámica)

Se almacena la suma acumulada de las notas para evitar recalcular desde cero cada vez.

Complejidad temporal:
- Con DP: **O(1)** para obtener el promedio si la suma ya está almacenada.
- Sin DP: **O(n)**

---

## Complejidad global del sistema

El costo está dominado por la operación de eliminación:

**Complejidad en el peor caso: O(n)**

---

## Mejor caso

Ocurre cuando:
- La búsqueda encuentra el elemento en la primera división.
- El promedio ya está precalculado.

Complejidad: **O(1)**

---

## Peor caso

Ocurre cuando:
- El estudiante no está en la lista o está en la última posición.
- Se debe eliminar un elemento.

Complejidad: **O(n)**

---

## Análisis propio

La implementación mejora significativamente la búsqueda respecto a la versión anterior (de O(n) a O(log n)) mediante Divide y Conquista.

El uso de Programación Dinámica optimiza el cálculo del promedio evitando recorrer toda la lista en cada consulta.

Para grandes volúmenes de datos, se podría mejorar aún más utilizando estructuras como árboles balanceados o tablas hash.
