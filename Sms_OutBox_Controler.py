# -*- coding: gbk -*-
import mysql.connector
import os
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

def Delete_SMS_Box(platname):
    print('删除' + platname +'系统在MAS平台的积压短信')
    cn = mysql.connector.connect(user = 'root',password = 'ceb1234',host = '127.0.0.1' ,database = 'mas')
    cursor = None
    try:
           cursor = cn.cursor()
           query = ('delete from  mas_sms_outbox where service_id= ' + '\''+platname + '\''+';')
           cursor.execute(query)
           cursor.execute('commit;')
    except mysql.connector.Error as err:
           print("Exectue delete table failed.")
           print("Error: {}".format(err.msg))
    cursor.close()
    cn.close()
def Save_Snap(platname):
    print('请稍等！对积压短信进行转存储')
    cn = mysql.connector.connect(user = 'root',password = 'ceb1234',host = '127.0.0.1' ,database = 'mas')
    cursor = None
    try:
        cursor = cn.cursor()
        query = ('select *  from  mas_sms_outbox where  service_id= ' + '\''+platname + '\''+';')
        #print(query)
        cursor.execute(query)
        result_list =  cursor.fetchall()
        with open('Q_file.csv','w',encoding="utf-8") as f:
            for Col_line in result_list:
                Cloume =Col_line[1:]
                res_buff=""
                for Col_filed in Cloume:
                    res_buff=res_buff+str(Col_filed)+","
                f.write(res_buff+'\n')
        print("积压短信转储成功！")
    except mysql.connector.Error as err:
        print("执行积压短信转存过程失败！")
        print("Error: {}".format(err.msg))
    cursor.close()
    cn.close()
def main():
    plat = ['HUAWEIUC','ITIL','Solarwinds','SystemMon']
    while(True):
       try:
         os.system('cls')
         print('短信平台积压短信处理，请选择功能：')
         print('-------------------------------------------------------------------------------------------')
         print('1、查询MAS平台对接系统短信积压数量   2、删除对应系统在MAS平台的积压短信 \n')
         selection = input('请输入对应的功能序号: \n')
         #print(selection)
         if (selection == str(1)):
             print('你选择了查询MAS平台对接系统短信积压数量查询')
             platname = input('请输入平台名称 例如：HUAWEIUC  ITIL  Solarwinds  SystemMon \n')
             if (platname not in plat):
                 print('输入的对接系统名称非法!请参照平台名称示例！')
                 input('输入任意字符继续！')
             else:
                 res = Query_SMS_Box_Count(platname)
                 print( '该对接平台积压短信条数为 ：' + str(res[0]) + '\n')
                 input('输入任意字符继续！')
         elif(selection == str(2)):
             print('你选择了删除对应系统在MAS平台积压的短信')
             platname = input('请输入平台名称 例如：HUAWEIUC  ITIL  Solarwinds  SystemMon \n')

             if (platname not in plat):
                 print('输入的对接系统名称非法!请参照平台名称示例！')
                 input('输入任意字符继续！')
             else:
                 res = Query_SMS_Box_Count(platname)
                 print('该对接平台积压短信条数为 ：' + str(res[0]) + '\n')
                 Save_Snap(platname)
                 print('开始删除积压短信！！！ \n')
                 Delete_SMS_Box(platname)
                 print('积压短信已删除成功 \n')
                 input('输入任意字符继续！')
         elif(selection != str(1) or selection != str(2)):
             print('输入了无效的操作码！')
             break
       except  EOFError:
         print('你的选择结果无效，请重新输入')
         input('输入任意字符退出:')
         os.system('exit')

if __name__=='__main__':
    main()
