# Remove a key-value pair from a dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_remove = 'b'
if key_to_remove in my_dict:
    del my_dict[key_to_remove]
print("Dictionary after removing key '{}': {}".format(key_to_remove, my_dict))