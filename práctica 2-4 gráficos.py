import matplotlib.pyplot as plt
from scipy.stats import binom

personas = 12
cada_persona = list(range(personas + 1))

ciudades = [
    ["Chicago", 0.20],
    ["Nueva York", 0.35],
    ["Albuquerque", 0.6]
]

for ciudad, porcentaje in ciudades:
    distribucion = [binom.pmf(i, personas, porcentaje) for i in cada_persona]
    plt.plot(cada_persona, distribucion, marker='o', label=ciudad)

plt.xticks(cada_persona)
plt.title('Distribución binomial')
plt.xlabel('Cantidad de hispanohablantes')
plt.ylabel('Probabilidad')
plt.legend()
plt.grid(True)
plt.show()
