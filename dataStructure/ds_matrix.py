from numpy import *

a = array(
    [
        ['Mon', 18, 20, 22, 17],
        ['Tue', 11, 18, 21, 18],
        ['Wed', 15, 21, 20, 19],
        ['Thu', 11, 20, 22, 21],
        ['Fri', 18, 17, 13, 22],
        ['Sat', 12, 22, 20, 18],
        ['Sun', 13, 15, 19, 16]
    ]
)

m = reshape(a, (7, 5))
print(m)

#print array
print("\nPrint matrix index 2: ")
print(m[2])
print("\nPrint matirx with index 2d: ")
print(m[0][3])

#add new row to matrix
m_r = append(m, [['Avr', 12, 15, 13, 11]],0)
print("\nAdd new row: ")
print(m_r)

#add new column to matrix
m_c = insert(m,[5],[[1], [2], [3], [4], [5], [6], [7]], 1)
print("\nAdd new Column:")
print(m_c)

#delete row from matrix

m = delete(m,[2], 0)
print("\nDelete row from matrix:")
print(m)

#delete column from matrix
m = delete(m, [0], 1)
print("\nDelete column from matrix:")
print(m)

#Update row to matrix
m[0] = ['12', '13', '90', '17']
print("\nUpdate matrix")
print(m)