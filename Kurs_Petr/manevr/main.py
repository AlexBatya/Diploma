import sys
sys.path.insert(0,"../")
import numpy as np 
import matplotlib.pyplot as plt 
import math
from Data import *

def V(M,H):
    return M*a(H)

def q(M,H):
    return 0.7*M**2*p(H)

def Cy(M,H):
    return 0.95*(80000 - 100000*0.5)*9.81/(q(M,H)*S)

def Cx(M,H):
    return Cx0(M) + A(M)*Cy(M,H)*Cy(M,H) 

def He(M,H):
    return H+V(M,H)**2/(2*9.81)

def K(M,H):
    return Cy(M,H)/Cx(M,H)

def Pp(M,H):
    return 0.95*(80000 - 100000*0.5)*9.81/K(M,H)

def Pr(M,H):
    if H>=11000:
        return P0(M,H)*(80000 - 100000*0.5)*9.81*P00*(p(H)/22699.9)
    else: 
        return P0(M,H)*(80000 - 100000*0.5)*9.81*P00

def nx(M,H):
    return (Pr(M,H)-Pp(M,H))/(0.95*mass*9.81)

def Vy(M,H):
    return nx(M,H)*V(M,H)

def ny(M,H):
    return Cydop(M)*q(M,H)*S/(80000 - 100000*0.5*9.81)

def ny_e(M,H):
    return Cydop(M)/Cy(M,H)

def ny_P(M,H):
    return 1/Cy(M,H)*math.sqrt()

mc = 80000 - 100000*0.5
ny_ee = 3.5 
M = np.arange(0.41,1.36,0.01)
H = 6000
# print(M)

n_ydop = []
n_y = []
n_ye = []
ny_vir = []
bar_Pr = []
ny_P = []

for i in range(len(M)):
    bar_Pr.append(Pr(M[i],H)/(mc*9.81))
    ny_P.append(1/Cy(M[i],H)*((bar_Pr[i]*Cy(M[i],H)-Cx0(M[i]))/(A(M[i])))**0.5)
    n_y.append(ny(M[i],H))
    n_ye.append(ny_e(M[i],H))
    n_ydop.append(min(n_y[i],ny_ee))
    print(ny_P[i])

    # ny_vir.append(min(n_ydop[i],ny_P))

print(ny_P)


