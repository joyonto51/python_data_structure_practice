array = list(map(int, input("Enter the elements of list : ").split(' ')))
sum = 0

for item in array:
    sum += item

print("sum = ", sum)