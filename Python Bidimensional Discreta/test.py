
from bidimensional import Matriz

def prueba(a: Matriz):
    print(a)
    print("Matriz marginal x ", a.marginal_x())
    print("Matriz marginal y ", a.marginal_y())
    print("Esperanza x ", a.esperanza_x())
    print("Esperanza y ", a.esperanza_y())
    print("Esperanza x^2 ", a.esperanza_xx())
    print("Esperanza y^2 ", a.esperanza_yy())
    print("Esperanza xy ", a.esperanza_xy())
    print("Covarianza xy ", a.covarianza_xy())
    print("Varianza x ", a.varianza_x())
    print("Varianza y ", a.varianza_y())
    print("Coeficiente de correlación: ", a.coef_correlacion())
    print("Esperanza (xy)^2 : ", a.esperanza_xxyy())
    print("Varianza xy : ", a.varianza_xy())
    print("Desvío estándar xy : ", a.desv_estandar_xy())
    print("Varianza X + Y : ", a.varianza_xmasy())
    print("Esperanza X + Y : ", a.esperanza_xmasy())

m_matriz_1 =  [["x/y",1,2,3],
              [1,0.15,0.1,0.1],
              [2,0.1,0.2,0.15],
              [3,0.05,0.05,0.1]]

m_matriz_2 = [["x/y",129,130,131],
              [15,0.12,0.42,0.06],
              [16,0.08,0.28,0.04]]

m_matriz_3= [["x/y",0,1,2,3],
             [0,0.08,0.07,0.04,0.01],
             [1,0.06,0.15,0.05,0.06],
             [2,0.05,0.04,0.10,0.08],
             [3,0.00,0.04,0.09,0.08]]
m_matriz_4 = [["x/y", 0, 1 ,2, 3],
              [0, 0.12, 0.06,0.045, 0.075],
              [1, 0.1, 0.05, 0.0375, 0.0625],
              [2, 0.1, 0.05, 0.0375, 0.0625],
              [3, 0.08, 0.04, 0.03, 0.05]]

matriz_1 = Matriz(3,3, m_matriz_1)
matriz_2 = Matriz(2,3, m_matriz_2)
matriz_3 = Matriz(4, 4, m_matriz_3)



matriz_4 = Matriz(4,4,m_matriz_4)

prueba(matriz_4)