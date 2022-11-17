count=0
a=int(input("starting number="))
b=int(input("ending number="))
i=a
while i>=b:
    if i%2==0:
        print("even number=",i)
        count=count+1
    else:
        print("odd number=",i)
    i=i-1
print("number of even number",count)
print("number of odd number",count)

