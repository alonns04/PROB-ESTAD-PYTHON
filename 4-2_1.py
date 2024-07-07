"""
lista = [1.6, 1.9, 2.2, 2.5, 2.6, 2.6, 2.9, 3.0, 3.0, 3.1,
         3.1, 3.1, 3.1, 3.2, 3.2, 3.2, 3.3, 3.3, 3.3, 3.4, 
         3.4, 3.4, 3.5, 3.5, 3.6, 3.7, 3.7, 3.7, 3.8, 3.8, 
         3.9, 3.9, 4.1, 4.1, 4.2, 4.3, 4.4, 4.5, 4.7, 4.7]

print(len(lista))

media = sum(lista)/len(lista)
mediana = (lista[len(lista)//2] + lista[len(lista)//2 - 1]) / 2 
q1 = (lista[len(lista)//2//2] + lista[len(lista)//2//2 - 1]) / 2 
q3 = (lista[len(lista)//2 + len(lista)//2//2] + lista[len(lista)//2 + len(lista)//2//2 - 1]) / 2 

sumatoria = 0

for i in lista:
    sumatoria += (i - sum(lista)/len(lista))**2

varianza = sumatoria / (len(lista) - 1)

print("media: ", media)
print("mediana: ", mediana)
print("q1: ", q1)
print("q3: ", q3)
print("Varianza: ", varianza)
"""
import pandas as pd
import numpy as np

# Lista de valores proporcionados
datos = [1.6, 1.9, 2.2, 2.5, 2.6, 2.6, 2.9, 3, 3, 3.1, 3.1, 3.1, 3.1, 3.2, 3.2, 3.2, 3.3, 3.3, 3.3, 3.4, 3.4,
         3.4, 3.5, 3.5, 3.6, 3.7, 3.7, 3.7, 3.8, 3.8, 3.9, 3.9, 4.1, 4.1, 4.2, 4.3, 4.4, 4.5, 4.7, 4.7]

# Definir los intervalos de clase
intervalos = np.arange(1.5, 5, 0.5)

# Crear una tabla de frecuencias utilizando pandas
tabla_frecuencias = pd.cut(datos, bins=intervalos, right=False)
frecuencia = tabla_frecuencias.value_counts().sort_index()

# Calcular la marca de clase (punto medio de cada intervalo)
marca_clase = [interval.left + (interval.right - interval.left) / 2 for interval in frecuencia.index]

# Calcular la frecuencia relativa
frecuencia_relativa = frecuencia / len(datos)

# Calcular la frecuencia acumulada
frecuencia_acumulada = frecuencia.cumsum()

# Calcular la frecuencia acumulada relativa
frecuencia_acumulada_relativa = frecuencia_relativa.cumsum()

# Crear un DataFrame para organizar la tabla de frecuencias
tabla = pd.DataFrame({
    'Intervalo de clase': frecuencia.index,
    'Marca de clase': marca_clase,
    'Frecuencia': frecuencia,
    'Frecuencia relativa': frecuencia_relativa,
    'Frecuencia acumulada': frecuencia_acumulada,
    'Frecuencia acumulada relativa': frecuencia_acumulada_relativa
})

# Mostrar la tabla
print(tabla)
