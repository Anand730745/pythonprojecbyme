from numpy import *
#isme id=id hoga aur index number change=index number change(all the id and index value will same)
print("aliasing ")
arr1=array([3,5,7,9,11,15,17])
print(arr1,id(arr1))
arr2=arr1
print(arr2,id(arr2))
arr2[0]=100
print(arr2,id(arr2))
print(arr1,id(arr1))

print("view method--Shallow copy")
#isme (id) equal nhi (id) hoga aur index number change=index number change (id isnot equal to another id but number change value will be equal change )
arr3=array([14,56,52,20,25])
print(arr3,id(arr3))

arr4=arr3.view()

print(arr4,id(arr4))

arr4[0]=300
print(arr4,id(arr4))
print(arr3,id(arr3))

print("Copy method--Deep Copy")
#isme (id) equal nhi (id) hoga aur index number change nhi hoga, keval pahle wale array ko change karega)
arr5=array([13,35,57,68,79])
print(arr5,id(arr5))

arr6=arr5.copy()
print(arr6,id(arr6))

arr5[0]=700
print(arr5,id(arr5))
print(arr6,id(arr6))





