from main import * 
# for i in range(len(H)):

Array = [H, M, ] 
tab1 =  
f = open('texi/Результаты.tex','w') 
for i in range(len(H)):
    for j in range(len(M)):
        if MT[i][j] == MT[i][-1]:
            f.write(str(MT[i][j]))
        else:
            f.write(str(MT[i][j])+' & ')
    if MT[i] == MT[-1]:  
        f.write(str(''))
    else:
        f.write(str(r' \\ \hline '))
f.close()