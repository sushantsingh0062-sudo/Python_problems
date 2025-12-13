# Sum of digits of a number using a loop.
num = int (input("Enter a number: "))
sum_digit = 0

while num > 0:
    digits = num % 10 
    sum_digit += digits

    num = num // 10
    print("sum of digits:",sum_digit)