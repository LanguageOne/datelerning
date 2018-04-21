import pymysql

def Main(thestr):
    A = A= pymysql.connect(host="localhost",user="root",password="790945538",db="time") 
    themin = 0
    themid = 1
    for i in range(0,len(thestr)):
        if thestr[i] == '@':
           themin = i
        elif thestr[i] =='#' :
           themid = i
           break

    Themin = thestr[themin+1:themid]
    Themid = thestr[themid+1:len(thestr)]
    cur = A.cursor()
    sql = "select user,label,score from submit_status where updated>%s  and updated>%s"

    cur.execute(sql,(Themin,Themid))
    raw = cur.fetchall()

    return raw

    A.close()

if __name__ ==  '__main__':
    Main()

