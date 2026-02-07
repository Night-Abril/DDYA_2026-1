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

### Notación Big-O

Considerando que los estudiantes se almacenan en una lista, la complejidad temporal de las operaciones del sistema es la siguiente:

- Registrar estudiante: O(1), ya que solo se agrega un nuevo elemento a la lista.
- Consultar estudiante: O(n), debido a que puede ser necesario recorrer toda la lista para encontrar al estudiante.
- Actualizar estudiante: O(n), porque primero se debe buscar al estudiante en la lista.
- Eliminar estudiante: O(n), ya que se requiere localizar al estudiante antes de eliminarlo.

En el peor caso, el comportamiento del sistema está dominado por las operaciones de búsqueda, por lo que la complejidad temporal total del sistema es O(n).

### Mejor caso

El mejor caso ocurre cuando el sistema no necesita recorrer la lista de estudiantes para realizar una operación.  
Esto sucede, por ejemplo, cuando se registra un nuevo estudiante o cuando el estudiante buscado se encuentra en la primera posición de la lista.

En este escenario, el tiempo de ejecución no depende del número de estudiantes registrados, ya que se realizan pocas operaciones.

**Complejidad en el mejor caso:** O(1)

### Peor caso

El peor caso ocurre cuando el sistema debe recorrer completamente la lista de estudiantes para realizar una operación.  
Esto sucede cuando el estudiante buscado no se encuentra en el registro o cuando se encuentra en la última posición de la lista.

En este escenario, el tiempo de ejecución aumenta proporcionalmente al número de estudiantes registrados.

**Complejidad en el peor caso:** O(n)

### Gráficas de complejidad

A continuación se presentan las gráficas que representan el comportamiento del sistema en el mejor y peor caso:

**Mejor caso O(1):**

<img width="3000" height="1703" alt="Mejor caso O(1)" src="https://github.com/user-attachments/assets/ee568377-af50-45b6-b028-f68a1932046f" />

**Peor caso O(n):**

<img width="3000" height="1703" alt="Peor caso O(n)" src="https://github.com/user-attachments/assets/b2f41525-2b0f-44a3-b3cf-eb277a315d3c" />

Las gráficas fueron elaboradas utilizando GeoGebra y representan el crecimiento del costo computacional en función del tamaño de la entrada.

### Análisis propio

A partir del análisis realizado, se puede concluir que el sistema es eficiente para un número moderado de estudiantes.  
Las operaciones de registro presentan un costo constante, mientras que las operaciones de consulta, actualización y eliminación dependen linealmente del tamaño de la lista.

Para volúmenes de datos pequeños o medianos, este enfoque es adecuado y fácil de implementar. Sin embargo, para sistemas con una gran cantidad de estudiantes, sería recomendable utilizar estructuras de datos más eficientes que reduzcan el tiempo de búsqueda.

