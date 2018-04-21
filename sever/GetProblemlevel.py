import pandas as pd
import numpy as np
import The0007,The0009,The1001,The0010
import pymysql

# exc (id,label,score)
def thefrist(i,j):
    thetmpdate = The0010.Main(i,j)
    thefristsum = 0
    for i in range(0,len(thetmpdate)):
        if thetmpdate[i][2][0] =='1':
            thefristsum += 1
    if thefristsum == 0 :
        return 0.0
    else :
        return float(thefristsum) / float(len(thetmpdate))

def geteasy(x):
    if x>=0.75:
        j = 1
    elif x >=0.5 and x < 0.75:
        j =2
    elif x>0.25 and x < 0.5:
        j =3
    else:
        j = 4
    return j

def thesum(i,j):
    #有人重复提交
    thetmpdate = The0009.Main(i,j)
    thetmptop = 0.0
    thetmpsum = 0
    for i in range(0,len(thetmpdate)):
        if thetmpdate[i][2] == 100:
            thetmptop += 1
        elif thetmpdate[i][2] < 100 and thetmpdate[i][2] >=60 :
            thetmptop += 0.6
        elif thetmpdate[i][2] <60 and thetmpdate[i][2] >0 :
            thetmptop += 0.2
        thetmpsum += 1
    if thetmpsum == 0:
        return 0.0
    else :
        return thetmptop / float(thetmpsum)

def thecompletely(i,j):
    thetmpdate = The0009.Main(i,j)
    thetmptop = 0.0
    thetmpsum = 0
    for i in range(0,len(thetmpdate)):
        if thetmpdate[i][2] == 100:
            thetmptop += 1
        thetmpsum += 1
    if thetmpsum == 0:
        return 0.0
    else :
        return thetmptop / float(thetmpsum)

def thestudc(i,j):
    thetmpdate = The0010.Main(i,j)
    theendsum = 0
    for i in range(0,len(thetmpdate)):
        if len(thetmpdate[i][2]) > 2 :
           if thetmpdate[i][2][len(thetmpdate[i][2])-3] =='1':
                theendsum += 1
    if theendsum == 0 :
        return 0.0
    else :
        return float(theendsum) / float(len(thetmpdate))

def Main(label,contest_id):
    datalen = 0
    for i in contest_id:
        exc = The0007.Main(i)
        if len(exc) == 0:
            continue
        for j in label:
            tmp1 = thefrist(i,j)
            tmp2 = thesum(i,j)
            tmp3 = thecompletely(i,j)
            tt = thestudc(i,j)
            tmp = 0.7 * tmp1 + 0.3 *tmp2
            if tmp1 == 0 and tmp2 == 0:
                continue
            else:
                mm = len(The0010.Main(i,j))
                nn = len(The0009.Main(i,j))
                The1001.Main(str(i)+j,geteasy(tmp),mm,nn,tmp1,tmp2,tmp3,tt,tmp)

    return 0
               
if __name__ =='__main__':
    label = ['A','B','C','D']
    contest_id =[i for i in range(55,69)]
    #label =['1000','1001']
    #contest_id = [0]
    Main(label,contest_id)