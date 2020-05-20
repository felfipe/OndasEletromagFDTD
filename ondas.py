import matplotlib.pyplot as plt
import matplotlib.animation as animation
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
v = []
i = []
'''
c1 = -(2*deltaT/(deltaT*deltaZ*R+2*deltaZ*L))
c2 = (2*L-deltaT*R)/(2*L+deltaT*R)
c3 = -(2*deltaT)/(deltaT*deltaZ*G+2*deltaZ*C)
c4 = (2*C-deltaT*G)/(2*C-deltaT*G)
'''
vl = []
il = []
v0 = [] #v inicial para n = 0 representa i -1/2 para qualque k
i0 = []#i inicial para n = 0 representa n 0 para qualquer k
v0.append(Z0/(Zg + Z0)*Vg)
i0.append(Vg/(Zg+Z0))
for j in range(kmax-1):
    v0.append(0)
    i0.append(0)
v.append(v0)
i.append(i0)
#função para animar

'''

A primeira corrente que calculamos é a corrente no tempo 1/2 para diferentes valores de k
para isso precisamos da corrente no tempo -1/2(que devemos inserir no vetor i0) e da tensão
no tempo 0 para qualquer ponto da LT.
A primeira tensão que calculamos é a tensão no tempo 1 para diferentes valores de k
para isso precisamos da tensão no tempo 0(que devemos inserir no vetor v0) e da corrente no tempo
1/2(calculada no passo anterior) para qualquer ponto da LT
 '''
for n in range (nmax):
    for k in range (kmax):
        if(k == 0):
            iaux = c1*(v[n][k] - v[n][k])+c2*i[n][k]#v[n][k-1] esta fora da linha de transmissao logo v = 0 ou ???
            il.append(iaux)
        else:
            iaux = (c1*(v[n][k]-v[n][k-1])+c2*i[n][k])
            il.append(iaux)
    i.append(il)
    for k in range (0,kmax):
        if (k == kmax-1):
            vl.append(0)
        else:
            vaux = c3*(i[n+1][k+1]-i[n+1][k])+c4*v[n][k]
            vl.append(vaux)
    v.append(vl) 
    vl = []
    il = []
plt.plot(range(kmax),v[900])
plt.show()

'''
Do jeito que esta o codigo i[1][0] contem a corrente no i tempo 1/2, k 0
e v [1][0] possui a tensao no tempo 1, posicao 1/2
'''
