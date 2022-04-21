import pandas as pd 
# import matplotlib.pyplot as plt
# from control import *
import csv 
import numpy as np

def columnTable(A):
    column_format = ''
    [n,m] = A.shape
    for i in range(m):
        column_format =column_format+'|c|'
    return column_format

H=pd.read_excel('Data/H.xlsx')
M=pd.read_excel('Data/MAX.xlsx')
M=pd.DataFrame(['gf'],H.T)

K_wz=pd.read_excel('Data/K_wz.xlsx')
K_v=pd.read_excel('Data/K_v.xlsx')


with open("M.tex", "w") as f1:
    f1.write(
        M
        .rename(columns= {'1':r'$ \omega_z$'})
        .round(3)
        .to_latex(
            caption = "Сетка махов",
            label = "tab:Сетка махов",
            column_format= columnTable(M),
            escape=False,
            position="H"
        )
    )
# with open("K_wz.tex", "w") as f2:
#     f2.write(
#         K_wz
#         .rename(columns= {'1':r'$ \omega_z$'})
#         .round(3)
#         .to_latex(
#             caption = "Сетка махов",
#             label = "tab:Сетка махов",
#             column_format= "|c|c|c|c|c|c|c|c|c|c|",
#             escape=False,
#             position="H"
#         )
#     )
# with open("K_v.tex", "w") as f3:
#     f3.write(
#         K_v
#         .rename(columns= {'1':r'$ \omega_z$'})
#         .round(3)
#         .to_latex(
#             caption = "Сетка махов",
#             label = "tab:Сетка махов",
#             column_format= "|c|c|c|c|c|c|c|c|c|c|",
#             escape=False,
#             position="H"
#         )
#     )