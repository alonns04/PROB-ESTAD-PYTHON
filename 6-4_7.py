import pandas as pd
import numpy as np
import scipy.stats as stats
import math
from scipy.stats import t

# Leer el archivo Anorexia.dat
ruta_del_archivo = r'C:\UNI\Materias\Probabilidad y estadística\Prácticas\Anorexia.dat'
data = pd.read_csv(ruta_del_archivo, delim_whitespace=True)

# Filtrar datos para la terapia 'cb'
cb_data = data[data['therapy'] == 'cb']
cb_before = cb_data['before'].values
cb_after = cb_data['after'].values
cb_diff = cb_after - cb_before

# Filtrar datos para la terapia 'c'
c_data = data[data['therapy'] == 'c']
c_before = c_data['before'].values
c_after = c_data['after'].values

cb_diferencia = (cb_after - cb_before)
cb_diferencia = cb_diferencia.tolist()
c_diferencia = (c_after - c_before)
c_diferencia = c_diferencia.tolist()


def desviacion_muestral(lista):
    media = sum(lista) / len(lista)
    suma = 0
    for i in lista:
        suma += (i - media)**2
    return math.sqrt(suma / (len(lista) - 1))

def intervalo(lista, confianza):
    media = sum(lista) / len(lista)
    sem = (desviacion_muestral(lista) / math.sqrt(len(lista)))
    t_critico = -stats.t.ppf((1 - confianza) / 2, len(lista)-1)
    print(f"{media} - {t_critico} * {sem} = ", (media - t_critico * sem))
    print(f"{media} + {t_critico} * {sem} = ", (media + t_critico * sem))
    return (media - t_critico * sem, media + t_critico * sem)

print("Respuesta: ", intervalo(c_diferencia, 0.95))
print("Respuesta: ", intervalo(cb_diferencia, 0.95))
print("Respuesta: ", intervalo(c_diferencia, 0.99))
print("Respuesta: ", intervalo(cb_diferencia, 0.99))
