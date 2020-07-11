import numpy
import matplotlib.pyplot as plt
import math




def figura_2_1(S, n):
    
    fig, ax1 = plt.subplots();
    ax1.plot(N, atenuacao,'g',label = 'Atenuação')
    ax2 = ax1.twinx()
    ax2.plot(N, Vp,'b', label = 'Velocidade de fase numérica')
    ax2.set_ylabel('Velocidade de fase numérica (Vp/c)')
    ax2.set_ylim(0, 2)
    ax1.set_ylabel('Atenuação constante')
    ax1.set_ylim(0, 6)
    plt.xlim(1,10)
    plt.show()

def figura_2_2(S,n):
    N = numpy.linspace(3, 80, num = n)
    Vp = numpy.zeros(n)
    for i in range(n):
        tau = 1 + 1/(S**2)*(math.cos(2*math.pi*S/N[i])-1)
        k = math.acos(tau)
        Vp[i] = 2*math.pi/(N[i]*k)
    Vp = 100*(1 - Vp) # calcula erro percentual    
    plt.plot(N,Vp,'r', label = 'S = ')
    plt.xlabel('Densidade de amostras N')
    plt.ylabel('Erro percentual da Velocidade de fase')
    plt.yscale('log')
    plt.show()
#figura_2_1(1/2,1000)
figura_2_2(1/math.sqrt(2),1000)