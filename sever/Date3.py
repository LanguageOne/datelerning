import pandas as pd
import numpy as np
import pymysql
def Main():
    theid = [54,55,58,62,65,67,69]
    for i in range(0,7):
        exc = pd.read_excel(str(theid[i])+"xl.xls")
        xc = exc.corr()
        xc.to_excel(str(theid[i])+".xls",index=False)
if __name__ == '__main__':
    Main()