import pymysql

def Main(contest_id):
   A= pymysql.connect(host="localhost",user="root",password="790945538",db="time")
   cur = A.cursor() 
   sql = "select user,label,GROUP_CONCAT(score) from submit_status where contest_id = %s and label = 'A' group by user"
   cur.execute(sql,contest_id)
   raw = cur.fetchall()
   A.close()
   print(raw[33][2][1])
   print(len(raw))
   return len(raw)

if __name__ == '__main__':
    contest_id = 55
    Main(contest_id)


