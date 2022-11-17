import socket

ob=socket.socket()
ob.bind(('192.168.90.42',2302))
ob.listen(4)
clientobject,add=ob.accept()
print('server is ready to accept connection')
print('connected with this address',add)
'''gotmsg=clientobject.recv(1024)
gotmsg.decode('utf-8')
print(gotmsg)
#ob.close()'''
conn=True
while conn:
    gotmsg=clientobject.recv(1024)
    gotmsg.decode('utf-8')
    print(gotmsg)
    if len(gotmsg)==0:
        conn=False
        ob.close()





















