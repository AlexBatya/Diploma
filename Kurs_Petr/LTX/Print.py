import sys

sys.path.insert(0,"../")
from Expenses import qh,qkm
from VerticalSpeed import Vy,nx
from Ppotr import *
from Data import *
from Prasp import *
from funPrint import *
import pandas as pd

M_interp = np.arange(M1[1],M1[-1],0.3)
H_interp = np.arange(H1[0],H1[-1],4000)

VV = pd.DataFrame(V(M_interp,H_interp),columns = M_interp,index = H_interp)
VV.columns.name = 'H,м/M'
qq= pd.DataFrame(q(M_interp,H_interp)/10000,columns = M_interp,index = H_interp)
qq.columns.name = 'H,м/M'
Cyy = pd.DataFrame(Cy(M_interp,H_interp),columns = M_interp,index = H_interp)
Cyy.columns.name = 'H,м/M'
Cxx = pd.DataFrame(Cx(M_interp,H_interp),columns = M_interp,index = H_interp)
Cxx.columns.name = 'H,м/M'
KK = pd.DataFrame(K(M_interp,H_interp),columns = M_interp,index = H_interp)
KK.columns.name = 'H,м/M'
pp = pd.DataFrame(Pp(M_interp,H_interp)/100000,columns = M_interp,index = H_interp)
pp.columns.name = 'H,м/M'
pr = pd.DataFrame(np.divide(Pr(M_interp,H_interp),100000),columns = M_interp,index = H_interp)
pr.columns.name = 'H,м/M'
Vyy = pd.DataFrame(Vy(M_interp,H_interp),columns = M_interp,index = H_interp)
Vyy.columns.name = 'H,м/M'
nxx = pd.DataFrame(nx(M_interp,H_interp),columns = M_interp,index = H_interp)
nxx.columns.name = 'H,м/M'
qhh = pd.DataFrame(qh(M_interp,H_interp)/10000,columns = M_interp,index = H_interp)
qhh.columns.name = 'H,м/M'
qkkr = pd.DataFrame(qkm(M_interp,H_interp),columns = M_interp,index = H_interp)
qkkr.columns.name = 'H,м/M'

M_interp = np.arange(M1[0],M1[-1],0.01)

LatexTable(VV,'texi/V','V',r'Результаты расчётов $V(M,H)$ м/с',1)
LatexTable(qq,'texi/q','q',r'Результаты расчётов $q(M,H)$, \cdot 10^{-4}$ Н/м$^2$',2)
LatexTable(Cyy,'texi/Cy','Cy',r'Результаты расчётов $C_y(M,H)$',3)
LatexTable(Cxx,'texi/Cx','Cx',r'Результаты расчётов $C_x(M,H)$',3)
LatexTable(KK,'texi/K','K',r'Результаты расчётов $K(M,H)$',2)
LatexTable(pp,'texi/Pp','Pp',r'Результаты расчётов $P_\text{п}(M,H) \cdot 10^{-5},$ Н$',2)
LatexTable(pr,'texi/Pr','Pr',r'Результаты расчётов $P_\text{р}(M,H) \cdot 10^{-5},$ Н$',2)
LatexTable(Vyy,'texi/Vy','Vy',r'Результаты расчётов $V^*_y(M,H)$, м/с',1)
LatexTable(nxx,'texi/nx','nx',r'Результаты расчётов $n_x(M,H)$',3)
LatexTable(qhh,'texi/qh','nx',r'Результаты расчётов $q_\text{ч}(M,H) \cdot 10^{-4}$, кг/ч',2)
LatexTable(qkkr,'texi/qkm','nx',r'Результаты расчётов $q_\text{км}(M,H)$, кг/км',0)

P_rasp = Pr(M_interp,H_interp)
P_potr = Pp(M_interp,H_interp)

# for i in range(len(H_interp)):
#     plt.plot(M_interp,P_potr[i])
#     plt.plot(M_interp,P_rasp[i],'-.')
#     plt.legend(('Pп, Н','Pр, Н'))
#     plt.grid()
#     plt.title('H = '+str(H_interp[i])+' км')
#     plt.xlabel('Число Маха')
#     plt.ylabel('Тяга, H')
#     plt.savefig('figs/PpPr'+str(i)+'.jpg')
#     plt.show()

