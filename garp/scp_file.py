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

def main():
    sh = Server_ssh_sftp.Myssh()
    #res = sh.verification_ssh('10.1.35.72','root','admin1234',22,'ls  /opt/sfi/output/ipstatistics/ | grep garp*.xls')

    curtime = time.strftime('%Y%m%d%H',time.localtime(time.time()))    #�õ���ǰСʱ�Ĵ���ļ������е�ʱ�䲿��
    garp_filename = "garp_" + curtime + "*" + ".xls"                  #��ϵõ���ǰСʱ�Ĵ���ļ���
    remote_path = '/home/yulink/workspace/aa/'                      #������Զ�̷������ļ�·��
    lscmd = 'ls -d ' + remote_path + garp_filename                     #��ϵ�½ִ��ls -d �ļ��� ����
    res = sh.verification_ssh('192.168.72.129','yulink','123123',22,lscmd)  #��½ִ��ls����鿴��ʱ����ļ�����

    remote_file = str("").join(list(bytes(res[0]).decode(encoding='utf-8'))[-24:-1]) # �Եõ��Ľ�����мӹ�����

    #for x in res:
    #    get_file_name = list(bytes(x).decode(encoding='utf-8').split('\n'))
    #    print(get_file_name)
    #curtime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    #garp_filename = "garp_" + curtime + ".xls"

    #remote_dir = '/opt/sfi/output/ipstatistics'
    remote_dir = remote_path
    #remote_file = garp_filename
    print(remote_dir + remote_file)
    local_dir = sys.path[0]
    print(local_dir)
    local_file = remote_file
    sh.sftp_get('192.168.72.129',22,'yulink','123123',remote_dir,remote_file,local_dir,local_file)

if __name__ == '__main__':
    main()