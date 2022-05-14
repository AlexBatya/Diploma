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
h = 1000

method = 'cubic'

M_min = [] 
M_max = []
# MVy_max = [0.276*1.2,0.837,0.881,0.903,0.945,1.012,1.039]
MVy_max = [0.276*1.2,0.402,0.454,0.515,0.587,0.671,0.709]
HVy = [0,2000,4000,6000,8000,10000,11000]

H = np.arange(H0,Hk+h,h)
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
VV = []
nxx = []
V_y = []
Hee = []
Cee = []
Ppp = []
MM = []

def summa1(A,B):
    s= 0
    B.append(s)
    for i in range(len(A)):
        s = s + A[i] 
        B.append(s)
    
def summa(A):
    s= 0
    for i in range(len(A)):
        s = s + A[i] 
    return s

for i in range(len(H)):
    MM.append(M(H[i]))
    VV.append(V(M(H[i]),H[i]))
    nxx.append(nx(M(H[i]),H[i]))
    V_y.append(Vy(M(H[i]),H[i]))
    Hee.append(He(M(H[i]),H[i]))
    Cee.append(Ce0(M(H[i]),H[i]))
    Ppp.append(Pp(M(H[i]),H[i]))
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


nxx = [*map(list, zip(*nxx))]
V_y = [*map(list, zip(*V_y))]
Cee = [*map(list, zip(*Cee))]
MM = np.round(MM,2)
VV = np.round(VV,2)
nxx = np.round(nxx,2)
V_y = np.round(V_y,2)
Hee = np.round(Hee,2)
Cee = np.round(Cee,4)
Ppp = np.round(Ppp,0)
nxx = nxx[0]
V_y = V_y[0]
Cee = Cee[0]


Array = [H,MM,VV,nxx,V_y,Hee,Cee,Ppp]
Array = [*map(list, zip(*Array))]
f = open('tables/РезультатыНабор1.tex','w') 
for i in range(len(H)):
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

H = np.delete(H,-1)

dVdH = np.round(dVdH,4)
teta_nab = np.round(teta_nab,2)
Vy_nab = np.round(Vy_nab,2)
dHe = np.round(dHe,1)
nx_cred = np.round(nx_cred,3)
Vy_cred = np.round(Vy_cred,2)
teta_nab = [*map(list, zip(*teta_nab))]
Vy_nab = [*map(list, zip(*Vy_nab))]
nx_cred = [*map(list, zip(*nx_cred))]
Vy_cred = [*map(list, zip(*Vy_cred))]
teta_nab = teta_nab[0]
Vy_nab = Vy_nab[0]
nx_cred = nx_cred[0]
Vy_cred = Vy_cred[0]

Array = [H,dVdH,teta_nab,Vy_nab,dHe,nx_cred,Vy_cred]
Array = [*map(list, zip(*Array))]
f = open('tables/РезультатыНабор2.tex','w') 
for i in range(len(H)):
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

print(summa(dL_nab))
print(summa(dt_nab))
print(summa(dmt_nab))

L = []
T = []
mama = []
summa1(dL_nab,L)
summa1(dt_nab,T)
summa1(dmt_nab,mama)
H = np.append(H,Hk)

# plt.plot(T,np.multiply(L,100),'--',T,H,T,mama,'-.')
# plt.grid()
# plt.legend((r'$L \cdot 10^{-2}$ км',r'$H$, м',r'$m_{T_{наб}}$, кг'))
# plt.xlabel('t,мин')
# plt.savefig('figs/Характеристики набора высоты1'+'.jpg')
# plt.show()

# T = np.delete(T,-1)
# H = np.delete(H,-1)

# fig, ax = plt.subplots()
# ax.plot(T,Vy_nab,marker ='^')
# ax.plot(T,teta_nab,marker = 's')
# ax.plot(T,H/1000,marker = 'x')
# ax.plot(T,M(H),marker = 'o')
# plt.grid()
# plt.legend((r'$V_y^*$, м/c', r'$\theta$, град',r'H, км',r'M' ))
# plt.xlabel('t,мин')
# plt.savefig('figs/Характеристики набора высоты2'+'.jpg')
# plt.show()

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

#Участок снижения 
