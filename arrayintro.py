from array import *
import time
l=array('f',[2,3,4,55,23,21,2.6,67])
print(l)
for i in l:
    #time.sleep(1)
    print(i)

for j in range(len(l)):
    print(l[j])

print(l.buffer_info())
