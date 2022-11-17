#print(list(range(11)))
'''for i in range(10):
    print(i,",",end="")'''

'''for i in range (1,10):
    if i%2==0:
        print("even number",i)
    else:
        print("odd number",i)'''

l=(2,3,5,6,"abc")
for k in l:
    print(k)

i=0
while i<len(l):
    print(l[i])
    i=i+1

for m in range(len(l)):
    print(l[m])

