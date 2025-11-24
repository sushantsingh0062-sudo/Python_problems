# Print characters at even index positions.and
input_string = input("Enter a string: ")
even_indexed_chars = ""
for i in range(0, len(input_string), 2):
    even_indexed_chars += input_string[i]
print("Characters at even index positions:", even_indexed_chars)        
 	
