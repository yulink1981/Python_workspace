# -*- coding: gbk -*-
import telnetlib
import re
import sys
import os
from datetime import datetime
import time
import re
def nexus_telnet_cmd(username,password,ipaddress):
    curdate=time.strftime('%Y-%m-%d',time.localtime(time.time()) )
    try:
        print('--------------------��ʼ��½�豸--------------------')
        tn = telnetlib.Telnet(ipaddress)
        tn.read_until(b"login:")
        tn.write(username.encode('ascii')+b"\n")
        print(ipaddress+'--------------------�����û��ɹ�--------------------')
        tn.read_until(b"Password:")
        try:
            tn.write(password.encode('ascii')+b"\n")
            tn.read_until(b"#")
            print('--------------------��������ɹ�--------------------')
            tn.write(b"\n")
            FH=tn.read_until(b"#")
            fuhao=FH.decode('ascii')
            fuhaoall=fuhao[2:-1]
            print('--------------------�������豸����:'+fuhaoall+"--------------------")
            tn.write(b"terminal length 0\n")
            msg=tn.read_until(b"#")

            


            
            tn.write(b"exit\n")
            print(fuhaoall+'ץȡ�豸������ɣ�')
            tn.close
            return("1")

        except EOFError:
            tn.close
            print('�����û���������Ч��')
            return None
       
            
    except ConnectionRefusedError:
        print('��½'+ipaddress+'ʧ�ܣ���ȷ��IP�ɷ���')
        return None
    except OSError:
        print('��½'+ipaddress+'ʧ�ܣ���ȷ��IP�ɷ���')
        return None
    except EOFError:
        print('��½'+ipaddress+'ʧ�ܣ���ȷ��IP�ɷ���')
        return None

def main():
    res = nexus_telnet_cmd("checklist","ceb12345","10.1.100.193")


if __name__ == "__main__":
     print(main())



