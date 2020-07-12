# coding: utf-8
import numpy
import math
from scipy import constants
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits import mplot3d

##### CONSTANTS #####
c = constants.speed_of_light      # VELOCIDADE DA LUZ
u = 4*math.pi*10**(-7)            # PERMEABILIDADE
e = 1/(u*(c**2))                  # PERMISSIVIDADE

##### FUNCTIONS #####


def sin_source(n, freq):
    return math.sin(freq*n)


def step_source(n):
    if n >= 0:
        return 1
    else:
        return 0


def impulse_source(n):
    if(n == 2):
        return 1
    else:
        return 0


def fdtd_2d(delta, deltaT, nmax, imax, jmax, sigma, sigma_estrela, source):
    print("Calculando...")
    Ez = numpy.zeros((nmax, imax, jmax))
    Hx = numpy.zeros((nmax, imax, jmax))
    Hy = numpy.zeros((nmax, imax, jmax))
    Ca = (1 - sigma*deltaT/(2*e))/(1 + sigma*deltaT/(2*e))
    Cb = (deltaT/(e*delta))/(1+sigma*deltaT/(2*e))
    Da = (1 - sigma_estrela*deltaT/(2*u))/(1 + sigma_estrela*deltaT/(2*u))
    Db = (deltaT/(u*delta))/(1 + sigma_estrela*deltaT/(2*u))
    for n in range(1, nmax-1):
        for i in range(1, imax-1):
            for j in range(1, jmax-1):
                Hx[n][i][j] = Da*Hx[n-1][i][j] + Db * \
                    (Ez[n-1][i][j] - Ez[n-1][i][j+1])
                Hy[n][i][j] = Da*Hy[n-1][i][j] + Db * \
                    (Ez[n-1][i+1][j] - Ez[n-1][i][j])
                Ez[n][i][j] = Ca*Ez[n-1][i][j] + Cb * \
                    (Hy[n][i][j] - Hy[n][i-1][j] + Hx[n][i][j-1] - Hx[n][i][j])
            Ez[n][i][jmax-1] = 0
            Ez[n][i][0] = 0
        Ez[n][int(imax/2)][int(jmax/2)] = source(n)
    return Ez, Hx, Hy


def fdtd_1d(delta, deltaT, nmax, imax, sigma, sigma_estrela, source):
    Ez = numpy.zeros((nmax, imax))
    Hy = numpy.zeros((nmax, imax))
    Ca = (1 - sigma*deltaT/(2*e))/(1 + sigma*deltaT/(2*e))
    Cb = (deltaT/(e*delta))/(1+sigma*deltaT/(2*e))
    Da = (1 - sigma_estrela*deltaT/(2*u))/(1 + sigma_estrela*deltaT/(2*u))
    Db = (deltaT/(u*delta))/(1 + sigma_estrela*deltaT/(2*u))
    print(Da)
    for n in range(nmax):
        Ez[n][0] = source(n)
    for n in range(1, nmax):
        for i in range(1, imax-1):
            Hy[n][i] = Da*Hy[n-1][i] + Db*(Ez[n-1][i+1] - Ez[n-1][i])
            Ez[n][i] = Ca*Ez[n-1][i] + Cb*(Hy[n][i] - Hy[n][i-1])
        Ez[n][1] = source(n)
        Ez[n][imax-2] = 0
        # Hy[n][imax-2] = 0 # PARA O EXERCÍCIO 3.4
    return Ez, Hy


def plot_wave(U, nmax, imax, delta):
    def animate(n):
        U_plot1.set_ydata(U[n])
        return U_plot,

    figure, U_plot = plt.subplots()
    U_plot.grid(True)
    U_plot.set_ylim(-1, 1)  # -0.03, 0.03 para Hy
    U_plot.set_xlabel("coordenada na malha i")
    U_plot.set_ylabel("função de onda Ez(x,t)")
    U_plot1, = U_plot.plot(numpy.linspace(0, imax, imax), U[0], 'r')
    animation1 = animation.FuncAnimation(figure, func=animate, frames=numpy.arange(0, nmax, (int)(
        imax/50)), interval=100, repeat=False)  # ajustar kmax/50 para ajustar velocidade
    plt.show()


