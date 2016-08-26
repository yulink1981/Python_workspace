#coding:GBK
__metaclass__ = type
import paramiko,sys,re,os,getpass,time
from datetime import datetime
import paramiko.ssh_exception,paramiko.util
from subprocess import call

class Myssh():

    def verification_ssh(self,host,username,password,port,cmd): #此方法完成ssh方式登陆主机并执行一条命令功能，命令执行完毕即返回结果和命令执行状态，此方法不保持session
        paramiko.util.log_to_file("ssh.log")
        s=paramiko.SSHClient()
        s.load_system_host_keys()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname = host,port=int(port),username=username, password=password)
        print(cmd)
        stdin, stdout, stderr = s.exec_command(cmd)
        result = stdout.read()
        status = stderr.read()
        if result is  b'':
            print("command is fail! exec command is :" + cmd)
            reset = result
            s.close()
        else:
            reset = result
            s.close()
        return reset,status

    def sftp_get(self,ip,port,user,password,remote_path,remote_file,local_path,local_file):#此方法完成sftp.get功能，每次调用下载一个文件
        t_con = paramiko.Transport(ip,port)
        t_con.connect(username=user,password=password)
        sftp = paramiko.SFTPClient.from_transport(t_con)
        remote = os.path.join(remote_path,remote_file)
        local = os.path.join(local_path,local_file)
        sftp.get(remote,local)
        sftp.close()
        t_con.close()

    def sftp_mget(self,ip,port,user,password,remote_dir,local_dir):                        #此方法完成sftp.mget()功能，每次调用可下载多个文件
        t=paramiko.Transport((ip,port))
        t.connect(username=user,password=password)
        sftp=paramiko.SFTPClient.from_transport(t)
    #   files=sftp.listdir(dir_path)
        files=sftp.listdir(remote_dir)
        for f in files:
                print ('')
                print ('#########################################')
                print ('Beginning to download file  from %s  %s ' % (ip,datetime.now()))
                print ('Downloading file:',os.path.join(remote_dir,f))
                sftp.get(os.path.join(remote_dir,f),os.path.join(local_dir,f))
              # sftp.put(os.path.join(local_dir,f),os.path.join(remote_dir,f))
                print ('Download file success %s ' %datetime.now())
                print ('')
                print ('##########################################')
        t.close()

    def sftp_put(self,ip,port,user,password,local_path,local_file,remote_path,remote_file): #此方法完成sftp.putt功能，每次调用上传一个文件
        t_con = paramiko.Transport(ip,port)
        t_con.connect(username=user,password=password)
        sftp = paramiko.SFTPClient.from_transport(t_con)
        remote = os.path.join(remote_path,remote_file)
        local = os.path.join(local_path,local_file)
        sftp.put(local,remote)
        sftp.close()
        t_con.close()

    def sftp_mput(self,ip,port,user,password,local_dir,remote_dir):                         #此方法完成sftp.mput()功能，每次调用可上传多个文件
         t=paramiko.Transport((ip,port))
         t.connect(username=user,password=password)
         sftp=paramiko.SFTPClient.from_transport(t)
    #    files=sftp.listdir(dir_path)
         files=os.listdir(local_dir)
         for f in files:
                print ('')
                print ('#########################################')
                print ('Beginning to upload file  to %s  %s ' % (ip,datetime.now()))
                print ('Uploading file:',os.path.join(remote_dir,f))
                sftp.put(os.path.join(local_dir,f),os.path.join(remote_dir,f))
              # sftp.put(os.path.join(local_dir,f),os.path.join(remote_dir,f))
                print ('Uploading file success %s ' %datetime.now())
                print ('')
                print ('##########################################')
         t.close()











