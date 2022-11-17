from numpy import *
arr1=array([
    [1,1,1],
    [2,2,2],
    [3,3,3]

])
print(arr1)

arr2=array([
    [3,3,3],
    [2,2,2],
    [1,1,1]
])
print(arr2)

print(arr1+arr2)

print(dot(arr1,arr2))
print(arr1@arr2)