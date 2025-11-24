#  Input a three-digit number and print its reverse.
num = input("Enter a three-digit number: ")
if len(num) == 3 and num.isdigit():
    reversed_num = num[::-1]
    print(f"Reversed number: {reversed_num}")
else:
    print("Please enter a valid three-digit number.")
    
 	
 
 	
