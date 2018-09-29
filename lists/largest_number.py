array = list(map(int, input("Enter the elements of list : ").split(' ')))

max_number = array[0]
for item in array:
    if item > max_number:
        max_number = item

print("Largest_number = ",max_number)

