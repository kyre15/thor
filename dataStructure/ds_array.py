from array import *


def print_array(array):
    for x in array:
        print(x)


# create array
array1 = array('i', [10, 20, 30, 40, 50])
print("Original Array")
print_array(array1)

# delete operation
array1.remove(50)
print("\n50 remove from array")
print_array(array1)

# search operation
print("\nSearch index for value 30 in array: ", array1.index(30))

# update operation
array1[1] = 21
print("\nupdate value on index 1 in array")
print_array(array1)

# insert operation
print("\nadd 60 to index 4 to array")
array1.insert(4, 60)
print_array(array1)
