import socket

ob=socket.socket()
ob.connect(('localhost',2302))
'''msg='hello this is first client'
ob.send(msg.encode('utf-8'))

#ob.close()'''

conn=True
while conn:
    msg=input('enter your message')
    ob.send(msg.encode('utf-8'))
    if msg=='no':
        conn=False
        ob.close()