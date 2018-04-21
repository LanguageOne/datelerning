import pymysql
import matplotlib.pyplot as plt


def Main(thestr):
    A= pymysql.connect(host="localhost",user="root",password="790945538",db="time") 
    cur = A.cursor()
    cur.execute("select score,contest_id from submit_status where user = %s",thestr)
    raw = cur.fetchall()
 
    """
    cur.execute("select user,label from submit_status where user = %s",thestr)
    raw2 = cur.fetchall()
    k=0
    score = [0]*10
    id = ['']*10
    for i in range(1,len(raw)):
        tmp=raw2[i][1]
        if tmp!=raw2[i-1][1]:
            score[k]=raw[i-1][0]
            id[k]=raw2[i-1][1]
            k=k+1
        elif i == len(raw)-1:
            score[k]=raw[i][0]
            id[k]=raw2[i][1]

    print(id)
    print(score)
    plt.scatter(id,score)
    plt.grid()
    plt.show()
    A.close()
    """
    return raw

if __name__ == '__main__':
    thestr = "gaoyan"
    Main(thestr)


