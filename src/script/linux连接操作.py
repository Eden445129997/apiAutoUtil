#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import paramiko

"""
实现远程服务器的连接与认证，对于该方法只有hostname是必传参数。
    connect():
        hostname 连接的目标主机
        port=SSH_PORT 指定端口
        username=None 验证的用户名
        password=None 验证的用户密码
        pkey=None 私钥方式用于身份验证
        key_filename=None 一个文件名或文件列表，指定私钥文件
        timeout=None 可选的tcp连接超时时间
        allow_agent=True, 是否允许连接到ssh代理，默认为True 允许
        look_for_keys=True 是否在~/.ssh中搜索私钥文件，默认为True 允许
        compress=False, 是否打开压缩

设置远程服务器没有在know_hosts文件中记录时的应对策略。目前支持三种策略：
    set_missing_host_key_policy()：
        AutoAddPolicy 自动添加主机名及主机密钥到本地HostKeys对象，不依赖load_system_host_key的配置。即新建立ssh连接时不需要再输入yes或no进行确认
        WarningPolicy 用于记录一个未知的主机密钥的python警告。并接受，功能上和AutoAddPolicy类似，但是会提示是新连接
        RejectPolicy 自动拒绝未知的主机名和密钥，依赖load_system_host_key的配置。此为默认选项

在远程服务器执行Linux命令的方法。
    exec_command()：

在当前ssh会话的基础上创建一个sftp会话。该方法会返回一个SFTPClient对象。
    open_sftp()：
        #基于当前连接的sftp对象，可以进行文件的上传等操作.
        sftp = client.open_sftp()
        sftp.put('test.txt','text.txt')

SFTPCLient作为一个sftp的客户端对象，根据ssh传输协议的sftp会话，实现远程文件操作，如上传、下载、权限、状态
        from_transport(cls,t) 创建一个已连通的SFTP客户端通道
        put(localpath, remotepath, callback=None, confirm=True) 将本地文件上传到服务器 参数confirm：是否调用stat()方法检查文件状态，返回ls -l的结果
        get(remotepath, localpath, callback=None) 从服务器下载文件到本地
        mkdir() 在服务器上创建目录
        remove() 在服务器上删除目录
        rename() 在服务器上重命名目录
        stat() 查看服务器文件状态
        listdir() 列出服务器目录下的文件
"""

def connect_ssh(host,username,password):
    # 使用ssh远程连接Linux
    ssh = paramiko.SSHClient()
    key = paramiko.AutoAddPolicy()
    ssh.set_missing_host_key_policy(key)
    try:
        ssh.connect(hostname=host, port=22, username=username,password=password ,timeout=5,allow_agent=True)
        return ssh
    except:
        print("连接linuxSSH失败，host：" + host)

def do_main():
    ssh = connect_ssh("10.113.248.110",'root','root')
    stdin, stdout, stderr = ssh.exec_command(
        "cd /;"
        "ls"
    )

    #返回的是一段list
    for i in stdout.readlines():
        print(i)

    ssh.close()

if __name__ == '__main__':
    do_main()