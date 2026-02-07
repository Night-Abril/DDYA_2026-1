# Problema: Gestión de estudiantes

## Descripción del problema

En un entorno académico, es necesario llevar un control organizado de la información de los estudiantes que pertenecen a una institución educativa.  
Actualmente, la gestión manual de estos datos puede generar errores, pérdida de información y dificultad para realizar consultas rápidas.

El problema consiste en diseñar un programa que permita administrar la información básica de los estudiantes, facilitando el registro, la consulta y la actualización de datos de manera eficiente.

Este sistema busca optimizar el manejo de la información estudiantil y servir como apoyo en procesos académicos y administrativos.

## Requerimientos del sistema (Historias de usuario)

- **HU-01**  
  Como usuario del sistema,  
  quiero registrar un estudiante con su información básica,  
  para llevar un control organizado de los estudiantes.

- **HU-02**  
  Como usuario del sistema,  
  quiero consultar la información de un estudiante,  
  para acceder rápidamente a sus datos cuando sea necesario.

- **HU-03**  
  Como usuario del sistema,  
  quiero actualizar la información de un estudiante,  
  para mantener los datos correctos y actualizados.

- **HU-04**  
  Como usuario del sistema,  
  quiero eliminar un estudiante del registro,  
  para depurar la información que ya no es necesaria.

## Diagramas de flujo

El siguiente diagrama representa el flujo general del sistema de gestión de estudiantes, mostrando las opciones disponibles y el comportamiento del sistema según la opción seleccionada por el usuario.

[Diagrama de flujo del sistema de estudiantes](https://github.com/Night-Abril/DDYA_2026-1/tree/Semana-2/problema-estudiantes/diagramas-flujo#diagramas-de-flujo)

## Análisis de complejidad

En esta sección se analiza el costo computacional del sistema de gestión de estudiantes, teniendo en cuenta el tiempo de ejecución de las operaciones principales según el número de estudiantes registrados.

### Costo computacional (tiempo)

El tiempo de ejecución del sistema depende principalmente del número de estudiantes registrados.  
Cada una de las operaciones realiza un conjunto de acciones que pueden variar en costo según el tamaño de la lista de estudiantes.

Registrar un estudiante implica agregar su información a la lista, lo cual no requiere recorrer los datos existentes.

Consultar, actualizar o eliminar un estudiante requiere buscarlo dentro de la lista, lo que puede implicar recorrer varios elementos hasta encontrar el estudiante deseado.
