import pandas as pd 
# import matplotlib.pyplot as plt
import csv 
import numpy as np

def columnTable(A):
    column_format = ''
    [n,m] = A.shape
    for i in range(m):
        column_format =column_format+'c|'
    return column_format



def LatexTable(table,fileNaame):
    with open(f'{fileNaame}.tex', "w") as f:
        f.write(
            table
            .rename(columns= {'1':r'$ \omega_z$'})
            .round(3)
            .to_latex(
                caption = "Сетка махов",
                label = "tab:Сетка махов",
                column_format='|' + columnTable(table),
                escape=False,
                position="H"
            )
        )
