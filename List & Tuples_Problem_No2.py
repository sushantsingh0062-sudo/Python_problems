# Remove duplicates from a list without using set()
my_list = [1,2,3,3,4]
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print("List after removing duplicates:", unique_list)