# Count how many times each item appears in a list.
my_list = [1,2,2,3,4,4,4,5]
count_dict = {}
for item in my_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1
for item, count in count_dict.items():
    print(f"Item {item} appears {count} times.")