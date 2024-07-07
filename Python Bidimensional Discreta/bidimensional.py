import numpy as np
"""
# Crear matrices
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print("Matriz A:")
print(A)

print("\nMatriz B:")
print(B)

# Suma de matrices
C = A + B
print("\nSuma de A y B:")
print(C)

# Producto elemento a elemento
D = A * B
print("\nProducto elemento a elemento de A y B:")
print(D)

# Producto matricial
E = np.dot(A, B)
print("\nProducto matricial de A y B:")
print(E)

# Transposición
F = A.T
print("\nTransposición de A:")
print(F)

# Determinante
G = np.linalg.det(A)
print("\nDeterminante de A:")
print(G)

# Inversa (solo para matrices cuadradas e invertibles)
H = np.array([[1, 2], [3, 4]])
I = np.linalg.inv(H)
print("\nMatriz H:")
print(H)

print("\nInversa de H:")
print(I)
"""
"""
value_x = int(input("x"))

x = []

for i in range(value_x):
    value = input({i})
    x.append(value)
value_y = input("y")

"""
"""
        for ix in range(self.x):
            fila = []
            for iy in range(self.y):
                valor = float(input(f"Valor x = {ix+1} y = {iy+1}: "))
                valor = format(valor, '.5f')[slice(6)]
                fila.append(valor)
            matriz.append(fila)
        self.matriz = matriz
"""
import math

def acomodar(numero):
    if isinstance(numero, (int, float)):
        return format(numero, '.5f')[slice(4)]
    else:
        return numero

class Matriz:
    def __init__(self, x = 0, y = 0, matriz = []):
        self.x = x  # tamaño de x
        self.y = y # tamaño de y
        self.matriz = matriz
        self.matriz_marginal_x = [["   x  "], [" p(y) "]]
        self.matriz_marginal_y = [["   y  "], [" p(y) "]]
        self.ex = 0
        self.ey = 0
        self.exx = 0
        self.eyy = 0
        self.exxyy = 0
        self.vx = 0
        self.vy = 0
        self.vxy = 0
        self.exy = 0
        self.cxy = 0
        self.ccxy = 0
        self.dexy = 0
        self.vxmasy = 0
        self.exmasy = 0

    def vacio(self): 
        y = ["''"]
        for i in range(self.y + 1):
            self.matriz.append("''")
            y.append("''")
        for ix in range(self.x):
            self.matriz.append(y)

    def variables(self):    
        matriz = [[" x/y "]]

        for iy in range(self.y):
            valor_x = float(input(f"Valor y = {iy+1}: "))
            valor_x = acomodar(valor_x)
            matriz[0].append(valor_x)

        for ix in range(self.x):
            fila = []
            valor_x = float(input(f"Valor x = {ix+1}: "))
            valor_x = acomodar(valor_x)
            fila.append(valor_x)
            matriz.append(fila)

        self.matriz = matriz


    def valores(self):
        matriz = self.matriz
        
        for ix in range(self.x):
            for iy in range(self.y):
                valor_xy = float(input(f"Valor xy: x = {ix+1} y = {iy+1}: "))
                valor_xy = acomodar(valor_xy)
                matriz[ix+1].append(valor_xy)

        self.matriz = matriz

    def valor(self, a, b):
        return self.matriz[a][b]

    def marginal_x(self):

        for ix in range(self.x):
            self.matriz_marginal_x[0].append(acomodar(self.valor(ix+1, 0)))
            suma = 0
            for iy in range(self.y):
                suma += float(self.valor(ix+1, iy+1))
            self.matriz_marginal_x[1].append(acomodar(suma))
        return Matriz(self.x, self.y, self.matriz_marginal_x)

    def marginal_y(self):

        for iy in range(self.y):
            self.matriz_marginal_y[0].append(acomodar(self.valor(0, iy+1)))
            suma = 0
            for ix in range(self.x):
                suma += float(self.valor(ix+1,iy+1))
            self.matriz_marginal_y[1].append(acomodar(suma))
        return Matriz(self.x, self.y, self.matriz_marginal_y)

    def esperanza_x(self):
        suma = 0
        for ix in range(len(self.matriz_marginal_x[0])-1):
            suma += float(self.matriz_marginal_x[0][ix+1]) * float(self.matriz_marginal_x[1][ix+1])
        self.ex = round(suma,7)    
        return self.ex

    def esperanza_y(self):
        suma = 0
        for iy in range(len(self.matriz_marginal_y[0])-1):
            suma += float(self.matriz_marginal_y[0][iy+1]) * float(self.matriz_marginal_y[1][iy+1])
        self.ey = round(suma,7)
        return self.ey
    
    def esperanza_xx(self):
        suma = 0
        for ix in range(len(self.matriz_marginal_x[0])-1):
            suma += float(self.matriz_marginal_x[0][ix+1]) ** 2 * float(self.matriz_marginal_x[1][ix+1])
        self.exx = round(suma,7)
        return self.exx
    
    def esperanza_yy(self):
        suma = 0
        for iy in range(len(self.matriz_marginal_y[0])-1):
            suma += float(self.matriz_marginal_y[0][iy+1]) ** 2 * float(self.matriz_marginal_y[1][iy+1])
        self.eyy = round(suma,7)
        return self.eyy
    
    def esperanza_xy(self):
        suma = 0
        for ix in range(self.x):
            for iy in range(self.y):
                suma += self.valor(0,iy+1) * self.valor(ix+1,0) * self.valor(ix+1, iy+1)
        self.exy = suma
        return self.exy

    def varianza_x(self):
        self.vx = self.esperanza_xx() - self.esperanza_x() ** 2
        return self.vx
    
    def varianza_y(self):
        self.vy = self.esperanza_yy() - self.esperanza_y() ** 2
        return self.vy
    
    def covarianza_xy(self):
        print(f"{self.esperanza_xy()} - {self.esperanza_x()} * {self.esperanza_y()}")
        self.cxy = self.esperanza_xy() - (self.esperanza_x() * self.esperanza_y())
        return self.cxy
    
    def coef_correlacion(self):
        self.ccxy = self.covarianza_xy() / (math.sqrt(self.varianza_x()) * math.sqrt(self.varianza_y()) )
        return self.ccxy 

    def esperanza_xxyy(self):
        suma = 0
        for ix in range(self.x):
            for iy in range(self.y):
                suma += ((self.valor(0,iy+1) * self.valor(ix+1,0))**2) * self.valor(ix+1, iy+1)
        self.exxyy = suma
        return self.exxyy


    def varianza_xy(self): 
        self.vxy = self.esperanza_xxyy() - (self.esperanza_xy()**2)
        return self.vxy

    def desv_estandar_xy(self): 
        self.dexy = math.sqrt(self.varianza_xy())
        return self.dexy
    
    def varianza_xmasy(self):
        self.vxmasy = self.varianza_x() + self.varianza_y() + 2 * self.covarianza_xy()
        return self.vxmasy
    
    def esperanza_xmasy(self):
        self.exmasy = self.esperanza_x() + self.esperanza_y()
        return self.exmasy


    def __str__(self):
        # Aplicamos la función acomodar a cada elemento de la matriz
        nueva_matriz = [[acomodar(elemento) for elemento in fila] for fila in self.matriz]
        # Construimos una lista de cadenas donde cada cadena es una fila de la matriz
        filas = ['[' + ', '.join(map(str, fila)) + ']' for fila in nueva_matriz]
        # Unimos las filas en una sola cadena con saltos de línea entre ellas
        matriz_str = '[\n' + ',\n'.join(filas) + '\n]'
        return matriz_str
    
    
