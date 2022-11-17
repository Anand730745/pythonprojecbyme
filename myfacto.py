n = int(input("Enter any number = "))
fact = 1
for i in range(n,0,-1):
    fact = fact * i

    if i == 1:
        print(i, "=", fact)
    else:
        print(i, "*", end="")

#print('factorial of',n,'is',fact)

