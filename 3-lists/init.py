

test_list = ['12',3,['12',2.3],"what"]
print(test_list)
print('xxxxxxx')

print(test_list[3])
print('xxxxxxx')


print('what' in test_list)
print('xxxxxxx')


print(test_list[-2])
print('xxxxxxx')


for item in test_list:
    print(item)
print('xxxxxxx')


for i in range(len(test_list)):
    test_list[i] = ""
print(test_list)
print('xxxxxxx')


test_list.insert(-1,22)
print(test_list)
print('xxxxxxx')

test_list.append(11)
print(test_list)
print('xxxxxxx')

test_list.extend(["waka","waka"])
print(test_list)
print('xxxxxxx')

sliced_list = test_list[1:7]
print(sliced_list)
print('xxxxxx')

sliced_list[0:2] = [99,"this is you"]
print(sliced_list)
print('xxxxxx')

sliced_list.pop(-2)
print(sliced_list)
print('xxxxxx')

del sliced_list[1:3]
print(sliced_list)
print('xxxxxx')

sliced_list.remove('')
print(sliced_list)
print('xxxxxx')


if "waka" in sliced_list:
    print('found waka')
print('xxxxxx')


concat_list = sliced_list+test_list
print(concat_list)
print('xxxxxxxx')

print(concat_list *2)
print('xxxxxxxxx')


nums_list = [1,2,3,4,56,7,78,5,34,243,25234,1,32,14,7,6,12]
print(nums_list)
print(max(nums_list))
print(min(nums_list))
print(sum(nums_list))
print('xxxxxx')

string_x = 'this is a string'
list_string = list(string_x)
print(list_string)
print('xxxxxxxxx')

list_y = string_x.split()
print(list_y)
print('xxxxxxxxx')

prev_list = [1,2,3,45,64,321]
new_list = [i*3 for i in prev_list]
print(new_list)
print('xxxxxxxxx')


something = "this is something"
something_list = [i for i in something]
print(something_list)
print('xxxxxxxxx')


conditional_list = [item for item in prev_list if item>20]
print(conditional_list)
print('xxxxxxxx')