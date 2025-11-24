import random


three_digits = random.randint(100,999)
tries = 10
print(three_digits)
while tries > 0 and tries <= 10:
    user_input =  input ("Enter a 3  digit number:")
    if len(user_input)==3:
        tries = tries-1 
        if int(user_input) == three_digits:
            print ("correct guess")
            break 
        else:
            print(f"try again you have {tries} left")
    else:
        print (f"Enter 3 digit number you enterd {len(user_input)} digit")
