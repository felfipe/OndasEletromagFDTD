import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy
import math

def animate(n):
    voltage_plot.set_ydata(V[n])
    current_plot.set_ydata(I[n])
    return voltage_plot,
Z0 = 50
Vp = 0.9*3.00E8
L = Z0/Vp
C = 1/(Z0*Vp)
l = 10

Vg = 2
Zg = 75
Zl = 50
kmax = 100
Ttotal = 10.5*l/Vp#3.70E-5
deltaZ = l/kmax#Respeita a condição de estabilidade
deltaT = deltaZ/Vp*0.7
nmax = int(Ttotal/deltaT)
V = numpy.zeros((nmax,kmax))
I = numpy.zeros((nmax,kmax))
'''
c1 = -(2*deltaT/(deltaT*deltaZ*R+2*deltaZ*L))
c2 = (2*L-deltaT*R)/(2*L+deltaT*R)
c3 = -(2*deltaT)/(deltaT*deltaZ*G+2*deltaZ*C)
c4 = (2*C-deltaT*G)/(2*C-deltaT*G)
'''

# condições iniciais para o tempo
V[0][0] = Z0*2/(Zg+Z0)
I[0][0] = V[0][0]/Z0
gamaS = 2*deltaT/(Zg*C*deltaZ)
if Zl == 0:
    gamaL = math.inf
elif Zl == math.inf:
    gamaL = 0
else:
    gamaL = 2*deltaT/(C*Zl*deltaZ)
print(Vp)
print(deltaZ/Vp)
print(nmax)



for n in range (1, nmax):
    V[n][0] = (1- gamaS)*V[n-1][0] -2*I[n-1][0] + 2/Zg*2 # fonte 2
    if Zl == 0:
        V[n][kmax-1] = 0
    else:
        V[n][kmax-1] =(1 - gamaL)*V[n-1][kmax-1] + 2*I[n-1][kmax-2]
    for k in range (1,kmax-1):
        V[n][k] = V[n-1][k] - (I[n-1][k]-I[n-1][k-1])
    for k in range (0, kmax-1):
        I[n][k] = I[n-1][k] - (deltaT*deltaT)/(L*C*deltaZ*deltaZ)*(V[n][k+1] - V[n][k])#k+1 e k

V = V*(deltaT/(C*deltaZ))
figure, (voltage,current) = plt.subplots(2,1)
voltage.grid(True)
current.grid(True)

voltage_plot, = voltage.plot(numpy.linspace(0,l,kmax), V[0])
current_plot, = current.plot(numpy.linspace(0,l,kmax), I[0])

animation = animation.FuncAnimation(figure, func = animate, frames=numpy.arange(0, nmax, (int)(kmax/100)), interval = 100, repeat = False)
plt.show()
    
