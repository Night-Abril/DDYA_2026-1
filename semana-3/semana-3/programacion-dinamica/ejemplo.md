# Ejemplo de Programación Dinámica

## Sin Programación Dinámica

Cada vez que se calcula el promedio:

suma = 0  
recorrer toda la lista  
promedio = suma / n  

Complejidad: O(n)

---

## Con Programación Dinámica

Se mantiene una suma acumulada:

suma_total += nueva_nota  
contador += 1  

promedio = suma_total / contador  

Complejidad: O(1)
