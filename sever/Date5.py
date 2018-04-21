import pandas as pd
import matplotlib.pyplot as plt 

def Main():
    #班级比较 系数成绩
    theid = ['54','55','58','62','65','67','69']
    thex = ['A','B','C','D']
    score=[]
    for i in theid:
        thesum = 0
        k=0.1
        exc = pd.read_excel(i+"xl.xls")
        for j in thex:
            A = float(sum(exc[i+j])) / float(len(exc[i+j]))
            thesum  = thesum + k * A
            k = k + 0.1
        score.append(thesum)
    plt.scatter(theid,score)
    plt.grid()
    plt.show()


if __name__ == '__main__':
    Main()
