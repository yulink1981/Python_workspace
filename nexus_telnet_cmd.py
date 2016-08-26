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
        print('--------------------开始登陆设备--------------------')
        tn = telnetlib.Telnet(ipaddress)
        tn.read_until(b"login:")
        tn.write(username.encode('ascii')+b"\n")
        print(ipaddress+'--------------------输入用户成功--------------------')
        tn.read_until(b"Password:")
        try:
            tn.write(password.encode('ascii')+b"\n")
            tn.read_until(b"#")
            print('--------------------输入密码成功--------------------')
            tn.write(b"\n")
            FH=tn.read_until(b"#")
            fuhao=FH.decode('ascii')
            fuhaoall=fuhao[2:-1]
            print('--------------------操作的设备名称:'+fuhaoall+"--------------------")
            tn.write(b"terminal length 0\n")
            msg=tn.read_until(b"#")

            


            
            tn.write(b"exit\n")
            print(fuhaoall+'抓取设备配置完成！')
            tn.close
            return("1")

        except EOFError:
            tn.close
            print('输入用户名密码无效！')
            return None
       
            
    except ConnectionRefusedError:
        print('登陆'+ipaddress+'失败，请确认IP可访问')
        return None
    except OSError:
        print('登陆'+ipaddress+'失败，请确认IP可访问')
        return None
    except EOFError:
        print('登陆'+ipaddress+'失败，请确认IP可访问')
        return None

def main():
    res = nexus_telnet_cmd("checklist","ceb12345","10.1.100.193")


if __name__ == "__main__":
     print(main())



