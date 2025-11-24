# Input a string and count vowels, consonants, digits, and spaces.
input_string = input ("Entera string:")
vowels = 0
consonants = 0
ddigit = 0
spaces = 0
for char in input_string:
    if char.isalpha():
        if char.lower() in 'aeiou':
            vowels += 1
        else:
            consonants += 1
    elif char.isdigit():
        ddigit += 1
    elif char.isspace():
        spaces += 1
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {ddigit}")
print(f"Spaces: {spaces}")