# Input marks of 5 subjects; print total, average, and percentage.
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)
total = sum(marks)
average = total / 5
percentage = (total / 500) * 100  # Assuming each subject is out of
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
print(f"Percentage: {percentage}%")

