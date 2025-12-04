# Find common values between two dictionaries.
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'x': 3, 'y': 4, 'z': 2}
common_values = set(dict1.values()) & set(dict2.values())
print("Common Values:", common_values)