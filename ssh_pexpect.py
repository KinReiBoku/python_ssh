# coding:utf-8

from pexpect import spawn

# 接続情報
HOST = '192.168.43.50'
USER = 'default'
PASS = 'password'
PORT = 22
SIGN = ('# ', '$ ', '> ')

# ssh接続
ssh = spawn('ssh %s@%s -p %s' % (USER, HOST, PORT))
i = ssh.expect_exact(['yes', 'assword: ',SIGN[0], SIGN[1], SIGN[2]])
if i == 0:
	ssh.sendline('yes')
	ssh.expect_exact('assword: ')
ssh.sendline(PASS)
i = ssh.expect_exact([SIGN[0], SIGN[1], SIGN[2]])

# コマンド実行
if i == 2:
	ssh.sendline('dir')
else:
	ssh.sendline('ls -l')
ssh.expect_exact([SIGN[0], SIGN[1], SIGN[2]])

# 実行結果出力
print ssh.before

# 切断
ssh.close()
