import numpy
import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def animate(n):
    ax.set_ydata(Ez[n])
    return U_plot,
def J_source(i):
    if i >= 0:
        return 1
    else:
        return 0
def M_source(i):
    return 1
c = 3.0E8
delta = 1.5*10**3
deltaX = deltaY = delta
deltaT = delta/(c*math.sqrt(2))
nmax = 100
imax = 100
jmax = 100
Ez = numpy.zeros((nmax,imax,jmax))
Hx = numpy.zeros((nmax,imax,jmax))
Hy = numpy.zeros((nmax,imax,jmax))
ro = 0
ro_estrela = 0
u = 4*math.pi*10**(-7)
e = 1/(u*(c**2))
Ca = (1 - ro*deltaT/(2*e))/(1 + ro*deltaT/(2*e))
Cb = (deltaT/(e*delta))/(1+ro*deltaT/(2*e))
Da = (1 - ro_estrela*deltaT/(2*u))/(1 + ro_estrela*deltaT/(2*u))
Db = (deltaT/(u*delta))/(1 + ro_estrela*deltaT/(2*u))
### FDTD
for i in range(0,nmax):
    Ez[i][int(imax/2)][int(jmax/2)] = J_source(i)


for n in range(2,nmax):
    for i in range(2,imax-2):
        for j in range(2,jmax-2): 
            Ez[n][i][j] = Ca*Ez[n-1][i][j] + Cb*(Hy[n-1][i][j] - Hy[n-1][i-1][j] + Hx[n-1][i][j-1] - Hx[n-1][i][j])
    for i in range(2,imax-2):
        for j in range(2,jmax-2):        
            Hx[n][i][j] = Da*Hx[n-1][i][j] + Db*(Ez[n][i][j] - Ez[n][i][j+1])
            
    for i in range(2,imax-2):
        for j in range(2,jmax-2):
            Hy[n][i][j] = Da*Hy[n-1][i][j] + Db*(Ez[n][i+1][j] - Ez[n][i][j])
            
            



x = numpy.linspace(0,delta*(imax), imax)
y = numpy.linspace(0,delta*(jmax), jmax)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y = numpy.meshgrid(x,y)
ax.plot_wireframe(X,Y,Ez[50], rstride=5,cstride=5)
plt.show()
animation = animation.FuncAnimation(figure, func = animate, frames=numpy.arange(0, nmax, (int)(kmax/50)), interval = 100, repeat = False) # ajustar kmax/10 para ajustar velocidade
#line = ax.plot3D(x,y,)
