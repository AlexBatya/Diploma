import sys
sys.path.insert(0,"../")
from Data import *
import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.pyplot as plt
import math 

fp=0.02
m0=180000
g=9.81
a=6
alfa=a*3.14/180
Ps=490.5
Ro=1.225
P0=0.408
Ph=0.935
Pr=m0*g*Ph*P0
P=1.25*Pr
P_vzlet=P/(m0*g)
Cy_vzlet=0.96875                                                                    #из графиков 
sin=math.sin(alfa)
V_otr=math.sqrt(20*Ps*(1-0.9*P_vzlet*sin)/(Ro*Cy_vzlet))
print("—корость отрыва=",V_otr,V_otr*3.6)
print()

Cp=0.9*P_vzlet-fp
Cyp=0.625
Cxp=0.1125
bp=(Cxp-fp*Cyp)*Ro/(2*Ps*10)

Lp=(1/(2*g*bp))*math.log(Cp/(Cp-bp*V_otr**2))
print("ƒлина разбега=",Lp)
print()

x_otr=0.11
V2=1.1*V_otr
H_vzlet=10.7
V_cp=math.sqrt((V2**2+V_otr**2)/2)
nx_cp=P_vzlet-(x_otr*Ro*V_cp**2)/(Ps*20)
L_BYB=(1/nx_cp)*((V2**2-V_otr**2)/(2*g)+H_vzlet)

L_BD=Lp+L_BYB
print("¬злетна€ дистанци€=",L_BD)
print()

m_tsnp=0.015
m_kkr=0.715
m_pos=m_kkr-m_tsnp
Cy_kas=1.344

V_kas=math.sqrt((2*m_pos*Ps*10)/(Cy_kas*Ro))
print('—корость касани€ ¬ѕѕ=',V_kas,V_kas*3.6)
print()

fn=0.2
n=2/4
Prevers=P0*m0*0.4*n*g
P_revers=Prevers/(m_pos*m0*g)
an=-P_revers-fn
Cx_prob=0.196875
Cy_prob=0.25
bn=Ro*(Cx_prob-fn*Cy_prob)/(m_pos*Ps*20)

Lprob=(1/(2*g*bn))*math.log((an-bn*V_kas**2)/an)
print('ƒлина пробега',Lprob)
print()


H_pos=15
Cy_pos=0.7*Cy_kas
Cx_pos=0.16
K_pos=Cy_pos/Cx_pos
V_pl=math.sqrt((2*m_pos*Ps*10)/(Cy_pos*Ro))
L_BYP=K_pos*(H_pos+(V_pl**2-V_kas**2)/(2*g))

Lpd=Lprob+L_BYP
print('ѕосадочна€ дистанци€',Lpd)

