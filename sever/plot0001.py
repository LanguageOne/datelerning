import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def Main(id,score):
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
    Main(label,labelscore)