# M_interp = np.arange(M1[1],M1[-1],0.01)
# for i in range(len(H_interp)):
#     plt.plot(M_interp,Cydop(M_interp),'-.',M_interp,Cy(M_interp,H_interp[i]))
#     plt.legend((r'$C_{y_{доп}}$',r'$C_y$'))
#     plt.grid()
#     plt.title('H = '+str(H_interp[i])+' км')
#     plt.xlabel('Число Маха')
#     plt.ylabel('Коэффициент подьёмной силы')
#     plt.savefig('figs/CyCydop'+str(i)+'.jpg')
#     plt.show()

# for i in range(len(H_interp)):
#     plt.plot(M_interp,qh(M_interp,H_interp[i]))
#     plt.legend([r'$q_ч,$ кг/ч'])
#     plt.grid()
#     plt.title('H = '+str(H_interp[i])+' км')
#     plt.xlabel('Число Маха')
#     plt.ylabel('Часовой расход топлива, H/ч')
#     plt.savefig('figs/qh'+str(i)+'.jpg')
#     plt.show()

# for i in range(len(H_interp)):
#     plt.plot(M_interp,qkm(M_interp,H_interp[i]))
#     plt.legend([r'$q_{км},$ кг/км'])
#     plt.grid()
#     plt.title('H = '+str(H_interp[i])+' км')
#     plt.xlabel('Число Маха')
#     plt.ylabel('Километровый расход топлива, H/км')
#     plt.savefig('figs/qkm'+str(i)+'.jpg')
#     plt.show()

V_y = Vy(M_interp,H_interp)

# for i in range(len(H_interp)):
#     plt.plot(M_interp,V_y[i])
#     plt.legend([r'$V_y,$ м/с'])
#     plt.grid()
#     plt.title('H = '+str(H_interp[i])+' км')
#     plt.xlabel('Число Маха')
#     plt.ylabel('Вертикальная скорость, м/c')
#     plt.savefig('figs/Vy'+str(i)+'.jpg')
#     plt.show()

Vy_max = []
MVy_max = []
P_potr_min = []
M_nae = []
qh_min = []
qkm_min = []
Mq_max = []
Mqh_min = []
Mqkm_min = []
MCy_dop = []
M_interp = np.arange(M1[0],M1[-1],0.0001)
H_interp = np.arange(H1[0],H1[-1],1000)
P_rasp = Pr(M_interp,H_interp)
P_potr = Pp(M_interp,H_interp)
V_y = Vy(M_interp,H_interp)
C_y = Cy(M_interp,H_interp)
M_min = []
M_max = []
for i in range(len(H_interp)):
    P_potr_min.append(np.min(P_potr[i]))
    M_nae.append(M_interp[np.where(P_potr[i]==P_potr_min[i])])
    Vy_max.append(np.max(V_y[i]))
    qh_min.append(np.min(qh(M_interp,H_interp[i])))
    qkm_min.append(np.min(qkm(M_interp,H_interp[i])))
    MVy_max.append(M_interp[np.where(V_y[i]==Vy_max[i])])
    Mqh_min.append(M_interp[np.where(qh(M_interp,H_interp[i])==qh_min[i])])
    Mqkm_min.append(M_interp[np.where(qkm(M_interp,H_interp[i])==qkm_min[i])])
    for j in range(len(M_interp)):
        if M_nae[i]>=M_interp[j]:
            if abs(P_rasp[i][j]-P_potr[i][j])<=500:
                M_min.append(M_interp[j])
                break
    for j in range(len(M_interp)):
        if M_nae[i]<=M_interp[j]:
            if abs(P_rasp[i][j]-P_potr[i][j])<=500:
                M_max.append(M_interp[j])
                break   
    for j in range(len(M_interp)): 
        if abs(Cydop(M_interp[j])-C_y[i][j])<=0.01:
            MCy_dop.append(M_interp[j])
            break 
# print(MCy_dop)



