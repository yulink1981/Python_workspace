# -*- coding: gbk -*-
import mysql.connector
import os
def Query_SMS_Box_Count(platname):
    print('��ѯMASƽ̨�Խ�ϵͳ���Ż�ѹ����')
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
    print('ɾ��' + platname +'ϵͳ��MASƽ̨�Ļ�ѹ����')
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
    print('���Եȣ��Ի�ѹ���Ž���ת�洢')
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
        print("��ѹ����ת���ɹ���")
    except mysql.connector.Error as err:
        print("ִ�л�ѹ����ת�����ʧ�ܣ�")
        print("Error: {}".format(err.msg))
    cursor.close()
    cn.close()
def main():
    plat = ['HUAWEIUC','ITIL','Solarwinds','SystemMon']
    while(True):
       try:
         os.system('cls')
         print('����ƽ̨��ѹ���Ŵ�����ѡ���ܣ�')
         print('-------------------------------------------------------------------------------------------')
         print('1����ѯMASƽ̨�Խ�ϵͳ���Ż�ѹ����   2��ɾ����Ӧϵͳ��MASƽ̨�Ļ�ѹ���� \n')
         selection = input('�������Ӧ�Ĺ������: \n')
         #print(selection)
         if (selection == str(1)):
             print('��ѡ���˲�ѯMASƽ̨�Խ�ϵͳ���Ż�ѹ������ѯ')
             platname = input('������ƽ̨���� ���磺HUAWEIUC  ITIL  Solarwinds  SystemMon \n')
             if (platname not in plat):
                 print('����ĶԽ�ϵͳ���ƷǷ�!�����ƽ̨����ʾ����')
                 input('���������ַ�������')
             else:
                 res = Query_SMS_Box_Count(platname)
                 print( '�öԽ�ƽ̨��ѹ��������Ϊ ��' + str(res[0]) + '\n')
                 input('���������ַ�������')
         elif(selection == str(2)):
             print('��ѡ����ɾ����Ӧϵͳ��MASƽ̨��ѹ�Ķ���')
             platname = input('������ƽ̨���� ���磺HUAWEIUC  ITIL  Solarwinds  SystemMon \n')

             if (platname not in plat):
                 print('����ĶԽ�ϵͳ���ƷǷ�!�����ƽ̨����ʾ����')
                 input('���������ַ�������')
             else:
                 res = Query_SMS_Box_Count(platname)
                 print('�öԽ�ƽ̨��ѹ��������Ϊ ��' + str(res[0]) + '\n')
                 Save_Snap(platname)
                 print('��ʼɾ����ѹ���ţ����� \n')
                 Delete_SMS_Box(platname)
                 print('��ѹ������ɾ���ɹ� \n')
                 input('���������ַ�������')
         elif(selection != str(1) or selection != str(2)):
             print('��������Ч�Ĳ����룡')
             break
       except  EOFError:
         print('���ѡ������Ч������������')
         input('���������ַ��˳�:')
         os.system('exit')

if __name__=='__main__':
    main()
