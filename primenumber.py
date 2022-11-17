'''n=3333

i=2
while i<=n-1:
    if n%i==0:
        print("not prime number")
        break
    i = i + 1
else:
    print("prime number")'''

n=2
while n<=20:
    print(n)
    i=2
    while i<=n-1:
        if i % n == 0:
            #print("not prime number",n)
            break
        i=i+1
    else:
        print("prime number",n)
    n=n+1






