'''
str2="namaskar doston main amitabh bacchan"
print(str2)
print(len(str2))
print(str2.capitalize())
print(str2.upper())
print(str2.lower())
print(str2.title())
print(str2.swapcase())


name=input('enter your name=')
if name.isalpha():
    print(name.upper())
else:
    print("not valid name")
print(name.upper())


age=input("enter your age=")
#print(age)
if age.isdigit():
    print(age)
else:
    print("not valid age")


enrollment=input("enter your enrollment no=")
#print(enrollment)
if enrollment.isalnum():
    print(enrollment)
else:
    print('not valid enrollment no')
'''
name=input('enter your name=')
print(name.strip('#'))
print(name.strip('$'))
print("thank you")



name=input('enter your name=')
if name.lstrip():
    print("name")
else:
    print("not valid name")


str2="my name is anand and i think that anand is best name"
search="anand"
print(str2.find(search))
rep="mukesh"
print(str2.replace(search,rep))

#if str2.find(search):
    #print(str2.replace(search,rep))
print(str2.index(search))
print(str2.endswith('d'))
print(str2.split(' '))

l=eval(input('enter the elements='))
print(l)
print(type(l))


















