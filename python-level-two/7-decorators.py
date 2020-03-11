# def hello(name='Rakib'):
#     print('THE HELLO() FUNCTION HAS BEEN RUN')
#     def greet():
#         return 'THIS STRING IS INSIDE GREET()'
#     def welcome():
#         return 'THIS STRING IS INSIDE WELCOME'
#     print(greet())
#     print(welcome())
#     print('End of hello()')
# hello()

# def hello(name='jose'):
#     print('THE HELLO() FUNCTION HAS BEEN RUN')
#     def greet():
#         return 'THIS STRING IS INSIDE GREET()'
#     def welcome():
#         return 'THIS STRING IS INSIDE WELCOME'
#
#     if name == 'jose':
#         return greet
#     else:
#         return welcome
#
#
# x = hello()
# print(x())

# pass in function as argument
# def hello():
#     return 'Hi JOSE!'
# def other(func):
#     print('hello')
#     print(func)
# # other(hello)
# print(hello)
def new_decorator(func):

    def wrap_func():
        print('CODE HERE BEFORE EXECUTING FUNC')
        func()
        print('FUNC() HAS BEEN CALLED')

    return wrap_func
    
@new_decorator
def func_needs_decorator():
    print('THIS FUNCTION IS IN NEED OF A DECORATOR')

# func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()
