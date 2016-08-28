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
#引入SSH登陆设备python扩展包
import paramiko
import getopt

def get_file():
    sh = Server_ssh_sftp.Myssh()
    curtime = time.strftime('%Y%m%d%H',time.localtime(time.time()))    #得到当前小时的大概文件名称中的时间部分
    print("开始执行程序，执行时间：" + curtime)
    garp_filename = "garp_" + curtime + "*" + ".xls"                  #组合得到当前小时的大概文件名
    remote_path = '/home/yulink/workspace/aa/'                      #定义了远程服务器文件路径
    lscmd = 'ls -d ' + remote_path + garp_filename                     #组合登陆执行ls -d 文件名 命令
    res = sh.verification_ssh('192.168.72.129','yulink','123123',22,lscmd)  #登陆执行ls命令查看本时间段文件名称
    if bytes(res[0]) ==b'':
     print('命令执行完毕，但没有找到文件')
    else:
     remote_file = str("").join(list(bytes(res[0]).decode(encoding='utf-8'))[-24:-1]) # 对得到的结果进行加工处理
     print("得到文件名称：" + remote_file)
    remote_dir = remote_path
    local_dir = sys.path[0]
    local_file = remote_file
    print("开始get文件：" +  remote_file)
    sh.sftp_get('192.168.72.129',22,'yulink','123123',remote_dir,remote_file,local_dir,local_file)
    print("文件:" + remote_file + "下载成功！" )
    return remote_file
def insert_data():
    with open(get_file()) as sourcefile:
        sourcefile.readline()
def main():
    insert_data()


if __name__ == '__main__':
    main()