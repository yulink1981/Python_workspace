# -*- coding: gbk -*-
import telnetlib,re,os,sys,time
from datetime import datetime

#__Login__ = "Logon successfule"
#__Failure__ = "Logon failure"
def N5k_Telnet_logon(username,password,ipaddr):
    curdate = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    try:
        print('--------------------��ʼ��½�豸--------------------')
        tn = telnetlib.Telnet(ipaddr)
        tn.read_until(b"login:")
        tn.write(username.encode('ascii')+b"\n")
        print(ipaddr+'--------------------�����û��ɹ�--------------------')
        tn.read_until(b"Password:")
        try:
            tn.write(password.encode('ascii')+b"\n")
            tn.read_until(b"#")
            print('--------------------��������ɹ�--------------------')
            tn.write(b"\n")
            return  tn

        except EOFError:
            tn.close
            print('�����û���������Ч��')
            return "0"


    except ConnectionRefusedError:
        print('��½'+ipaddr+'ʧ�ܣ���ȷ��IP�ɷ���')
        tn.close()
        return "0"
    except OSError:
        print('��½'+ipaddr+'ʧ�ܣ���ȷ��IP�ɷ���')
        tn.close()
        return "0"
    except EOFError:
        print('��½'+ipaddr+'ʧ�ܣ���ȷ��IP�ɷ���')
        tn.close()
        return "0"

def N5k_Telnet_logon(username,password,ipaddr,cmd[],expr):

    res = []
    return res

def main():
    res = N5k_Telnet_logon("checklist","ceb12345","10.1.100.193")


if __name__ == "__main__":
     print(main())