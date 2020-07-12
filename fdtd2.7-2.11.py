# coding: utf-8
import matplotlib.pyplot as plt
import math
import numpy
import matplotlib.animation as animation


##### SOURCES #####
def gauss_source(t, S):  # EX 2.8
    return math.exp(-((t*S - 40)**2)/200)


def step_source(t):  # EX 2.7
    if t >= 0 and t <= 40:
        return 1
    else:
        return 0

# FUNCTIONS TO PLOT WAVES ANIMATED


def plot_1_wave(U, nmax, kmax):
    def animate(n):
        U_plot1.set_ydata(U[n])
        return U_plot,
    figure, U_plot = plt.subplots()
    U_plot.grid(True)
    U_plot.set_ylim(-1.2, 1.2)
    U_plot.set_xlabel("coordenada na malha i")
    U_plot.set_ylabel("função de onda u(x,t)")
    U_plot1, = U_plot.plot(numpy.linspace(0, kmax-2, kmax), U[0], 'r')
    animation1 = animation.FuncAnimation(figure, func=animate, frames=numpy.arange(0, nmax, (int)(
        kmax/100)), interval=100, repeat=False)  # ajustar kmax/50 para ajustar velocidade
    plt.show()


def plot_2_waves(U1, U2, nmax, kmax):
    def animate(n):
        U_plot1.set_ydata(U1[n])
        U_plot2.set_ydata(U2[n])
        return U_plot,
    figure, U_plot = plt.subplots()
    U_plot.grid(True)
    U_plot.set_ylim(-2, 2)
    U_plot.set_xlabel("coordenada na malha i")
    U_plot.set_ylabel("função de onda u(x,t)")
    U_plot1, = U_plot.plot(numpy.linspace(0, kmax-2, kmax), U1[0], 'r')
    U_plot2, = U_plot.plot(numpy.linspace(0, kmax-2, kmax), U2[0], 'g--')
    animation1 = animation.FuncAnimation(figure, func=animate, frames=numpy.arange(0, nmax, (int)(
        kmax/100)), interval=100, repeat=False)  # ajustar kmax/50 para ajustar velocidade
    plt.show()


def plot_3_waves(U1, U2, U3, nmax, kmax):
    def animate(n):
        U_plot1.set_ydata(U1[n])
        U_plot2.set_ydata(U2[n])
        U_plot3.set_ydata(U3[n])
        return U_plot,
    figure, U_plot = plt.subplots()
    U_plot.grid(True)
    U_plot.set_ylim(-1, 1)
    U_plot.set_xlabel("coordenada na malha i")
    U_plot.set_ylabel("função de onda u(x,t)")
    U_plot1, = U_plot.plot(numpy.linspace(0, kmax-2, kmax), U1[0], 'r')
    U_plot2, = U_plot.plot(numpy.linspace(0, kmax-2, kmax), U2[0], 'g')
    U_plot3, = U_plot.plot(numpy.linspace(0, kmax-2, kmax), U3[0], 'b--')
    animation1 = animation.FuncAnimation(figure, func=animate, frames=numpy.arange(0, nmax, (int)(
        kmax/100)), interval=100, repeat=False)  # ajustar kmax/50 para ajustar velocidade
    plt.show()


##### FDTD #####
def fdtd(S, source, nmax, kmax):
    U = numpy.zeros((nmax, kmax))
    for i in range(1, nmax-1):
        U[i][0] = source(i)     # condição inicial
        for k in range(1, kmax-1):
            U[i+1][k] = S(k)**2*(U[i][k+1] - 2*U[i][k] +
                                 U[i][k-1]) + 2*U[i][k] - U[i-1][k]
    return U


def fig_2_3a():

    def S1(i): return 0.99
    def S2(i): return 1.0
    kmax = 200
    nmax1 = int(kmax/S1(0))
    nmax2 = int(kmax/S2(0))
    def source(i): return step_source(i)
    U1 = fdtd(S1, source, nmax1, kmax)
    U2 = fdtd(S2, source, nmax2, kmax)
    plot_2_waves(U1, U2, nmax2, kmax)


def fig_2_3b():
    def S1(i): return 0.5
    def S2(i): return 1.0
    kmax = 200
    nmax1 = int(kmax/S1(0))
    nmax2 = int(kmax/S2(0))
    def source(i): return step_source(i)
    U1 = fdtd(S1, source, nmax1, kmax)
    U2 = fdtd(S2, source, nmax2, kmax)
    plot_2_waves(U1, U2, nmax2, kmax)


def fig_2_4a():
    kmax = 200
    def S1(i): return 0.99
    def S2(i): return 1.0
    nmax1 = int(kmax/S1(0))
    nmax2 = int(kmax/S2(0))
    def source1(i): return gauss_source(i, S1(0))  # GAUSS SOURCE
    def source2(i): return gauss_source(i, S2(0))
    U1 = fdtd(S1, source1, nmax1, kmax)
    U2 = fdtd(S2, source2, nmax2, kmax)
    plot_2_waves(U1, U2, nmax2, kmax)


