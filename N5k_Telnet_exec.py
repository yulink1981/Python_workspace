# -*- coding: gbk -*-
import telnetlib,re,os,sys,time
from datetime import datetime
from N5k_Telnet_Login import N5k_Telnet_logon


#tn = N5k_Telnet_logon("checklist","ceb12345","10.1.100.193")
def N5k_telnet_exec(tn,cmd):
            tn.write(b"\n")
            FH=tn.read_until(b"#")
            fuhao=FH.decode('ascii')
            fuhaoall=fuhao[2:-1]
            print('--------------------操作的设备名称:'+fuhaoall+"--------------------")
            tn.write(cmd)
            msg=tn.read_until(b"#")
            tn.write(b"exit\n")
            print(fuhaoall+'抓取设备配置完成！')
            tn.close
            return msg


def main():
    N5k_telnet_exec()

if __name__ == "__main__":
  main()
