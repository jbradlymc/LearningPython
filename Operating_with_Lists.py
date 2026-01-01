my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
clean_list = []

for number in my_list:
    if number not in clean_list:
        clean_list.append(number)

my_list[:] = clean_list[:]

print("The list with unique elements only:")
print(my_list)
