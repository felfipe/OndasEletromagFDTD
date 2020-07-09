import matplotlib.pyplot as plt
import math
import numpy
import matplotlib.animation as animation
##### FONTES #####
def gauss_source(t): # EX 2.8
    return math.exp(-((t*S -40)**2)/200)

def step_source(t):  # EX 2.7
    if t >=0 and t <= 40:
        return 1
    else:
        return 0




def animate(n):
    U_plot1.set_ydata(U[n])
    return U_plot,

#### VARIÁVEIS ####
S = 0.5
kmax = 200
nmax = int(kmax/S)
U = numpy.zeros((nmax,kmax))

##### FDTD #####
U[0,0] = step_source(0)
for i in range(1,nmax-2):
    U[i][0] = step_source(i)    
    for k in range(1,kmax-2):
        U[i+1][k] = S**2*(U[i][k+1] -2*U[i][k] + U[i][k-1]) +2*U[i][k] - U[i-1][k]

##### GRÁFICO #####
figure, (U_plot) = plt.subplots(1,1)
U_plot.grid(True)
U_plot.set_ylim(-2,2)
U_plot.set_xlabel("coordenada na malha i")
U_plot.set_ylabel("função de onda u(x,t)")
U_plot1, = U_plot.plot(numpy.linspace(0,kmax-2,kmax),U[0],'r')
animation = animation.FuncAnimation(figure, func = animate, frames=numpy.arange(0, nmax, (int)(kmax/50)), interval = 100, repeat = False) # ajustar kmax/10 para ajustar velocidade
plt.show()