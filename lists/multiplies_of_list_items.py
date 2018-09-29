array = list(map(int, input("Enter the elements of list : ").split(' ')))
product = 1

for item in array:
    product *= item

print("Multiplies of List = ", product)