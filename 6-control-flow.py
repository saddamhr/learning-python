# if,elif, else Statements
if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
else:
    print('Last')

# LOOPS

# for loops in list
seq = [1,2,3,4,5,6]
for item in seq:
    print(item)

# for loop in dictionary
d = {'saddam':1, 'Hossain':2,'Rakib':3}
for x in d:
    print(x)
    print(d[x])

# for loop in tuple unpacking
mypairs = [(1,2),(3,4),(5,6)]
for (x,y) in mypairs:
    print(y)
    print(x)
# while loop
i = 1
while i < 5:
    print('i is :{}'.format(i))
    i = i + 1

# range
for i in range(10):
    print(i)
    
# list comprehension
nums = [1,2,3,4]
# out = []
# for num in x:
#     out.append(num ** 2)
# print(out)
out = [x ** 2 for x in nums]
