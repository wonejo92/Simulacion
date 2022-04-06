
import random
import matplotlib.pyplot as plt
from collections import Counter

iteraciones_100=[]
iteraciones_1000=[]
iteraciones_10000=[]

def generate_randoms(cantidad, lista):
    for i in range(cantidad):
        dado1=random.randint(1,6)
        dado2=random.randint(1,6)
        lista.append(dado1+dado2)
    return iteraciones_100

def graficar(valores,cantiteraciones):
    numeros = valores.keys()
    cantidad = valores.values()
    plt.bar(numeros, cantidad, color='green')
    plt.title(f"Grafico de barras con {str(cantiteraciones)} Iteraciones")
    plt.xlabel("Sumatorias")
    plt.ylabel("Cantidades")
    plt.show()

generate_randoms(100,iteraciones_100)
generate_randoms(1000,iteraciones_1000)
generate_randoms(10000,iteraciones_10000)

cout100=Counter(iteraciones_100)
cout1000=Counter(iteraciones_1000)
cout10000=Counter(iteraciones_10000)

graficar(cout100,100)
graficar(cout1000,1000)
graficar(cout10000,10000)

