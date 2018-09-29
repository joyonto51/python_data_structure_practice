dict1 = {'country': 'Bangladesh', 'division': 'Rangpur'}
dict2 = {'district': 'Dinajpur', 'Upzilla': 'Sadar'}
dict3 = {'Post': 'Kaliagonj', 'village': 'Rampur'}

my_dict = {}

my_dict.update(dict1)
my_dict.update(dict2)
my_dict.update((dict3))

print(my_dict)

another_dict = {}
for item in dict1,dict2,dict3:
     another_dict.update(item)

print(another_dict)