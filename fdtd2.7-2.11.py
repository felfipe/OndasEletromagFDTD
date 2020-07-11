import matplotlib.pyplot as plt
import math
import numpy
import matplotlib.animation as animation


##### SOURCES #####
def gauss_source(t, S): # EX 2.8
    return math.exp(-((t*S -40)**2)/200)

def step_source(t):  # EX 2.7
    if t >=0 and t <= 40:
        return 1
    else:
        return 0

#### FUNCTION TO PLOT WAVES ANIMATED
def plot_1_wave(U, nmax, kmax):
    def animate(n):
        U_plot1.set_ydata(U[n])
        return U_plot,
    figure, U_plot = plt.subplots()
    U_plot.grid(True)
    U_plot.set_ylim(-4,4)
    U_plot.set_xlabel("coordenada na malha i")
    U_plot.set_ylabel("função de onda u(x,t)")
    U_plot1, = U_plot.plot(numpy.linspace(0,kmax-2,kmax),U[0],'r')
    animation1 = animation.FuncAnimation(figure, func = animate, frames=numpy.arange(0, nmax, (int)(kmax/100)), interval = 100, repeat = False) # ajustar kmax/50 para ajustar velocidade
    plt.show()

def plot_2_waves(U1, U2, nmax, kmax):
    def animate(n):
        U_plot1.set_ydata(U1[n])
        U_plot2.set_ydata(U2[n])
        return U_plot,
    figure, U_plot = plt.subplots()
    U_plot.grid(True)
    U_plot.set_ylim(-2,2)
    U_plot.set_xlabel("coordenada na malha i")
    U_plot.set_ylabel("função de onda u(x,t)")
    U_plot1, = U_plot.plot(numpy.linspace(0,kmax-2,kmax),U1[0],'r')
    U_plot2, = U_plot.plot(numpy.linspace(0,kmax-2,kmax),U2[0],'g--')
    animation1 = animation.FuncAnimation(figure, func = animate, frames=numpy.arange(0, nmax, (int)(kmax/100)), interval = 100, repeat = False) # ajustar kmax/50 para ajustar velocidade
    plt.show()

def plot_3_waves(U1, U2, U3, nmax, kmax):
    def animate(n):
        U_plot1.set_ydata(U1[n])
        U_plot2.set_ydata(U2[n])
        U_plot3.set_ydata(U3[n])
        return U_plot,
    figure, U_plot = plt.subplots()
    U_plot.grid(True)
    U_plot.set_ylim(-1,1)
    U_plot.set_xlabel("coordenada na malha i")
    U_plot.set_ylabel("função de onda u(x,t)")
    U_plot1, = U_plot.plot(numpy.linspace(0,kmax-2,kmax),U1[0],'r')
    U_plot2, = U_plot.plot(numpy.linspace(0,kmax-2,kmax),U2[0],'g')
    U_plot3, = U_plot.plot(numpy.linspace(0,kmax-2,kmax),U3[0],'b--')
    animation1 = animation.FuncAnimation(figure, func = animate, frames=numpy.arange(0, nmax, (int)(kmax/100)), interval = 100, repeat = False) # ajustar kmax/50 para ajustar velocidade
    plt.show()


##### FDTD #####
def fdtd(S, source,nmax,kmax):
    U = numpy.zeros((nmax,kmax))
    U[0,0] = source(0) 
    for i in range(1,nmax-1):
        U[i][0] = source(i)
        for k in range(1,kmax-1):
            U[i+1][k] = S(i)**2*(U[i][k+1] -2*U[i][k] + U[i][k-1]) +2*U[i][k] - U[i-1][k]
    return U




def fig_2_3a():
    
    S1 = lambda i: 0.99
    S2 = lambda i: 1.0
    kmax = 200
    nmax1 = int(kmax/S1(0))
    nmax2 = int(kmax/S2(0))
    source = lambda i: step_source(i)
    U1 = fdtd(S1,source,nmax1,kmax)
    U2 = fdtd(S2,source,nmax2,kmax)
    plot_2_waves(U1,U2,nmax2,kmax)

def fig_2_3b():
    S1 = lambda i: 0.5
    S2 = lambda i: 1.0
    kmax = 200
    nmax1 = int(kmax/S1(0))
    nmax2 = int(kmax/S2(0))
    source = lambda i: step_source(i)
    U1 = fdtd(S1,source,nmax1,kmax)
    U2 = fdtd(S2,source,nmax2,kmax)
    plot_2_waves(U1,U2, nmax2, kmax)

def fig_2_4a():
    kmax = 200
    S1 = lambda i: 0.99
    S2 = lambda i: 1.0
    nmax1 = int(kmax/S1(0))
    nmax2 = int(kmax/S2(0))
    source1 = lambda i: gauss_source(i,S1(0)) ## GAUSS SOURCE
    source2 = lambda i: gauss_source(i,S2(0))
    U1 = fdtd(S1,source1,nmax1,kmax)
    U2 = fdtd(S2,source2,nmax2,kmax)
    plot_2_waves(U1,U2, nmax2, kmax)

def fig_2_4b():
    kmax = 200
    S1 = lambda i: 0.5
    S2 = lambda i: 1.0
    nmax1 = int(kmax/S1(0))
    nmax2 = int(kmax/S2(0))
    source1 = lambda i: gauss_source(i,S1(0))
    source2 = lambda i: gauss_source(i,S2(0))
    U1 = fdtd(S1,source1,nmax1,kmax)
    U2 = fdtd(S2,source2,nmax2,kmax)
    plot_2_waves(U1,U2, nmax2, kmax)

def fig_2_5():
    
    S = lambda i: 1 if i < 140 else 0.25
    kmax = 200
    nmax = 400
    source = lambda i: gauss_source(i,S(0))
    U = fdtd(S,source,nmax,kmax)
    plot_1_wave(U, nmax, kmax)

def fig_2_6a():
    kmax = 220
    S = lambda i: 1.0005
    source = lambda i: gauss_source(i,S(0))
    U1 = fdtd(S,source,200,kmax)
    U2 = fdtd(S,source,210,kmax)
    U3 = fdtd(S,source,220,kmax)
    plot_3_waves(U1,U2,U3,200,kmax)

def fig_2_6b():
    kmax = 220
    S = lambda i: 1.0005
    source = lambda i: gauss_source(i,S(0))
    U1 = fdtd(S,source,200,kmax)
    U2 = fdtd(S,source,210,kmax)
    U3 = fdtd(S,source,220,kmax)

    figure, U_plot = plt.subplots()
    U_plot.grid(True)
    U_plot.set_ylim(-0.05,0.05)
    U_plot.set_xlim(1,20)
    U_plot.set_xlabel("coordenada na malha i")
    U_plot.set_ylabel("função de onda u(x,t)")
    U_plot1, = U_plot.plot(numpy.linspace(0,kmax-2,kmax),U1[199],'r')
    U_plot2, = U_plot.plot(numpy.linspace(0,kmax-2,kmax),U2[199],'g')
    U_plot3, = U_plot.plot(numpy.linspace(0,kmax-2,kmax),U3[199],'b--')
    plt.show()

def fig_2_7():
    S = lambda i: 1.075 if i == 90 else 1.0
    source = lambda i: gauss_source(i,S(0))
    kmax = 220
    nmax1 = 190
    nmax2 = 200
    U1 = fdtd(S,source,nmax1,kmax)
    U2 = fdtd(S,source,nmax2,kmax)
    plot_2_waves(U1,U2,nmax1,kmax)

fig_2_7()