#coding:GBK
from garp import Server_ssh_sftp
from garp import DB_Control
import telnetlib
import getpass
import re
import sys
import os
from datetime import datetime
import time
#引入SSH登陆设备python扩展包
import paramiko
import getopt

def main():
    sh = Server_ssh_sftp.Myssh()
    #res = sh.verification_ssh('10.1.35.72','root','admin1234',22,'ls  /opt/sfi/output/ipstatistics/ | grep garp*.xls')
    res = sh.verification_ssh('10.1.29.82','root','ceb1234',22,'ls -a /etc/ | grep man.*')

    for x in res:
        print(x)
    #curtime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    #garp_filename = "garp_" + curtime + ".xls"

    #remote_dir = '/opt/sfi/output/ipstatistics'
    #remote_file = garp_filename
    #print(remote_dir + '/' + remote_file)
    #local_dir = os.path.join(local_dir,f)
    #sh.sftp_get('10.1.35.75',22,'root','admin1234',)
if __name__ == '__main__':
    main()