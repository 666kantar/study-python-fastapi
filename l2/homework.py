#Part 1
string = ("home")
integer = 4 
float = 4.1
bool = integer == float
list = [1, 2, 3]
dict = {'Name': 'Stas', 'Age': 4}
tuple = ('a', 'b', 'c')
none = None
print ('Part 1: ', type(string), type(integer), type(float), type(bool), type(list), type(dict), type(tuple), type(none))

#Part 2
a = integer == 4 or float == 4
b  = integer == 4 and float == 4
c = 'Stas' in dict['Name']
d = int(dict['Age']) == integer
e = dict['Age'] not in list and 5 in list or 3 in list 
print('Part 2: ', a, b, c, d, e)

#Part 3
num_str = 125
f = str(num_str)
print('Part 3', '_1: ', type(f), f)

message = 'Hi, my name is Python!'
message = message.replace('y','0').replace('i', '1') 
print('Part 3', '_2: ',message)

split_test = 'This is a split test'
string_split = split_test.split(' ')
string_join = ' '.join(string_split)
print('Part 3', '_3: ', string_split, string_join)
print('Part 3', '_4: ', len(string_join))

#Part 4
list_append = [1, 2, 3]
list_append.append(4)
print('Part 4', '_1: ', list_append)
list_append.append(5)
print(list_append)

list_extend = [4, 5, 6]
list_extend.extend([7,8,9])
print('Part 4', '_2: ', list_extend)
print('Part 4', '_3: ', list_extend.index(6))
print('Part 4', '_4: ', len(list_append))

#Part 5
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print('Part 5', '_1: ', dict_test['car'], dict_test['where'])
print('Part 5', '_2: ', dict_test.keys(), dict_test.values())
print('Part 5', '_3: ', dict_test.items())