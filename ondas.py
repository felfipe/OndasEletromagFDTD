import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

R = 0#Linha sem perdas
G = 0#Linha sem perdas
Vp = 0.9*3.00E8
L = 1.85E-7
C = 7.41E-11
l = 1000
Z0 = 50
Vg = 2
Zg = 75
Zl = 100
nmax = 1000
kmax = 100
Ttotal = 10*l/Vp#3.70E-5
deltaT = Ttotal/nmax
deltaZ = l/kmax#Respeita a condição de estabilidade
V = numpy.zeros((nmax,kmax), int)
I = numpy.zeros((nmax,kmax), int)
'''
c1 = -(2*deltaT/(deltaT*deltaZ*R+2*deltaZ*L))
c2 = (2*L-deltaT*R)/(2*L+deltaT*R)
c3 = -(2*deltaT)/(deltaT*deltaZ*G+2*deltaZ*C)
c4 = (2*C-deltaT*G)/(2*C-deltaT*G)
'''

# condições iniciais para o tempo
V[0][0] = (Z0/(Zg + Z0)*Vg)
I[0][0] = (Vg/(Zg+Z0))



'''

A primeira corrente que calculamos é a corrente no tempo 1/2 para diferentes valores de k
para isso precisamos da corrente no tempo -1/2(que devemos inserir no vetor i0) e da tensão
no tempo 0 para qualquer ponto da LT.
A primeira tensão que calculamos é a tensão no tempo 1 para diferentes valores de k
para isso precisamos da tensão no tempo 0(que devemos inserir no vetor v0) e da corrente no tempo
1/2(calculada no passo anterior) para qualquer ponto da LT
 '''
for n in range (1, nmax):
    I[n][0] = c1*(v[n][k] - v[n][k])+c2*i[n][k]
    for k in range (1, kmax):
        I[n][k] = I[n-1][k] - deltaT/(L*deltaZ)*(V[n-1][k] - V[n-1][k-1])
    for k in range (1,kmax):
        V[n][k-1] = V[n-1][k-1] - deltaT/(C*deltaZ)(I[n][k]-I[n][k-1])
    I[n][kmax-1] = 0

plt.plot(range(kmax),v[900])
plt.show()

'''
Do jeito que esta o codigo i[1][0] contem a corrente no i tempo 1/2, k 0
e v [1][0] possui a tensao no tempo 1, posicao 1/2
'''
