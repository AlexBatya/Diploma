import sys
sys.path.insert(0,"../")
import numpy as np 
import matplotlib.pyplot as plt
from Data import *
from scipy.interpolate import interp1d, interp2d
import math

def V(M,H):
    return M*a(H)

def q(M,H):
    return 0.7*M**2*p(H)

def Cy(M,H):
    return 0.95*mass*9.81/(q(M,H)*S)

def Cx(M,H):
    return Cx0(M) + A(M)*Cy(M,H)*Cy(M,H) 

def He(M,H):
    return H+V(M,H)**2/(2*9.81)

def K(M,H):
    return Cy(M,H)/Cx(M,H)

def Pp(M,H):
    return 0.95*mass*9.81/K(M,H)

def Pr(M,H):
    if H>=11000:
        return P0(M,H)*mass*9.81*P00*(p(H)/22699.9)
    else: 
        return P0(M,H)*mass*9.81*P00

def nx(M,H):
    return (Pr(M,H)-Pp(M,H))/(0.95*mass*9.81)

def Vy(M,H):
    return nx(M,H)*V(M,H)

H0 = 0
M0 = 0.3312
Mk = 0.8
Hk =11000

method = 'cubic'

M_min = [] 
M_max = []
MVy_max = [0.276*1.2,0.837,0.881,0.903,0.945,1.012,1.039]
HVy = [0,2000,4000,6000,8000,10000,11000]

H = np.arange(H0,Hk,200)
M = interp1d(HVy,MVy_max,method)
# P_p = Pp(M(H),H)
# P_r = Pr(M,H)

dVdH = []
dHe = []
kappa = []
Vy_nab = []
teta_nab = []
nx_cred = []
dL_nab = []
Vy_cred = []
dt_nab = []
CeP_cred = [] 
dmt_nab = []
dL = []
CeP = []

def summa(A):
    s= 0
    for i in range(len(A)):
        s = s + A[i] 
    return s

for i in range(len(H)):
    CeP.append(Ce0(M(H[i]),H[i])*Pr(M(H[i]),H[i])/Vy(M(H[i]),H[i])*0.1)



for i in range(len(H)-1):
    dVdH.append(abs((V(M(H[i+1]),H[i+1]) - V(M(H[i]),H[i]))/(H[i+1] - H[i])))
    dHe.append(He(M(H[i+1]),H[i+1])-He(M(H[i]),H[i]))
    kappa.append(1/(1+V(M(H[i]),H[i])*dVdH[i]/9.81))
    Vy_nab.append(Vy(M(H[i]),H[i])*kappa[i])
    teta_nab.append(kappa[i]*nx(M(H[i]),H[i])*57.3)
    nx_cred.append(0.5*(1/nx(M(H[i]),H[i])+1/nx(M(H[i+1]),H[i+1])))
    dL_nab.append(nx_cred[i]*dHe[i]/1000)
    Vy_cred.append(0.5*(1/Vy(M([i]),H[i])+1/Vy(M([i+1]),H[i+1])))
    dt_nab.append(dHe[i]*Vy_cred[i]/60)
    CeP_cred.append(0.5*(CeP[i]+CeP[i+1]))
    dmt_nab.append(dHe[i]*CeP_cred[i]/3600)

m_sn=0.5
mt_nab_=summa(dmt_nab)/mass
mt_snp=0.015
mt_anz=0.05
mt_pr=0.01
m_cn=0.15


mt_kr=1-m_sn-m_cn-mt_nab_-mt_snp-mt_anz-mt_pr
Tkr=60*K(M(11000),11000)/(9.81*Ce0(M(11000),11000)*0.1)*math.log((1-mt_nab_-mt_pr)/(1-mt_kr-mt_nab_-mt_pr))
Lkr=(3.6*V(M(11000),11000)*K(M(11000),11000)/(9.81*Ce0(M(11000),11000)*0.1))*math.log((1-mt_nab_-mt_pr)/(1-mt_kr-mt_nab_-mt_pr))
m_kkr=1-mt_nab_-mt_pr-mt_kr
Ro_nkr=2*m_kkr*Ps/(Cy(M(11000),11000)*V(M(11000),11000)**2)
print("Время полета =",Tkr,"Дальность полета ",Lkr,"Плотность на конечной высоте =",Ro_nkr)

