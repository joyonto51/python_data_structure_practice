array = list(map(int, input("Enter the elements of list : ").split(' ')))

min_number = array[0]
for item in array:
    if item < min_number:
        min_number = item

print("smallest_number = ",min_number)