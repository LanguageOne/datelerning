import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import The0001,The0006
def Main(string):
    exc1 = The0001.Main(string)
    exc2 = The0001.Main(string)
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

    dataLenth = len(id)
    angles = np.linspace(0,2*np.pi,dataLenth,endpoint = False)
    data = np.concatenate((score,[score[0]]))
    angles = np.concatenate((angles,[angles[0]]))

    fig = plt.figure()
    ax = fig.add_subplot(111,polar = True)
    ax.plot(angles,data,'ro-',linewidth=2)
    ax.set_thetagrids(angles * 180/np.pi, id, fontproperties="SimHei")
    ax.set_title("hai", va='bottom', fontproperties="SimHei")
    ax.grid(True)
    plt.show()

if __name__ == '__main__':
    string = "gaoyan"
    Main(string)

