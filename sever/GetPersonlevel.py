import pandas as pd
import numpy as np
import The0001,The0006,The0008,plot0001
def Main(string):
    exc1 = The0001.Main(string)
    exc2 = The0006.Main(string)
    score = []
    id = []
    for i in range(1,len(exc1)):
        tmp=exc2[i][1]
        if tmp!=exc2[i-1][1]:
            score.append(exc1[i-1][0])
            if exc1[i-1][1] != 0:
                id.append(str(exc1[i-1][1])+exc2[i-1][1])
            else:
                id.append(exc2[i-1][1])
        elif i == len(exc1)-1:
            score.append(exc1[i][0])
            if exc1[i][1] != 0:
                id.append(str(exc1[i][1])+exc2[i][1])
            else:
                id.append(exc2[i][1])
    label = ['A','B','C','D']
    labelscore = [0]*4
    for i in id:
        thetmp = The0008.Main(i)
        if i[2] == 'A':
            labelscore[0] += thetmp
        if i[2] == 'B':
            labelscore[1] += thetmp
        if i[2] == 'C':
            labelscore[2] += thetmp
        if i[2] == 'D':
            labelscore[3] += thetmp

    plot0001.Main(label,labelscore)
    return 0
if __name__ == '__main__':
    string = "gaoyan"
    Main(string)


