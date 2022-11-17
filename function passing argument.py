'''
There are 4 ays to pass argument into function
1. positional argument
2. keyword argument
3. varaible length argument
4. keyword varaible length argument

'''
#1. positional argument
def person(name,age):
    print(name)
    age=age+10
    print(age)
person("anand",12)


#2. keyword argument
def person(name,age):
    print(name)
    age=age+10
    print(age)
person(age=12,name="ram")


#3. varaible length argument
def varsum(x,*y):
    print(x)
    print(y)
    sum=x
    for i in y:
        sum=sum+i
        print(sum)
varsum(9,4,9)


def varsum1(*x):
    print(x)
    sum=0
    for i in x:
        sum=sum+i
    return sum
t=varsum1(4,5,6,9,7,5)
print(t)



#4. keyword varaible length argument
def persondata(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,"=",j)
persondata(name="suraj",age=34,city="gkp",mob="8858147186",school="sachidanand inter college")



















