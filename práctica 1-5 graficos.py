"""
import matplotlib.pyplot as plt

# Crear una lista de valores de x de 1 a 1000
x = list(range(1, 1001))

# Crear una lista de valores de y (por ejemplo, y = x^2)
y = [i**2 for i in x]

# Crear la gráfica
plt.plot(x, y)

# Agregar etiquetas y título
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica de y = x^2')

# Mostrar la gráfica
plt.show()
"""
"""
import matplotlib.pyplot as plt

# Crear una lista de valores de x de 1 a 1000
x = list(range(1, 1001))

# Crear una lista de valores de y (por ejemplo, y = x^2)
y = [i**2 for i in x]

# Crear la gráfica de la función y = x^2
plt.plot(x, y, label='y = x^2')

# Agregar un punto en la posición (500, 500^2)
plt.scatter(500, 500**2, color='red', label='Punto de interés')

# Agregar etiquetas y título
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica de y = x^2 con un punto')

# Mostrar la leyenda
plt.legend()

# Mostrar la gráfica
plt.show()

"""
"""
import matplotlib.pyplot as plt
# Crear una lista de valores de Y (por ejemplo, valores aleatorios entre 0 y 1)
import random
tiradas_dado = [random.randint(1, 6) for _ in range(1000)]

valores_y = []
cincos = 0
for i in tiradas_dado:
    if i == 5:
        cincos += 1
    valores_y.append(cincos)

# Crear una lista de valores de X de 1 a 1000
valores_x = list(range(1, 1001))

# Crear la gráfica
plt.plot(valores_x, valores_y)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica de Y en función de X')

# Mostrar la gráfica

plt.show()
"""

import matplotlib.pyplot as plt
# Crear una lista de valores de Y (por ejemplo, valores aleatorios entre 0 y 1)
import random
tiradas_dado = [random.randint(1, 6) for _ in range(100000)]

valores_y = []
cincos = 0
for i, tirada in enumerate(tiradas_dado, start=1):
    if tirada == 5:
        cincos += 1
    frecuencia_relativa = cincos / i  # Calcular la frecuencia relativa en la iteración actual
    valores_y.append(frecuencia_relativa)

# Crear una lista de valores de X de 1 a 1000
valores_x = list(range(1, 100001))

# Crear la gráfica
plt.plot(valores_x, valores_y)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica de Y en función de X')

# Mostrar la gráfica

plt.show()
