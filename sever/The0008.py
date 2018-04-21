import pymysql

def  Main(label):
   A= pymysql.connect(host="localhost",user="root",password="790945538",db="time")
   cur = A.cursor()
   cur.execute("select easy from one where label = %s",label)
   raw = cur.fetchall()
   A.close()
   if raw ==():
       return 0
   else:
       return raw[0][0]

if __name__ == '__main__':
   Main(label)



    