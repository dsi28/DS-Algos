# day1: 11,12,10,6
# day2: 10,14,11,5
# day3: 12,17,12,8
# day4: 15,18,14,9

import numpy as np

array_2d = np.array([[11,12,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(array_2d)
print('xxxxxxxxxxx')

array_2d_insert = np.insert(array_2d,1,[4,4,4,4], 1)
print(array_2d_insert)
print('xxxxxxxxxxx')
array_2d_insert = np.insert(array_2d,2,[7,7,7,7], 0)
print(array_2d_insert)
print('xxxxxxxxxxx')

array_2d_append = np.append(array_2d, [[0],[0],[0],[0]],1)
print(array_2d_append)
print('xxxxx')


def get_element(ar,rowIndex, colIndex):
    if rowIndex>= len(ar) or colIndex>=len(ar[0]):
        print('index issue')
    else: 
        print(ar[rowIndex][colIndex])

get_element(array_2d_append, 2,3) 
print('xxxxx')


def traverse2DArray(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i,j])
traverse2DArray(array_2d_append)
print('xxxxx')

def search2dArray(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]==target:
                print(f"found {target} row {i} and column {j}")
    print('done')
search2dArray(array_2d_append,22)
print('xxxxx')

print(array_2d_append)
delete_2d_array = np.delete(array_2d_append,1,0)
print(delete_2d_array)
print('xxxxx')