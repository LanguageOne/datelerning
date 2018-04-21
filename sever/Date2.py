import pandas as pd
import numpy as np
import pymysql
def Data(one,x):
    for i in range(x[0],len(one)):
        if one[i] ==',':
            a = x[0]
            x[0] = i+1
            return one[a:i]
        elif i == len(one)-1:
            return one[x[0]:i+1]
def Main():
   A= pymysql.connect(host="localhost",user="root",password="790945538",db="time")
   cur = A.cursor()  
   sql = "select user,GROUP_CONCAT(label),GROUP_CONCAT(score) from submit_status where contest_id = %s and ( label = 'A' or label = 'B' or label = 'C'or label = 'D') group by user"
   #theid = [54,55,58,62,65,67,69]
   theid = [54,67]

   for x in range(0,7):
       cur.execute(sql,theid[x])
       raw = cur.fetchall()
       data = raw
       exc = pd.DataFrame (columns=['id',str(theid[x])+'A',str(theid[x])+'B',str(theid[x])+'C',str(theid[x])+'D'])
       print(len(data))
      
       for i in range(0,len(data)):
           exc.loc[i,'id'] = data[i][0]
           thetmp = [0]
           for j in range(0,len(data[i][1]),2):
               tmp = Data(data[i][2],thetmp)
               exc.loc[i,(str(theid[x]))+data[i][1][j]] = int(tmp)
       exc = exc.fillna(0)

       exc.to_excel(str(theid[x])+'xl.xls',index=False)

   return 0
   
if __name__ == '__main__':
    Main()