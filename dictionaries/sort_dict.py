import operator
my_dict ={1: 2, 2:3, 3:1, 4:5, 5:0}

print(my_dict)

sorted_dict = sorted(my_dict.items(), key=operator.itemgetter(1))
print("ascending order : ", sorted_dict)

sorted_dict = sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True)
print("descending order", sorted_dict)



sorted_dict = sorted(my_dict.items(), key=lambda kv:kv [1])
print("ascending order : ", sorted_dict)

sorted_dict = sorted(my_dict.items(), key=lambda kv:kv [1], reverse=True)
print("descending order", sorted_dict)

