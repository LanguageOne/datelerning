import The0004,Date3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def theMain(data):
    k=4
    clu_data = data
    kmodel = KMeans(n_clusters = 4,n_jobs = 4)
    kmodel.fit(clu_data)
    labels = data.columns #标签
    plot_data = kmodel.cluster_centers_
    color = ['b', 'g', 'r', 'c'] #指定颜色

    angles = np.linspace(0, 2*np.pi, k, endpoint=False)
    plot_data = np.concatenate((plot_data, plot_data[:,[0]]), axis=1) # 闭合
    angles = np.concatenate((angles, [angles[0]])) # 闭合

    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True) #polar参数！！

    for i in range(len(plot_data)):
        ax.plot(angles, plot_data[i], 'o-', color = color[i], label = u'分数'+str(i), linewidth=2) # 画线

    ax.set_rgrids(np.arange(0.01, 3.5, 0.5), np.arange(-1, 2.5, 0.5), fontproperties="SimHei")
    ax.set_thetagrids(angles * 180/np.pi, labels, fontproperties="SimHei")
    plt.legend(loc = 4)
    plt.show()
def Data(one,x):
    for i in range(x[0],len(one)):
        if one[i] ==',':
            a = x[0]
            x[0] = i+1
            return one[a:i]
        elif i == len(one)-1:
            return one[x[0]:i+1]
def Main(thestr):
    data = The4.Main(thestr)
    exc = pd.DataFrame (columns=['id','A','B','C','D'])

    for i in range(0,len(data)):
        exc.loc[i,'id'] = data[i][0]
        thetmp = [0]
        for j in range(0,len(data[i][1]),2):
            tmp = Data(data[i][2],thetmp)
            exc.loc[i,data[i][1][j]] = int(tmp)
    exc = exc.fillna(0)
    #exc.to_excel('58.xls',index=False)
    #Date3.Main()
    exc.pop('id')
    data = exc/exc.std(axis=0)
    data.columns = [i for i in data.columns]
    theMain(data)
  
if __name__ == '__main__':

    Main(thestr)

