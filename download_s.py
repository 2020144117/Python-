import socket
import os
s = socket.socket()
s.bind(('127.0.0.1',9999))
s.listen(2)
print('等待连接')

coon,addr = s.accept()
while True:
    filename = 'D:/socket.txt'
    print('get file %s' % filename)

    conn.send(filename.encode('utf-8'))
    str1 = conn.recv(1024)
    str2 = str1.decode('utf-8')
    if str2 == 'no':
        print('%s get the file is failed'% filename)
    else:
        conn.send(b'ready')
        temp = filename.split('/')
        myname = 'my-'+temp[len(temp)-1]
        size = 1024
        with open(myname,'wb') as f:
            while True:
                data = conn.recv(size)
                f.write(data)
                if len(data)<size:
                    break
    conn.close()
    print('download file is %s.' % myname)
s.close()