import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Parámetros
df = 24  # grados de libertad
t_critico = 7.2  # valor crítico

# Valores de la distribución t
x = np.linspace(-10, 10, 1000)
y = stats.t.pdf(x, df)

# CDF para el valor crítico
p_valor_cola_superior = 1 - stats.t.cdf(t_critico, df)
p_valor_total = 2 * p_valor_cola_superior

# Gráfica de la distribución t y la región de rechazo
plt.plot(x, y, label='Distribución t con 24 grados de libertad')
plt.fill_between(x, y, where=(x >= t_critico) | (x <= -t_critico), color='red', alpha=0.5, label='Región de rechazo')
plt.axvline(t_critico, color='red', linestyle='--', label=f'Valor crítico: {t_critico}')
plt.axvline(-t_critico, color='red', linestyle='--')
plt.title('Distribución t y Región de Rechazo para t_critico = 7.2')
plt.xlabel('Valores de t')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.show()

# Mostrar resultados del p-valor
print(f'P-valor (cola superior): {p_valor_cola_superior}')
print(f'P-valor total (prueba bilateral): {p_valor_total}')
