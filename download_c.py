import socket
import os 

def sendfile(s):
    str1 = s.recv(1024)
    filename = str1.decode('utf-8')
    print('the server requests my file:%s',filename)
    if os.path.exists(filename):
        print('hello,i have  %s,begin to download' % filename)
        s.send(b'yes')
        s.recv(1024)
        size = 1024
        with open(filename,'rb') as f:
            while True:
                data = f.read(size)
                s.send(data)
                if len(data)<1024:
                    break
        print('%s download successfully' % filename)

    else:
        print('sorry,i have not %s' % filename)
        s.send(b'no')
s = socket.socket()
s.connect(('127.0.0.1',9999))

while True:
    sendfile(s)
s.close()