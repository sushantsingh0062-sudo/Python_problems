# Check if a given string is a palindrome.
input_string = input("Enter a string: ")
# Remove spaces and convert to lowercase for accurate comparison
cleaned_string = ''.join(input_string.split()).lower()
# Check if the cleaned string is equal to its reverse
if cleaned_string == cleaned_string[::-1]:
    print("The string is a palindrome.")
else:            
    print("The string is not a palindrome.")                                    
