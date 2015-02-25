# coding:utf-8

import paramiko

# 接続情報
HOST = '192.168.43.50'
USER = 'default'
PASS = 'password'
PORT = 22

# ssh接続
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, username=USER, password=PASS, port=PORT)

# コマンド実行
stdin, stdout, stderr = ssh.exec_command('ls -l')

# 実行結果出力
for line in stdout.read().split('\n'):
	print line

# 切断
ssh.close()
