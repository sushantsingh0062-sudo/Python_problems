# Input a number; print multiplication table (1–10).
num = int(input("Enter a number: "))
print(f"Multiplication table for {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
    