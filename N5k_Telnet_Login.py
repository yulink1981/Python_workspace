# -*- coding: gbk -*-
import telnetlib,re,os,sys,time
from datetime import datetime

#__Login__ = "Logon successfule"
#__Failure__ = "Logon failure"
def N5k_Telnet_logon(username,password,ipaddr):
    curdate = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    try:
        print('--------------------开始登陆设备--------------------')
        tn = telnetlib.Telnet(ipaddr)
        tn.read_until(b"login:")
        tn.write(username.encode('ascii')+b"\n")
        print(ipaddr+'--------------------输入用户成功--------------------')
        tn.read_until(b"Password:")
        try:
            tn.write(password.encode('ascii')+b"\n")
            tn.read_until(b"#")
            print('--------------------输入密码成功--------------------')
            tn.write(b"\n")
            return  tn

        except EOFError:
            tn.close
            print('输入用户名密码无效！')
            return "0"


    except ConnectionRefusedError:
        print('登陆'+ipaddr+'失败，请确认IP可访问')
        tn.close()
        return "0"
    except OSError:
        print('登陆'+ipaddr+'失败，请确认IP可访问')
        tn.close()
        return "0"
    except EOFError:
        print('登陆'+ipaddr+'失败，请确认IP可访问')
        tn.close()
        return "0"

def N5k_Telnet_logon(username,password,ipaddr,cmd[],expr):

    res = []
    return res

def main():
    res = N5k_Telnet_logon("checklist","ceb12345","10.1.100.193")


if __name__ == "__main__":
     print(main())