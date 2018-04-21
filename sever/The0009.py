import pymysql

def  Main(contest,label):
   A= pymysql.connect(host="localhost",user="root",password="790945538",db="time")
   cur = A.cursor() 
   sqlA = "select user,label,score from submit_status where contest_id = %s and label = 'A'"
   sqlB = "select user,label,score from submit_status where contest_id = %s and label = 'B'"
   sqlC = "select user,label,score from submit_status where contest_id = %s and label = 'C'"
   sqlD = "select user,label,score from submit_status where contest_id = %s and label = 'D'"
   sql = "select user,label,score from submit_status where contest_id = 0 and label = %s"
   if label == 'A':
       cur.execute(sqlA,contest)
   elif label =='B': 
        cur.execute(sqlB,contest)
   elif label =='C':
       cur.execute(sqlC,contest)
   elif label =='D':
        cur.execute(sqlD,contest)
   else:
       cur.execute(sql,label)
   raw = cur.fetchall()
   A.close()
   return raw

if __name__ == '__main__':
   Main(contest,label)



    