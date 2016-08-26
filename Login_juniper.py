# -*- coding: gbk -*-
import telnetlib
import getpass
import re
import sys
import os
from datetime import datetime
import paramiko
import getopt

import time

def main():
    os.system('cls')
    user='checklist'
    password='ceb12345'
    msg_cmdcheck_all=b''
    F=open('ip.txt')
    for ttt in F:
        tt=ttt.strip()
        hh=re.findall('\d+\.\d+\.\d+\.\d+',tt)
        bb=re.findall('Juniper|netscreen',tt)
        HOST=''.join(hh)
        dd=''.join(bb)
        print(bb)
        print(HOST)
        try:
            if dd =='Juniper':
                s = paramiko.SSHClient()
                s.load_system_host_keys()
                s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                s.connect(HOST,22,user,password)
                ssh = s.invoke_shell()
                time.sleep(0.5)
                list1=['show route | no-more \n','show config |display set | no-more \n']
                for cmd in list1:
                    time.sleep(0.1)
                    ssh.send(cmd)
                    time.sleep(1)
                    buff=b''
                    while not buff.endswith(b'> '):
                        resp = ssh.recv(999999)
                        buff +=resp
                    print("HOST:",HOST,cmd[5:11])
                    out = open(r'c:\test\%s_%s.conf' %(HOST,cmd[5:11]),'w')
                    out.write(str(buff.decode("utf-8")))
                    out.close()
                ssh.send("exit\n")
                ssh.close()
            elif dd=='netscreen':
                sh = paramiko.SSHClient()
                sh.load_system_host_keys()
                sh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                paramiko.util.log_to_file('paramiko.log')
                sh.connect(HOST,22,user,password)
                ssh = sh.invoke_shell()
                time.sleep(1)
                #stdin,stdout,stderr = s.exec_command('show version')
                ssh.send('set console page 0 \n get config \n')
                time.sleep(1)
                buff = b''

                while not buff.endswith(b'> '):
                    resp = ssh.recv(999999)
                    buff +=resp
                print("HOST:",HOST,dd)
                with open(r'c:\test\%s.conf' %(HOST),'w') as f:
                    f.write(buff.decode('ascii','ignore'))
                    #f.write(str(buff.decode("utf-8")))
                    f.close()
                ssh.send("exit\n")
                sh.close()
            else:
                print ("11111111111111")
        except paramiko.ssh_exception.AuthenticationException:
            print("连接或登录失败，请检查服务器IP和用户名密码！")
            ssh.close()
        except TimeoutError:
            print("连接超时！")
            continue


if __name__=='__main__':
    main()





