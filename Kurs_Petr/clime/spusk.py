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

def summa1(A,B):
    s= 0
    B.append(s)
    for i in range(len(A)):
        s = s + A[i] 
        B.append(s)

method = 'cubic'

M_min = [] 
M_max = []
Mnae = [0.584,0.549,0.473,0.41,0.356,0.316,0.28]
HV = [11000,10000,8000,6000,4000,2000,0]

H5 = [Hk]
h=1000
n = abs(Hk-H0)/h+1
s = Hk
for i in range(int(n-1)):
    s = s-h
    H5.append(s)
M5 = interp1d(HV,Mnae,method)

Pp_MG = []
Ce = []
VV = []
nxx = []
nxpp = []
Vyy = []
CeP = []
Hee = []
Vy_spusk = []
teta_spusk = []
dL_spusk = []
dt_spusk = []
dmt_spusk = []
CeP_cred = []
MM = []
for i in range(len(H5)):
    MM.append(M5(H5[i]))
    Pp_MG.append(0.015*Pr(M5(H5[i]),H5[i]))
    Ce.append(0.1*Ce0(M5(H5[i]),H5[i])*2)
    VV.append(M5(H5[i])*a(H5[i]))
    nxx.append((Pp_MG[i]-Pp(M5(H5[i]),H5[i]))/(0.95*mass*9.81))
    Hee.append(H5[i]+VV[i]**2/(2*9.81))
    nxpp.append((-(Pr(M5(H5[i]),H5[i])-Pp(M5(H5[i]),H5[i]))/(0.95*mass*9.81)))
    Vyy.append(nxx[i]*VV[i])
    CeP.append(Ce[i]*Pp_MG[i]/Vyy[i])
# print(CeP)



for i in range(len(H5)-1):
    dVdH.append((VV[i+1]-VV[i])/(H5[i+1]-H5[i]))
    dHe.append(Hee[i+1]-Hee[i])
    kappa.append(1/(1+VV[i]*dVdH[i]/9.81))
    Vy_spusk.append(Vyy[i]*kappa[i])
    teta_spusk.append(kappa[i]*nxx[i]*57.3)
    nx_cred.append(0.5*(1/nxx[i]+1/nxx[i+1]))
    dL_spusk.append(nx_cred[i]*dHe[i]/1000)
    Vy_cred.append(0.5*(1/Vyy[i]+1/Vyy[i+1]))
    dt_spusk.append(dHe[i]*Vy_cred[i]/60)
    CeP_cred.append(0.5*(CeP[i]+CeP[i+1]))
    dmt_spusk.append(dHe[i]*CeP_cred[i]/3600)
# print(Vy_cred)

nxx = [*map(list, zip(*nxx))]
Vyy = [*map(list, zip(*Vyy))]
Ce = [*map(list, zip(*Ce))]
Pp_MG = [*map(list, zip(*Pp_MG))]
MM = np.round(MM,2)
VV = np.round(VV,2)
nxx = np.round(nxx,2)
Vyy = np.round(Vyy,2)
Hee = np.round(Hee,2)
Ce = np.round(Ce,4)
Pp_MG = np.round(Pp_MG,0)
nxx = nxx[0]
Vyy = Vyy[0]
Ce = Ce[0]
Pp_MG = Pp_MG[0]

Array = [H5,MM,VV,nxx,Vyy,Hee,Ce,Pp_MG]
Array = [*map(list, zip(*Array))]
f = open('tables/РезультатыСнижение1.tex','w') 
for i in range(len(H5)):
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

H = np.delete(H5,-1)

print(summa(dt_spusk))
print(summa(dmt_spusk))
print(summa(dL_spusk))

dVdH = np.round(dVdH,4)
teta_spusk = np.round(teta_spusk,2)
Vy_spusk = np.round(Vy_spusk,2)
dHe = np.round(dHe,1)
nx_cred = np.round(nx_cred,3)
Vy_cred = np.round(Vy_cred,2)
teta_spusk = [*map(list, zip(*teta_spusk))]
Vy_spusk = [*map(list, zip(*Vy_spusk))]
nx_cred = [*map(list, zip(*nx_cred))]
Vy_cred = [*map(list, zip(*Vy_cred))]
teta_spusk = teta_spusk[0]
Vy_spusk = Vy_spusk[0]
nx_cred = nx_cred[0]
Vy_cred = Vy_cred[0]

# Array = [H5,dVdH,teta_spusk,Vy_spusk,dHe,nx_cred,Vy_cred]
# Array = [*map(list, zip(*Array))]
# f = open('tables/РезультатыСнижение2.tex','w') 
# for i in range(len(H5)):
#     for j in range(len(Array[i])):
#         if Array[i][j] == Array[i][-1]:
#             f.write(str(Array[i][j]))
#         else:
#             f.write(str(Array[i][j])+' & ')
#     if Array[i] == Array[-1]:  
#         f.write(str(''))
#     else:
#         f.write(str(r' \\ \hline '))
# f.close()


# L = []
# T = []
# mama = []
# summa1(dL_spusk,L)
# summa1(dt_spusk,T)
# summa1(dmt_spusk,mama)
# # H = np.append(H5,Hk)

# plt.plot(T,np.multiply(L,100),'--',T,H5,T,mama,'-.')
# plt.grid()
# plt.legend((r'$L \cdot 10^{-2}$ км',r'$H$, м',r'$m_{T_{спуск}}$, кг'))
# plt.xlabel('t,мин')
# plt.savefig('figs/Характеристики Спуска1'+'.jpg')
# plt.show()

# T = np.delete(T,-1)
# # H = np.delete(H,-1)

# fig, ax = plt.subplots()
# ax.plot(T,Vy_spusk,marker ='^')
# ax.plot(T,teta_spusk,marker = 's')
# ax.plot(T,H/1000,marker = 'x')
# ax.plot(T,M5(H),marker = 'o')
# plt.grid()
# plt.legend((r'$V_y^*$, м/c', r'$\theta$, град',r'H, км',r'M' ))
# plt.xlabel('t,мин')
# plt.savefig('figs/Характеристики пуска2'+'.jpg')
# plt.show()

# H = [0,11,12.3,0]
# L = [77.2,5909,314]

# H1 = [] 
# L1 = []
# summa1(H,H1)
# summa1(L,L1)

# plt.plot(L1,H)
# plt.grid()
# plt.ylabel('Высота, км')
# plt.xlabel('L, км')
# plt.savefig('figs/Траектория полета'+'.jpg')
# plt.show()

m = [36000,36000, 14400, 0]
L = [6300,9954,11052.52]

L1 = []
summa1(L,L1)

plt.plot(L1 ,m)
plt.grid()
plt.ylabel('Целевая нагрузка, кг')
plt.xlabel('Дальность полёта, м')
plt.savefig('figs/Транспортные возможности'+'.jpg')
plt.show()