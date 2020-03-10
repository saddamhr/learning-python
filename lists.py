# LISTS
numberlist = [1,2,3]
mixedlist = ['abcd',1,2,3,23.2,True,'efgh',[1,2,3]]

#Lists Length
print(len(numberlist))

mylist = ['a','b','c','d','e']
print(mylist[1:])
print(mylist[:3])
mylist[0] = 'NEW ITEM'
# print(mylist)

# Append Extend
mylist.append(['x','y','z'])
mylist.extend(['x','y','z'])
print(mylist)

# pop elementes from list
print(mylist.pop(0))

# reverse list
mylist.reverse()
print(mylist)

# sort list
newlist = [2,4,1,7,3]
newlist.sort()
print(newlist)

# nested list
nestedlist = [1,2,['x','y','z']]
print(nestedlist[2][0])

# list comprehension
matrix = [[1,2,3],[4,5,6],[7,8,9]]
first_col = [row[0] for row in matrix]
print(first_col)
