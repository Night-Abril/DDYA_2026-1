# Descripción del problema

Se requiere diseñar un sistema para gestionar la información de los estudiantes de manera eficiente.

A diferencia de la implementación de la semana 2, en esta versión se aplicará la estrategia de **Divide y Vencerás**, con el objetivo de mejorar el proceso de búsqueda de estudiantes dentro del sistema.

El problema consiste en:

- Registrar estudiantes
- Consultar estudiantes
- Actualizar estudiantes
- Eliminar estudiantes

Para optimizar la búsqueda, los estudiantes serán organizados en una estructura ordenada que permita aplicar **búsqueda binaria**, reduciendo el tiempo de búsqueda de O(n) a O(log n).

Este enfoque permite mejorar el rendimiento del sistema cuando el número de estudiantes es grande.
