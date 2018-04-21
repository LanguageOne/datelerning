import pymysql


def Main(thestr):
    A = A= pymysql.connect(host="localhost",user="root",password="790945538",db="time") 
    thename = thestr[i+1:len(thestr)]

    cur = A.cursor()
    sql = "select user,label,score from submit_status where user like  '%s' " % thestr
    print(sql)
    cur.execute(sql)
    raw = cur.fetchall()
    A.close()
    print(raw)
    return raw
    

if __name__ ==  '__main__':
    Main(thestr)
