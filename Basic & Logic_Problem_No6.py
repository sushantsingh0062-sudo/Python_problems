# Swap two variables without using a third variable.
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
a = a + b
b = a - b
a = a - b
print(f"After swapping, a = {a} and b = {b}")
