array = list(map(str, input("Enter some word/number : ").split(' ')))

count = 0

for item in array:
    if len(item)>=2 and item[0] == item[-1]:
        count+=1

print(count)