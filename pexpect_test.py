# -*- coding: gbk -*-
print('中文测试')
import mysql.connector
def Query_SMS_Box_Count(platname):
    print('查询MAS平台对接系统短信积压数量')
    cn = mysql.connector.connect(user = 'root',password = 'ceb1234',host = '127.0.0.1' ,database = 'mas')
    cursor = None
    try:
           cursor = cn.cursor()
           query = ('select count(*) from  mas_sms_outbox where  service_id= ' + '\''+platname + '\''+';')
           #print(query)
           cursor.execute(query)
           result_list =  cursor.fetchone()
    except mysql.connector.error as err:
           print("execute query table failed.")
           print("error: {}".format(err.msg))
    cursor.close()
    cn.close()
    return result_list

if __name__ == '__main__':
      s = Query_SMS_Box_Count('ITIL')
      print('result is '+ str(s[0]))

