# Find the index of a value in a tuple (handle value not present).
my_tuple = (10, 20, 30, 40, 50)
value_to_find = 30
try:
    index = my_tuple.index(value_to_find)
    print(f"Index of {value_to_find} in tuple is: {index}")
except ValueError:
    print(f"{value_to_find} is not present in the tuple.")