# FUNCTION

def my_function(param1 = 'default'):
    print('My first python function! {}'.format(param1))
my_function()

def hello():
    return 'hello'
print(hello())

def add_nums(n1, n2):
    if type(n1) == type(n2) == type(10):
        return n1 + n2;
    else:
        return 'Sorry, I need integers!'
print(add_nums('2','3'))

# Lambda Expression

# Filter
mylist = [1,2,3,4,5,6,7,8]

# def even_bool(num):
#     return num % 2 == 0;

evens = filter(lambda num: num % 2 == 0, mylist)
print(list(evens))

# Split
tweet = 'GO Sports! #Sports'
res = tweet.split('#')[1]
print(res)

# IN
print('x' in [1,2,3,'x'])
