try:
    print("G.D.PUBLIC SCHOOL JAKHIRA CHAURAHA DIST-MAHARAJGANJ")
    a=int(input("marks in hindi="))
    b=int(input("marks in english="))
    c=int(input("marks in math="))
    d=int(input("marks in science="))
    t=(a+b+c+d)/400*100
    print("t=",t)
    if t<33:
        print("failed")
    elif (t>=33) and (t<45):
     print("passed with 3rd division and grade C")
    elif (t>=45) and (t<70):
        print("passed with 2nd division and grade B")
    elif (t>=70) and (t<100):
        print("passed with 1st division and grade A")

except ValueError as e:
    print("not valid character")

except Exception as e:
    print("something went wrong")
finally:
    print("thank you")