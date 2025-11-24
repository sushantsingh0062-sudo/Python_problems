# Remove duplicate characters from a string.
input_string = input("Enter a string: ")
unique_chars = ""
for char in input_string:
    if char not in unique_chars:
        unique_chars += char
print("String after removing duplicate characters:", unique_chars)
