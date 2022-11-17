class shop:
    shopkeeper=1
    room=1           #this is class variable


    def shop_info(self):
        self.name= 'Arya Provisinal Store'
        self.rent= 1000
        print(self.name)
s1=shop()
s1.shop_info()
s2=shop()
s2.shop_info()
s1.name='stark Provisinal Store'
print(s1.name)
print(s2.name)
s1.shop_info()
s2.shop_info()
s1.shopkeeper=12
print(s1.shopkeeper)
print(s2.shopkeeper)


