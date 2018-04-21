
import pymysql
import matplotlib.pyplot as plt


def Main(thestr):
    A= pymysql.connect(host="localhost",user="root",password="790945538",db="time") 
    cur = A.cursor()
    cur.execute("select user,label from submit_status where user = %s",thestr)
    raw = cur.fetchall()
    print()
    return raw

if __name__ == '__main__':
    thestr = "gaoyan"
    Main(thestr)


