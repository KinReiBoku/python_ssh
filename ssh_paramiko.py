# coding:utf-8

import paramiko

# �ڑ����
HOST = '192.168.43.50'
USER = 'default'
PASS = 'password'
PORT = 22

# ssh�ڑ�
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, username=USER, password=PASS, port=PORT)

# �R�}���h���s
stdin, stdout, stderr = ssh.exec_command('powershell .\\New-Folder.ps1')

# ���s���ʏo��
for line in stdout.read().split('\n'):
	print line

# �ؒf
ssh.close()