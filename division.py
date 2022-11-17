try:
    print("mathematics is our life")
    a=int(input("enter nominator="))
    b=int(input("enter denominator="))
    D=a/b
    print(D)
except ValueError as e:
    print("you enter a wrong character")
except ZeroDivisionError as e:
    print("you can't use the zero")
except Exception as e:
    print("something went wrong")

finally:
    print("thank you")




