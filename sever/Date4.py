import pandas as pd
import matplotlib.pyplot as plt
import pymysql

def QI(test):
    I2 = []
    for i in test:
        if not i in I2:
            I2.append(i)

    return I2

def Main(thestr):
    A= pymysql.connect(host="localhost",user="root",password="790945538",db="time") 
    cur = A.cursor()
    cur.execute("select user,contest_id,label,score from submit_status where user = %s",thestr)
    raw = cur.fetchall()
    truetest=[]
    falsetest=[]
    for i in range(0,len(raw)):
        if raw[i][3]>=80:
            if raw[i][1]==0:
                truetest.append(str(raw[i][2]))
            else :
                truetest.append(str(raw[i][1])+str(raw[i][2]))
        else:
            if raw[i][1]==0:
                falsetest.append(str(raw[i][2]))
            else :
                falsetest.append(str(raw[i][1])+str(raw[i][2]))
    truetest = QI(truetest)
    falsetest = QI(falsetest)
    print("trueid")
    for i in truetest:
        if i[len(i)-1]>='A':
            exc = pd.read_excel(i[0:len(i)-1]+".xls")
            print(exc[i])
    print("falseid")
    for i in falsetest:
        if i[len(i)-1]>='A':
            exc = pd.read_excel(i[0:len(i-1)]+".xls")
            print(exc[i])



if __name__ == '__main__':
    thestr='gaoyan'
    Main(thestr)

