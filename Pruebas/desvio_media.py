import math

print("Muestral: ")

numeros = "10.2 9.7 10.1 10.3 10.1 9.8 9.9 10.4 10.3 9.8"

lista_numeros = numeros.split()

lista_numeros = [float(numero) for numero in lista_numeros]

n = len(lista_numeros)

media = sum(lista_numeros)/len(lista_numeros)

sumatoria = 0

for i in lista_numeros:
    sumatoria += (i - media)**2

ss = sumatoria / (n-1)

print("n" , n)
print("s" , math.sqrt(ss))
print("s^2" , ss)
print("media", media)