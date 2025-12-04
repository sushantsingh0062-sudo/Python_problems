# Create a dictionary of 5 students marks and print topper.
students_marks = {
    "Ankit": 85,
    "Banti": 92,
    "Chintu": 78,
    "Dhoni": 90,
    "parth": 88
}
topper = max(students_marks, key=students_marks.get)
print("Topper:", topper, "with marks:", students_marks[topper])
