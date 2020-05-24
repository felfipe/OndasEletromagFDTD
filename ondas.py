######
## TRABALHO DE ONDAS ELETROMAGNÉTICAS: LINHAS DE TRANSMISSÃO
## Authors:
##  George Alexandre Gantus
##  Renata Oliveira Brito
##  Victor Felipe Domingues do Amaral
## Data: 24/05/2020
######
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy
import math

#definição da função responsavel por animar o gráfico
def animate(n):
    voltage_plot.set_ydata(V[n])
    current_plot.set_ydata(I[n])
    texto_tempo = "tempo t = %.2f uS" % (n*deltaT*1000000)
    label.set_text(texto_tempo)
    return voltage_plot,

#Definição das funções que representam nossos geradores
def fonte_1(t):
    if t < 0:
        return 0
    else:
        return 2
        
def fonte_2(t):
    if t < 0 or t >= l/(10*Vp):
        return 0
    else:
        return 1

Z0 = 50                                         #Impedancia caracteristica da linha de transmissão indicada
Vp = 0.9*3.00E8                                 #Velocidade de propagação
L = Z0/Vp                                       #Indutancia calculada a partir dos dados do problema
C = 1/(Z0*Vp)                                   #Capatância calculada a partir dos dados do problema
l = 1000                                        #tamanho da linha de transmissão
Zg = 75                                         #Impedância interna do Gerador

## Para carga em curto, Zl = 0
## Para carga em aberto, Zl = math.inf
Zl = 0                                       #Impendância da carga
##
kmax = 100                                      #numero de passos em que dividimos o tamanho da linha de tranmissão
Ttotal = 10.5*l/Vp                              #3.70E-5 tempo total da analise
deltaZ = l/kmax                                 #tamanho de cada passo na linha de transmissão
deltaT = deltaZ/Vp*0.5                          #tamanho de cada intervalo de tempo
nmax = int(Ttotal/deltaT)                       #numero de passos em que dividimos o tempo da analise
V = numpy.zeros((nmax,kmax))                    #inicializando a matriz que representa o valor das tensões
I = numpy.zeros((nmax,kmax))                    #inicializando a matriz que representa o valor das correntes
if Zg == math.inf:
    gamaS = math.inf
else:
    gamaS = (Zg - Z0)/(Z0 + Zg)
if Zl == math.inf:
    gamaL = math.inf
else:
    gamaL = (Zl - Z0)/(Z0 + Zl)
#Definição das variaveis para plotar o grafico com um visual mais agradavel

maxTensao = 0                           
minTensao = math.inf                               
maxCorrente = 0                       
minCorrente = math.inf                          

#condições iniciais para o tempo
V[0][0] = Z0*2/(Zg+Z0)                          
I[0][0] = V[0][0]/Z0                            

#Condições para diferentes casos do valor de da impedância interna do gerador  
if Zg == 0:
    betaS = math.inf
elif Zg == math.inf:
    betaS = 0
else:
    betaS = 2*deltaT/(C*Zg*deltaZ)

#Condições para diferentes casos do valor de da impedância da carga
if Zl == 0:
    betaL = math.inf
elif Zl == math.inf:
    betaL = 0
else:
    betaL = 2*deltaT/(C*Zl*deltaZ)
#Loop Que preenche as matrizes de tensão e corrente levando em conta as condições de contorno de cada caso
for n in range (1, nmax):
    ## para mudar a fonte, escolha fonte_1 ou fonte_2 nesta linha
    V[n][0] = (1 - betaS)*V[n-1][0] -2*I[n-1][0] + 2/Zg*fonte_1(n*deltaT)
    if Zl == 0:
        V[n][kmax-1] = 0
    else:
        V[n][kmax-1] = (1 - betaL)*V[n-1][kmax-1] + 2*I[n-1][kmax-1]
    for k in range (1,kmax-1):
        V[n][k] = V[n-1][k] - (I[n-1][k]-I[n-1][k-1])
    for k in range (kmax-1):
        I[n][k] = I[n-1][k] - (deltaT*deltaT)/(L*C*deltaZ*deltaZ)*(V[n][k+1] - V[n][k])#k+1 e k
    I[n][kmax-1] = I[n][kmax-2]


V = V*(deltaT/(C*deltaZ))
figure, (voltage,current) = plt.subplots(2,1)
voltage.grid(True)
current.grid(True)
voltage.set_ylim(-4, 4)
voltage.set_xlim(0, l)
current.set_ylim(-0.1, 0.1)
current.set_xlim(0,l)
voltage_plot, = voltage.plot(numpy.linspace(0,l,kmax), V[0], label ="Tensão [V]", color = 'r')
current_plot, = current.plot(numpy.linspace(0,l,kmax), I[0], label ="Corrente [A]", color = 'g')
voltage.set_ylabel('V(z,t)')
voltage.set_xlabel('z')
current.set_ylabel('I(z,t)')
current.set_xlabel('z')
voltage.legend()
current.legend()
if Zl == math.inf:
    texto_zl = "Zl = inf ohm"
else:    
    texto_zl = "Zl = %.2f ohm" % Zl
label_zl = plt.figtext(0.1, 0.9, texto_zl)
texto_tempo = "tempo t = 0.0 uS"
label = plt.figtext(0.7, 0.9, texto_tempo)
if gamaS == math.inf:
    texto_gamaS = "gamaS = inf"
else:
    texto_gamaS = "gamaS = %.2f" % (gamaS)
if gamaL == math.inf:
    texto_gamaL = "gamaL = inf"
else:
    texto_gamaL = "gamaL = %.2f" % (gamaL)
label_gamaS = plt.figtext(0.30, 0.9, texto_gamaS)
label_gamaL = plt.figtext(0.50, 0.9, texto_gamaL)
voltage.set_autoscale_on(False)
current.set_autoscale_on(False)
animation = animation.FuncAnimation(figure, func = animate, frames=numpy.arange(0, nmax, (int)(kmax/10)), interval = 100, repeat = False) # ajustar kmax/10 para ajustar velocidade
plt.show()
    
