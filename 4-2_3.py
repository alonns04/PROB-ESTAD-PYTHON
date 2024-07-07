import numpy as np
import matplotlib.pyplot as plt

# Generar datos de una distribución normal
np.random.seed(0)
datos = np.random.normal(loc=0, scale=1, size=1000)  # media=0, desviación estándar=1

# Crear el diagrama de caja
plt.boxplot(datos, vert=False)
plt.title('Diagrama de Caja de una Distribución Normal')
plt.xlabel('Valor')
plt.show()