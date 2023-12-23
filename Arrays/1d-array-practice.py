import array

# create array and traverse, access element via index
arr = array.array('i',[1,2,3,4,5,6,7])

for i in range(len(arr)):
    print(arr[i])

# append value to array
arr.append(22)

#insert value into array using insert
arr.insert(4,222)

# extend python array using extend
arr.extend(range(99,105))

# add items into array using fromlist method
listA = [8,9,10,11]
arr.fromlist(listA)

# remove element with value of 6 from array using remove method
arr.remove(6)

# remove last element using pop()
arr.pop()

# get element using index()
print(arr.index(4))

# reverse using the reverse()
arr.reverse()
print(arr)

# get array buffer info
print(arr.buffer_info(), 'buffer info')

# get number of occurnces of an element
print(arr.count(22))

# convert array to string using the tostring()
# tempS = arr.tostring()
# print('tostring ',tempS)

# convert array to list toList()
list2 = arr.tolist()
print(list2)


# slice an array
arr_temp = arr[2:7]
print(arr_temp)