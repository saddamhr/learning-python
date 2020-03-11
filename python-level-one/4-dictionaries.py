# DICTIONARIES

# create dictionaries and grab element from it
my_dict = {'key1':123,'key2':'value2','key3':{'123':[1,2,'grabMe']}}
print(my_dict['key3']['123'][2].upper())

my_stuff = {'lunch':'pizza','bfast':'eggs'}

# reassign into dictionarie
my_stuff['lunch'] = 'burger'
print(my_stuff)

# add new element into dictionaries
my_stuff['dinner'] = 'pasta'
print(my_stuff)
