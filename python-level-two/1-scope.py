# x = 25
#
# def my_func():
#     x = 50
#     return x
#
# print(x)
# print(my_func())
# my_func()
# print(x)

# LOCAL
# name = 'This is a global name!'
#
# def greet():
#     # name = 'Saddam'
#
#     def hello():
#         print('hello '+name)
#
#     hello()
#
# greet()
x = 50;

def func():
    # global x
    x = 1000
    return x
print('Before function call: ', x)
x = func()
print('Before function call: ', x)
