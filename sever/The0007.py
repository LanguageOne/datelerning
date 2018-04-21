import pymysql

def Main(contest_id):
   A= pymysql.connect(host="localhost",user="root",password="790945538",db="time")
   cur = A.cursor() 
   sql = "select user from submit_status where contest_id = %s "
   cur.execute(sql,contest_id)
   raw = cur.fetchall()
   A.close()
   
   return raw

if __name__ == '__main__':
    contest_id = 55
    Main(contest_id)


