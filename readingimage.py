f=open('niraj2.gif','rb')
f1=open('mukesh.gif','wb')
#print(f.read())
for data in f:
    f1.write(data)


