#coding:GBK
import Server_ssh_sftp
import DB_Control
import telnetlib
import getpass
import re
import sys
import os
from datetime import datetime
import time
#����SSH��½�豸python��չ��
import paramiko
import getopt

def get_file():
    sh = Server_ssh_sftp.Myssh()
    curtime = time.strftime('%Y%m%d%H',time.localtime(time.time()))    #�õ���ǰСʱ�Ĵ���ļ������е�ʱ�䲿��
    print("��ʼִ�г���ִ��ʱ�䣺" + curtime)
    garp_filename = "garp_" + curtime + "*" + ".xls"                  #��ϵõ���ǰСʱ�Ĵ���ļ���
    remote_path = '/home/yulink/workspace/aa/'                      #������Զ�̷������ļ�·��
    lscmd = 'ls -d ' + remote_path + garp_filename                     #��ϵ�½ִ��ls -d �ļ��� ����
    res = sh.verification_ssh('192.168.72.129','yulink','123123',22,lscmd)  #��½ִ��ls����鿴��ʱ����ļ�����
    if bytes(res[0]) ==b'':
     print('����ִ����ϣ���û���ҵ��ļ�')
    else:
     remote_file = str("").join(list(bytes(res[0]).decode(encoding='utf-8'))[-24:-1]) # �Եõ��Ľ�����мӹ�����
     print("�õ��ļ����ƣ�" + remote_file)
    remote_dir = remote_path
    local_dir = sys.path[0]
    local_file = remote_file
    print("��ʼget�ļ���" +  remote_file)
    sh.sftp_get('192.168.72.129',22,'yulink','123123',remote_dir,remote_file,local_dir,local_file)
    print("�ļ�:" + remote_file + "���سɹ���" )
    return remote_file
def insert_data():
    with open(get_file()) as sourcefile:
        sourcefile.readline()
def main():
    insert_data()


if __name__ == '__main__':
    main()