def get_grade(student_name, grades_dict):
    """Return the grade of the given student."""
    return grades_dict.get(student_name, None)


def average_grade(grades_dict):
    """Return the average grade of all students, rounded to two decimals."""
    if not grades_dict:
        return 0.0
    avg = sum(grades_dict.values()) / len(grades_dict)
    return round(avg, 2)


# --- main program ---
grades = {}

num = int(input("Enter the number of students: "))

for i in range(num):
    name = input(f"Enter student's name: ").strip()
    grade = int(input(f"Enter {name}'s grade: "))
    grades[name] = grade

student_to_check = input("\nEnter the student's name to get their grade: ").strip()
grade_value = get_grade(student_to_check, grades)

print()
if grade_value is not None:
    print(f"{student_to_check}'s grade is {grade_value}")
else:
    print(f"{student_to_check} not found in the list.")

avg = average_grade(grades)
print(f"The average grade is {avg:.2f}")