def plot_3D(U, nmax, imax, jmax, delta):
    def animate(n, Ez, plot):
        plot[0].remove()
        plot[0] = ax.plot_surface(
            X, Y, U[n], rstride=5, cstride=5, cmap=cm.magma)
        return ax,
    x = numpy.linspace(0, delta*(imax), imax)
    y = numpy.linspace(0, delta*(jmax), jmax)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X, Y = numpy.meshgrid(x, y)
    ax.set_zlim(-1.0, 1.0)
    plot = [ax.plot_surface(X, Y, U[0], rstride=5, cstride=5, cmap=cm.magma)]
    animation1 = animation.FuncAnimation(fig, func=animate, frames=numpy.arange(0, nmax, (int)(
        nmax/100)), fargs=(U, plot), interval=100, repeat=False)  # ajustar kmax/10 para ajustar velocidade
    plt.show()


def ex_3_3():
    nmax = 600
    imax = 301
    delta = 1
    deltaT = delta/c
    sigma = 0
    sigma_estrela = 0
    def source(n): return sin_source(n, freq=4*(2*math.pi/nmax))
    Ez, Hy = fdtd_1d(delta, deltaT, nmax, imax, sigma, sigma_estrela, source)
    # plot_wave(Ez, nmax, imax, delta)
    plot_wave(Ez, nmax, imax, delta)


def ex_3_5():
    nmax = 600
    imax = 301
    delta = 1
    deltaT = 0.99*delta/c
    sigma = 0
    sigma_estrela = 0
    def source(n): return sin_source(n, freq=4*(2*math.pi/nmax))
    Ez, Hy = fdtd_1d(delta, deltaT, nmax, imax, sigma, sigma_estrela, source)
    # plot_wave(Ez, nmax, imax, delta)
    plot_wave(Ez, nmax, imax, delta)


def ex_3_6():
    nmax = 600
    imax = 301
    delta = 1
    deltaT = 1.01*delta/c
    sigma = 0
    sigma_estrela = 0
    def source(n): return sin_source(n, freq=4*(2*math.pi/nmax))
    Ez, Hy = fdtd_1d(delta, deltaT, nmax, imax, sigma, sigma_estrela, source)
    # plot_wave(Ez, nmax, imax, delta)
    plot_wave(Ez, nmax, imax, delta)


def ex_3_7():
    nmax = 100
    imax = 100
    jmax = 100
    delta = 1
    deltaT = 1.0*delta/(c*math.sqrt(2))
    sigma = 0               # CONDUTIVIDADE ElÉTRICA
    sigma_estrela = 0       # PERDA MAGNÉTICA

    def source(n): return sin_source(
        n, freq=4*(2*math.pi/nmax))  # 4 ciclos ao tempo total
    # step_source(n)
    # impulse_source(n)
    Ez, Hx, Hy = fdtd_2d(delta, deltaT, nmax, imax, jmax,
                         sigma, sigma_estrela, source)
    plot_3D(Ez, nmax, imax, jmax, delta)


def ex_3_8():
    nmax = 100
    imax = 100
    jmax = 100
    delta = 1
    deltaT = 1.0*delta/(c*math.sqrt(2))
    sigma = 5.0E-4              # ORDEM de sigma 10^-4
    sigma_estrela = 0

    def source(n): return sin_source(
        n, freq=4*(2*math.pi/nmax))  # 4 ciclos ao tempo total
    # step_source(n)
    # impulse_source(n)
    Ez, Hx, Hy = fdtd_2d(delta, deltaT, nmax, imax, jmax,
                         sigma, sigma_estrela, source)
    plot_3D(Ez, nmax, imax, jmax, delta)


def ex_3_9():
    nmax = 100
    imax = 100
    jmax = 100
    delta = 1
    deltaT = 1.0005*delta/(c*math.sqrt(2))
    sigma = 0               # CONDUTIVIDADE ElÉTRICA
    sigma_estrela = 0       # PERDA MAGNÉTICA

    def source(n): return sin_source(
        n, freq=4*(2*math.pi/nmax))  # 4 ciclos ao tempo total
    # step_source(n)
    # impulse_source(n)
    Ez, Hx, Hy = fdtd_2d(delta, deltaT, nmax, imax, jmax,
                         sigma, sigma_estrela, source)
    plot_3D(Ez, nmax, imax, jmax, delta)


ex_3_9()
