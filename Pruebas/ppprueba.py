import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# Datos del problema
mu0 = 100000
x_bar = 110000
s = 25000
n = 50
alpha = 0.05

# Cálculo del estadístico T
T = (x_bar - mu0) / (s / np.sqrt(n))

# Valor crítico t para alpha = 0.05 y df = n - 1
df = n - 1
t_alpha = t.ppf(1 - alpha, df)

# Función de densidad de probabilidad t de Student
x = np.linspace(-4, 4, 1000)
y = t.pdf(x, df)

# Gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', label=f'Distribución t de Student (df={df})')
plt.fill_between(x, 0, y, where=(x > t_alpha), color='red', alpha=0.3, label='Zona de rechazo')
plt.fill_between(x, 0, y, where=(x <= t_alpha), color='green', alpha=0.3, label='Zona de no rechazo')
plt.axvline(T, color='black', linestyle='dashed', linewidth=1, label=f'Estadístico T = {T:.2f}')
plt.title('Test de Hipótesis - Neumáticos Ford')
plt.xlabel('Valor de T')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.grid(True)
plt.show()
