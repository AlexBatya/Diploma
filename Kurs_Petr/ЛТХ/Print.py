from mainLTX import *
from funPrint import *
import pandas as pd

qq= pd.DataFrame(q(M_interp,H_interp),columns = M_interp,index = H_interp)
qq.columns.name = 'H,м/M'
Cyy = pd.DataFrame(Cy(M_interp,H_interp),columns = M_interp,index = H_interp)
Cyy.columns.name = 'H,м/M'
Cxx = pd.DataFrame(Cx(M_interp,H_interp),columns = M_interp,index = H_interp)
Cxx.columns.name = 'H,м/M'
KK = pd.DataFrame(K(M_interp,H_interp),columns = M_interp,index = H_interp)
KK.columns.name = 'H,м/M'
pp = pd.DataFrame(Pp(M_interp,H_interp),columns = M_interp,index = H_interp)
pp.columns.name = 'H,м/M'
pr = pd.DataFrame(Pr(M_interp,H_interp),columns = M_interp,index = H_interp)
pr.columns.name = 'H,м/M'

LatexTable(qq,'texi/q.tex','q',r'Результаты расчётов $q(M,H), Н/$м$^2$',0)
LatexTable(Cyy,'texi/Cy.tex','Cy',r'Результаты расчётов $Cy(M,H)$',3)
LatexTable(Cxx,'texi/Cx.tex','Cx',r'Результаты расчётов $Cx(M,H)$',3)
LatexTable(KK,'texi/K.tex','K',r'Результаты расчётов $K(M,H)$',2)
LatexTable(pp,'texi/Pp.tex','Pp',r'Результаты расчётов $P_\text{п}(M,H)$',0)
LatexTable(pr,'texi/Pr.tex','Pr',r'Результаты расчётов $P_\text{р}(M,H)$',0)

figurePrint(M_interp,Pp(M_interp,H_interp[0]),'Потребные тяги','M',r'P_\text{п}','figs/Pp.jpg')