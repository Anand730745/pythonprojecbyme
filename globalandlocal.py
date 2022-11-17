
x=500
def test():
    global y
    y=1000
    x=5
    print("local=",x)
    d=globals()['x']
    print("global ko local me print karne ke liye(globals()['x']) use karte h=",d)
test()
print("local ko global me badlna(global y) se=",y)