def fig_2_4b():
    kmax = 200
    def S1(i): return 0.5
    def S2(i): return 1.0
    nmax1 = int(kmax/S1(0))
    nmax2 = int(kmax/S2(0))
    def source1(i): return gauss_source(i, S1(0))
    def source2(i): return gauss_source(i, S2(0))
    U1 = fdtd(S1, source1, nmax1, kmax)
    U2 = fdtd(S2, source2, nmax2, kmax)
    plot_2_waves(U1, U2, nmax2, kmax)


def fig_2_5():

    def S(i): return 1.0 if i < 140 else 0.25
    kmax = 200
    nmax = 240
    def source(i): return gauss_source(i, S(0))
    U = fdtd(S, source, nmax, kmax)
    plot_1_wave(U, nmax, kmax)


def fig_2_6a():
    kmax = 220
    nmax = 221
    def S(i): return 1.0005

    def source(i):
        if i > 120:
            return 0
        else:
            return math.exp(-(((i - 60)/20)**2))
    U = fdtd(S, source, nmax, kmax)
    figure, U_plot = plt.subplots()
    U_plot.grid(True)
    U_plot.set_ylim(-1, 1)
    U_plot.set_xlabel("coordenada na malha i")
    U_plot.set_ylabel("função de onda u(x,t)")
    U_plot1, = U_plot.plot(numpy.linspace(
        1, kmax, kmax), U[200], 'r', label='n = 200')
    U_plot1, = U_plot.plot(numpy.linspace(1, kmax, kmax),
                           U[210], 'r--', label='n = 210')
    U_plot1, = U_plot.plot(numpy.linspace(1, kmax, kmax),
                           U[220], 'b--', label='n = 220')
    plt.legend()
    plt.show()


def fig_2_6b():
    kmax = 220
    nmax = 221
    def S(i): return 1.0005

    def source(i):
        if i > 120:
            return 0
        else:
            return math.exp(-(((i - 60)/20)**2))
    U = fdtd(S, source, nmax, kmax)

    # PLOT
    figure, U_plot = plt.subplots()
    U_plot.grid(True)
    U_plot.set_ylim(-0.08, 0.08)
    U_plot.set_xlim(1, 20)
    U_plot.set_xlabel("coordenada na malha i")
    U_plot.set_ylabel("função de onda u(x,t)")
    U_plot1, = U_plot.plot(numpy.linspace(
        0, kmax, kmax), U[200], 'r', label='n = 200')
    U_plot2, = U_plot.plot(numpy.linspace(
        0, kmax, kmax), U[210], 'g', label='n = 210')
    U_plot3, = U_plot.plot(numpy.linspace(0, kmax, kmax),
                           U[220], 'b--', label='n = 220')
    plt.legend()
    plt.show()


def fig_2_7a():
    kmax = 220
    nmax = 220
    def S(i): return 1.075 if i == 90 else 1.0

    def source(i):
        if i > 74:
            return 0
        else:
            return math.exp(-(((i - 60)/5)**2))
    U = fdtd(S, source, nmax, kmax)
    # PLOT
    figure, U_plot = plt.subplots()
    U_plot.grid(True)
    U_plot.set_ylim(-1, 1)
    U_plot.set_xlim(1, 160)
    U_plot.set_xlabel("coordenada na malha i")
    U_plot.set_ylabel("função de onda u(x,t)")
    U_plot1, = U_plot.plot(numpy.linspace(
        0, kmax-1, kmax), U[191], 'r', label='n = 190')
    U_plot2, = U_plot.plot(numpy.linspace(
        0, kmax-1, kmax), U[201], 'g--', label='n = 200')
    plt.legend()
    plt.show()


def fig_2_7b():
    kmax = 220
    nmax = 220
    def S(i): return 1.075 if i == 90 else 1.0

    def source(i):
        if i > 74:
            return 0
        else:
            return math.exp(-(((i - 60)/5)**2))
    U = fdtd(S, source, nmax, kmax)

    # PLOT
    figure, U_plot = plt.subplots()
    U_plot.grid(True)
    U_plot.set_ylim(-1, 1)
    U_plot.set_xlim(70, 110)
    U_plot.set_xlabel("coordenada na malha i")
    U_plot.set_ylabel("função de onda u(x,t)")
    U_plot1, = U_plot.plot(numpy.linspace(
        0, kmax-1, kmax), U[191], 'r', label='n = 190')
    U_plot2, = U_plot.plot(numpy.linspace(
        0, kmax-1, kmax), U[201], 'g--', label='n = 200')
    plt.legend()
    plt.show()


fig_2_7b()
