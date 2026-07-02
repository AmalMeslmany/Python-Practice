name = input("Enter student name: ")
grade = int(input("Enter grade: "))

print("Student:", name)
print("Grade:", grade)

if grade >= 90:
    print("Result: Excellent")
elif grade >= 60:
    print("Result: Pass")
else:
    print("Result: Fail")