import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
# import Callculation as cal
from close import runSingle
from scipy.interpolate import interp1d, interp2d

mass = 180000
S=360
P00 = 0.408
Ha =[0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000,10500,11000,11500,12000,12500,13000,13500,14000,14500,15000,15500,16000,16500,17000,17500,18000,18500,19000,19500,20000,20500,21000,21500,22000,22500,23000,23500,24000,24500,25000,25500,26000,26500,27000,27500,28000,28500,29000,29500,30000]
pa =[101325,95461.3000000000,89876.3000000000,84559.7000000000,79501.4000000000,74691.7000000000,70121.2000000000,65780.4000000000,61660.4000000000,57752.6000000000,54048.3000000000,50539.3000000000,47217.6000000000,44075.5000000000,41105.3000000000,38299.7000000000,35651.6000000000,33154.2000000000,30800.7000000000,28584.7000000000,26499.9000000000,24540.2000000000,22699.9000000000,20984.7000000000,19399.4000000000,17934,16579.6000000000,15327.6000000000,14170.3000000000,13100.6000000000,12111.8000000000,11197.7000000000,10352.8000000000,9571.70000000000,8849.70000000000,8182.20000000000,7565.20000000000,6994.80000000000,6467.50000000000,5978,5529.30000000000,5113,4729,4374.60000000000,4047.50000000000,3745.60000000000,3466.90000000000,3209.50000000000,2971.70000000000,2752.10000000000,2549.20000000000,2361.70000000000,2188.40000000000,2028.10000000000,1880,1743,1616.20000000000,1499,1390.40000000000,1290,1197]
aa = [340.400000000000,338.500000000000,336,334.800000000000,332.700000000000,330.700000000000,328.700000000000,326.700000000000,324.700000000000,322.700000000000,320.700000000000,318.600000000000,316.600000000000,314.500000000000,312.400000000000,310.300000000000,308.200000000000,306.100000000000,303.900000000000,301.800000000000,299.600000000000,299.400000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000,295.200000000000]
Cx01 = [0.0175000000000000,0.0175000000000000,0.0175500000000000,0.0175655000000000,0.0180000000000000,0.0192000000000000,0.0223000000000000,0.0220000000000000,0.0218500000000000,0.0216000000000000,0.0215000000000000,0.0215500000000000,0.0215]
Cydop1 = [0.850000000000000,0.850000000000000,0.850000000000000,0.840000000000000,0.750000000000000,0.700000000000000,0.650000000000000,0.630000000000000,0.610000000000000,0.600000000000000,0.590000000000000,0.530000000000000,0.51]
A1 = [0.0250000000000000,0.0250000000000000,0.0247000000000000,0.0242000000000000,0.0237000000000000,0.0256000000000000,0.0340000000000000,0.0380000000000000,0.0420000000000000,0.0445000000000000,0.0475000000000000,0.0498000000000000,0.0498]
H1=[0,3000,6000,9000,11000,14000,17000,20000,23000]
M1 = [0.0300000000000000,0.250000000000000,0.500000000000000,0.750000000000000,1,1.25000000000000,1.50000000000000,1.75000000000000,2,2.25000000000000,2.50000000000000,2.75000000000000,3.03]
# Безфарсаж
P01 = [[1,0.836000000000000,0.788000000000000,0.851090000000000,0.935000000000000,1.00647000000000,1.09400000000000,1.19629000000000,1.29900000000000,1.21300000000000,1.03400000000000,0.898760000000000,0.85],
    [0.780000000000000,0.680000000000000,0.629000000000000,0.671870000000000,0.750440000000000,0.809590000000000,0.876690000000000,0.947000000000000,1.05700000000000,0.963000000000000,0.831670000000000,0.723960000000000,0.65],
    [0.605650000000000,0.510000000000000,0.486000000000000,0.530610000000000,0.580000000000000,0.612000000000000,0.665000000000000,0.731000000000000,0.824000000000000,0.760000000000000,0.649000000000000,0.557090000000000,0.49],
    [0.478520000000000,0.404000000000000,0.376000000000000,0.416000000000000,0.452910000000000,0.478520000000000,0.520010000000000,0.572100000000000,0.637000000000000,0.580000000000000,0.502000000000000,0.427310000000000,0.37],
    [0.382280000000000,0.327000000000000,0.302000000000000,0.333730000000000,0.376000000000000,0.396000000000000,0.427310000000000,0.467920000000000,0.510000000000000,0.474990000000000,0.412300000000000,0.352270000000000,0.49]]
Ce01 = [[0.884340000000000,0.922600000000000,0.984400000000000,1.07122000000000,1.16000000000000,1.23161000000000,1.29341000000000,1.33755000000000,1.38022000000000,1.40700000000000,1.42437000000000,1.43614000000000,1.44],
    [0.845814545454546,0.883673636363636,0.942263636363636,1.02386636363636,1.12000000000000,1.18425636363636,1.24445000000000,1.28658545454545,1.32805000000000,1.34878636363636,1.37340272727273,1.38718000000000,1.39],
    [0.807289090909091,0.844747272727273,0.900127272727273,0.976512727272727,1.06814272727273,1.13690272727273,1.19549000000000,1.23562090909091,1.27588000000000,1.29822272727273,1.32243545454545,1.33822000000000,1.34],
    [0.768763636363636,0.805820909090909,0.857990909090909,0.929159090909091,1.01436909090909,1.08954909090909,1.14653000000000,1.18465636363636,1.22371000000000,1.24765909090909,1.27146818181818,1.28926000000000,1.294],
    [0.743080000000000,0.779870000000000,0.829900000000000,0.897590000000000,0.978520000000000,1.05798000000000,1.11389000000000,1.15068000000000,1.18893000000000,1.21395000000000,1.23749000000000,1.25662000000000,1.26]
    ]
Cedop1 = [2,1.70000000000000,1.43000000000000,1.20000000000000,0.970000000000000,0.850000000000000,0.800000000000000,0.850000000000000,1]
R1 = [0,0.125000000000000,0.250000000000000,0.375000000000000,0.500000000000000,0.625000000000000,0.750000000000000,0.875000000000000,1]

for i in range(len(H1)):     #Добавляет в массивы тяг и расходов данные выше 11 км (они постоянные )
    if H1[i] > 11000:
        P01.append(P01[-1])
        Ce01.append(Ce01[-1])

method = 'cubic'

A = interp1d(M1, A1,method)  # Сразу интерполируем весь этот калл дабы потом было удобно с этим работать
Cx0 = interp1d(M1, Cx01,method)
Cydop = interp1d(M1, Cydop1,method)
p = interp1d(Ha, pa,method)
a = interp1d(Ha, aa,method)
CeDros = interp1d(R1,Cedop1)
P0 = interp2d(M1,H1,P01,method)
Ce0 = interp2d(M1,H1,Ce01,method)



Mmax =  [1.6202,1.9,2.2,2.4,2.4,2.4,2.4,2.4,2.4,2.4,2.4,2.3]   # Не принципиальное поле 
Mmin = [0.28,0.333,0.407,0.503,0.55,0.63,0.82,1.1,1.46,1.9,2.25,2.3] # Это для расчёта Траектории набора
M2 = np.array([Mmin,Mmax]).T 
n = np.size(M2,0)
number = 10
M = []

for i in range(n):
    M.append(np.linspace(M2[i][0],M2[i][-1],number)) #разбиения области на узловые точки