import mysql.connector
from datetime import *
import time
import os , sys


curdate=time.strftime('%Y_%m_%d',time.localtime(time.time()) )
year = curdate[:4]
month = curdate[5:7]
day = curdate[-2:]


def get_query_date(year,month,day):
 dlist = []
 i = 29
 
 while (i >= 0):
   d = datetime(int(year), int(month), int(day)) - timedelta(days=i)
   s = ((str(d)[:10])[:4]+'_'+(str(d)[:10])[5:7]+'_'+(str(d)[:10])[-2:])
   dlist.append(s)
   i -= 1
 return dlist
   

def queryresult(d): 
 cn = mysql.connector.connect(user = 'root',password = 'royasoft',host = '10.1.189.7' ,database = 'mas')
 HUAWEIUC_count = 0
 ITIL_count = 0
 Solarwinds_count = 0
 SystemMon_count = 0
 cursor = None

 try:
   cursor = cn.cursor()
   
   for x in range(len(d)):
    
     query = ("select  SERVICE_ID,count(*)  from mas_sms_sent_"+d[x] + " GROUP BY SERVICE_ID")
     cursor.execute(query)
     for line in cursor:
         
       
         if (line[0] == 'ITIL'):
          
           ITIL_count = ITIL_count + int(line[1])
         elif (line[0] == 'HUAWEIUC '):
          
           HUAWEIUC_count = HUAWEIUC_count + int(line[1])
         elif (line[0] == 'Solarwinds'):
          
           Solarwinds_count = Solarwinds_count + int(line[1])
         elif (line[0] == 'SystemMon'):
         
           SystemMon_count = SystemMon_count + int(line[1])
            
         
         
     
 except mysql.connector.Error as err:
     print("query table failed.")
     print("Error: {}".format(err.msg))
     
 result_list = {'hw': HUAWEIUC_count , 'ITIL': ITIL_count , 'Solarwinds' : Solarwinds_count , 'SystemMon' :  SystemMon_count}  
 cursor.close()
 cn.close()
 return result_list


def main():

   try:
     print('--------------《各系统最近30天内短信发送数量统计》----------------')
     RL = queryresult(get_query_date(year,month,day))
     print('HUAWEIUC发送数量：            ' + str(RL['hw']))
     print('ITIL发送数量:                 ' + str(RL['ITIL']))
     print('Solarwinds发送数量:           ' + str(RL['Solarwinds']))
     print('SystemMon发送数量:            ' + str(RL['SystemMon']))
     total_count = RL['hw'] + RL['ITIL'] + RL['Solarwinds'] + RL['SystemMon']
     print('发送短信总数量:               ' +  str(total_count))
     quit_input=input('输入任意字符退出:')
     os.system('exit')
   except  EOFError:
       quit_input=input('输入任意字符退出:')
       os.system('exit')

if __name__=='__main__':
   
    main()
