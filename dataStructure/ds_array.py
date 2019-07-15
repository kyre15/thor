from array import *

#create array
array1 = array('i', [10,20,30,40,50])
print("Original Array")
for x in array1:
    print(x)

#delete operation
array1.remove(50)
print("\n50 remove from array")
for x in array1:
    print(x)

#search operation
print("\nSearch index for value 30 in array: ", array1.index(30))

#update operation
array1[1] = 21
print("\nupdate value on index 1 in array")
for x in array1:
    print(x)
