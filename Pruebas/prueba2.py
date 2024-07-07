import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Datos de la muestra
datos = np.array([10.2, 9.7, 10.1, 10.3, 10.1, 9.8, 9.9, 10.4, 10.3, 9.8])
n = len(datos)
media_muestral = np.mean(datos)
desviacion_estandar_muestral = np.std(datos, ddof=1)  # Usamos ddof=1 para obtener la desviación estándar muestral

# Hipótesis nula
mu = 10

# Estadístico de prueba t
t = (media_muestral - mu) / (desviacion_estandar_muestral / np.sqrt(n))

# Valor crítico de t para alpha=0.01 y df=9 (dos colas)
t_critico_superior = stats.t.ppf(1 - 0.01/2, df=n-1)
t_critico_inferior = -t_critico_superior
alpha = 0.01
# Generar puntos para graficar la distribución t de Student
x = np.linspace(-4, 4, 1000)
y = stats.t.pdf(x, df=n-1)

# Graficar la distribución t de Student
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', label=f'Distribución t de Student con df={n-1}')
plt.axvline(t_critico_superior, color='r', linestyle='--', label=f'Valor crítico superior ({alpha/2} área)')
plt.axvline(t_critico_inferior, color='r', linestyle='--', label=f'Valor crítico inferior ({alpha/2} área)')
plt.axvline(t, color='g', linestyle='-', label=f'Estadístico de prueba ($t$={t:.3f})')
plt.fill_betweenx(y, x, t_critico_superior, where=(x >= t), color='gray', alpha=0.5, label='Región de rechazo (dos colas)')
plt.fill_betweenx(y, x, t_critico_inferior, where=(x <= -t), color='gray', alpha=0.5)
plt.xlabel('Valor de $t$')
plt.ylabel('Densidad de probabilidad')
plt.title('Prueba de hipótesis para la media con $\\alpha=0.01$ (dos colas)')
plt.legend()
plt.grid(True)
plt.xlim(-4, 4)
plt.ylim(0, 0.4)
plt.show()
