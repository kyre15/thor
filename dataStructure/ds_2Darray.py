from array import *

array2d = [[11, 12, 13, 14],
           [15, 16, 17, 18],
           [19, 20, 21],
           [22, 23, 24, 25]]

print("print value from index 0 in array2d: ")
print(array2d[0])
print("\nprint value from index x=1 y=1 . it should show 16")
print(array2d[1][1], "\n")

#print all value in matrix format
for x in array2d:
    for y in x:
        print(y,end = " ")
    print()

#update value in 2d array
print("\nUpdate Value:")
array2d[1] = [1, 2, 3]
array2d[3][3] = 30

for x in array2d:
    for y in x:
        print(y,end = " ")
    print()

#insert value to 2darray
print("\nInsert Value:")
array2d.insert(4, [31, 32])

for x in array2d:
    for y in x:
        print(y,end=" ")
    print()

#delete 2darray
print("\nDelete Value:")
del array2d[1]

for x in array2d:
    for y in x:
        print(y,end=" ")
    print()