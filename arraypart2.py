try:
    import time
    from array import *
    arr=array('i',[])
    n=int(input("how many elements you want to store in array="))
    for i in range(n):
        x=int(input("enter the elements ="))
        arr.append(x)
    for i in arr:
        #time.sleep(1)
        print(i)
        loc=0
    search = int(input("which element do you want to search="))
    for i in arr:
        if i==search:
            print("element found",loc)
            break
        loc=loc+1
    else:
         print("element does not found")
except Exception as e:
    print("something went wrong")















