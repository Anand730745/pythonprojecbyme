stock=20
n=int(input("enter the quantity of of chocolates="))
i=1
while i<=n:
    if i<=stock:
        print("collect chocolate",i)
    else:
        print("sorry! out of stock")
        break
    i=i+1
else:  # when loop runs properly
    print("thank you please visit again")


