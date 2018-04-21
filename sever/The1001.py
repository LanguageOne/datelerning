import pymysql

def  Main(a,b,c,d,e,f,g,h,i):
   A= pymysql.connect(host="localhost",user="root",password="790945538",db="time")
   cur = A.cursor()
   sql = "insert into one(label,easy,sumstud,sumdate,fristac,sumac,completelyac,studac,ac)values('%s',%d,%d,%d,%f,%f,%f,%f,%f)" %(a,b,c,d,e,f,g,h,i)
   cur.execute(sql)
   A.commit()
   A.close()


if __name__ == '__main__':
   Main(a,b,c,d,e,f)


