import pymysql
import pandas as pd
import numpy as np

def Main():
   A= pymysql.connect(host="localhost",user="root",password="790945538",db="time")
   cur = A.cursor() 
   sql = "select user,label,score from submit_status where contest_id = 0"
   sql1 = "select user,GROUP_CONCAT(label),GROUP_CONCAT(score) from submit_status where contest_id = 0 group by user"
   cur.execute(sql)
   raw = cur.fetchall()
   exc = pd.DataFrame (columns=['id','label','score'])
   A.close()

   print(len(raw))
   return exc

if __name__ == '__main__':
    Main()
