import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Parámetros
alpha = 0.01
df = 30
chi2_critico = stats.chi2.ppf(1 - alpha, df)
chi2_calculado = 24.3

# Generar puntos para graficar la distribución chi-cuadrado
x = np.linspace(0, 60, 1000)
y = stats.chi2.pdf(x, df)

# Graficar la distribución chi-cuadrado
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', label='Distribución Chi-cuadrado con df=30')
plt.axvline(chi2_critico, color='r', linestyle='--', label=f'Valor crítico ({alpha} área)')
plt.axvline(chi2_calculado, color='g', linestyle='-', label=f'Estadístico de prueba ($\\chi^2$={chi2_calculado:.2f})')
plt.fill_betweenx(y, x, chi2_critico, where=(x >= chi2_calculado), color='gray', alpha=0.5, label='Región de rechazo (una cola)')
plt.xlabel('Valor de $\\chi^2$')
plt.ylabel('Densidad de probabilidad')
plt.title('Prueba de hipótesis para la desviación estándar con $\\alpha=0.01$')
plt.legend()
plt.grid(True)
plt.xlim(0, 60)
plt.ylim(0, 0.15)
plt.show()
