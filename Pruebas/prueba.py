import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Definiciones
z_0 = -2.27
alpha = 0.05
z_alpha = -1.645

# Rango de valores z para la gráfica
z = np.linspace(-4, 4, 1000)
pdf = stats.norm.pdf(z)

# Gráfica de la distribución normal estándar
plt.plot(z, pdf, label='Distribución Normal Estándar')

# Sombreado de la zona de significancia
plt.fill_between(z, 0, pdf, where=(z <= z_alpha), color='red', alpha=0.5, label='Zona de significancia (α = 0.05)')

# Línea vertical para z_0
plt.axvline(z_0, color='blue', linestyle='--', label=f'Estadístico de prueba (z_0 = {z_0})')

# Línea vertical para z_alpha
plt.axvline(z_alpha, color='black', linestyle='--', label=f'Valor crítico (z_α = {z_alpha})')

# Etiquetas y leyenda
plt.xlabel('z')
plt.ylabel('Densidad de probabilidad')
plt.title('Prueba de Hipótesis para una Proporción')
plt.legend()

# Mostrar la gráfica
plt.grid(True)
plt.show()


