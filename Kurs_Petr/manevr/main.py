import sys
sys.path.insert(0,"../")
import numpy as np 
import matplotlib.pyplot as plt 
import math
from Data import *
global mc

def isint(s):
    try:
        int(s) or float(s)
        return True
    except ValueError:
        return False

def V(M,H):
    return M*a(H)

def q(M,H):
    return 0.7*M**2*p(H)

def Cy(M,H):
    return 0.95*mc*9.81/(q(M,H)*S)

def Cx(M,H):
    return Cx0(M) + A(M)*Cy(M,H)*Cy(M,H) 

def He(M,H):
    return H+V(M,H)**2/(2*9.81)

def K(M,H):
    return Cy(M,H)/Cx(M,H)

def Pp(M,H):
    return 0.95*mc*9.81/K(M,H)

def Pr(M,H):
    if H>=11000:
        return P0(M,H)*mc*9.81*P00*(p(H)/22699.9)
    else: 
        return P0(M,H)*mc*9.81*P00

def nx(M,H):
    return (Pr(M,H)-Pp(M,H))/(0.95*mass*9.81)

def Vy(M,H):
    return nx(M,H)*V(M,H)

def ny(M,H):
    return Cydop(M)*q(M,H)*S/(mc*9.81)

def ny_e(M,H):
    return Cydop(M)/Cy(M,H)


mc = 180000 - 30000*0.5
ny_ee = np.array([3.5])
M = np.arange(0.41,1.35,0.1)
H = 6000
# print(M)

n_ydop = []
n_y = []
n_ye = []
ny_vir = []
bar_Pr = []
ny_P = []
w_vir = []  
r_vir = [] 
t_vir =[]  
VV = []
n_yee = []


for i in range(len(M)):
    n_yee.append(ny_ee)
    VV.append(V(M[i],H))
    bar_Pr.append(Pr(M[i],H)/(mc*9.81))
    ny_P.append(1/Cy(M[i],H)*((bar_Pr[i]*Cy(M[i],H)-Cx0(M[i]))/(A(M[i])))**0.5)
    n_y.append(np.array([ny(M[i],H)]))
    n_ye.append(ny_e(M[i],H))
    n_ydop.append(min(n_y[i],ny_ee))
    if isint(ny_P[i]) == False :
        ny_P[i] = np.array([3.6])
    ny_vir.append(min(n_ydop[i],ny_P[i]))
    # if ny_P[i] == 100:
    #     ny_P = np.array([1])
    w_vir.append(9.81/V(M[i],H)*(ny_vir[i]**2-1)**0.5)
    r_vir.append(V(M[i],H)/w_vir[i])
    t_vir.append(2*3.14/w_vir[i])
    # print(t_vir[i])

M = np.round(M,2)
VV = np.round(VV,2)
ny_P = np.round(ny_P,3)
n_y = np.round(n_y,3)
n_ye = np.round(n_ye,3)
n_ydop = np.round(n_ydop,3)
ny_vir = np.round(ny_vir,3)
w_vir = np.round(w_vir,5)
r_vir = np.round(r_vir,1)
t_vir = np.round(t_vir,1)

ny_P = [*map(list, zip(*ny_P))]
n_y = [*map(list, zip(*n_y))]
# n_ye = [*map(list, zip(*n_ye))]
n_ydop = [*map(list, zip(*n_ydop))]
ny_vir = [*map(list, zip(*ny_vir))]
w_vir = [*map(list, zip(*w_vir))]
r_vir = [*map(list, zip(*r_vir))]
t_vir = [*map(list, zip(*t_vir))]

ny_P = ny_P[0]
n_y = n_y[0]
# n_ye = n_ye[0]
n_ydop = n_ydop[0]
ny_vir = ny_vir[0]
w_vir = w_vir[0]
r_vir = r_vir[0]
t_vir = t_vir[0]


Array = [M,VV,ny_P,n_ye,n_ydop,ny_vir,w_vir,r_vir,t_vir]
Array = [*map(list, zip(*Array))]
f = open('tables/РезультатыМаневр.tex','w') 
for i in range(len(M)):
    for j in range(len(Array[i])):
        if Array[i][j] == Array[i][-1]:
            f.write(str(Array[i][j]))
        else:
            f.write(str(Array[i][j])+' & ')
    if Array[i] == Array[-1]:  
        f.write(str(''))
    else:
        f.write(str(r' \\ \hline '))
f.close()

fig, ax = plt.subplots()
ax.plot(M,ny_vir,marker = '^')
ax.plot(M,np.divide(t_vir,10),marker = 'x')
ax.plot(M,np.multiply(w_vir,100), marker = 'o')
ax.plot(M,np.divide(r_vir,1000), marker = 's')

plt.grid()
plt.legend((r'$n_{y_{вир}}$',r'$t_{вир} \cdot 10$, c',r'$\omega_{вир} \cdot 10^{-2}$, 1/c',r'$r_{вир} \cdot 10^{3}$, м'))
plt.xlabel('Число Маха')
plt.savefig('figs/РезультатыМаневры.jpg')
plt.show()

fig, ax = plt.subplots()
ax.plot(M,ny_vir,marker = '^')
ax.plot(M,n_ydop,marker = 'x')
ax.plot(M,n_ye, marker = 'o')
ax.plot(M,ny_P, marker = 's')
ax.plot(M,n_yee, marker = '<')

plt.grid()
plt.legend((r'$n_{y_{вир}}$',r'$n_{y_{доп}}$',r'$n_{y_{ГП}}$',r'$n_{y_P}$',r'$n_{y_е}$'))
plt.xlabel('Число Маха')
plt.savefig('figs/РезультатыМаневры2.jpg')
plt.show()
