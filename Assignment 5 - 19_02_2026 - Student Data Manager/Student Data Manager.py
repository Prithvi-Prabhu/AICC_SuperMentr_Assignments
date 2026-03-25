def assign_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def main():
    students = {}

    # Input for 5 students
    for i in range(5):
        name = input(f"Enter name of student {i+1}: ")
        marks = float(input(f"Enter marks for {name}: "))
        
        students[name] = {
            "marks": marks,
            "grade": assign_grade(marks)
        }

    # Finding topper
    topper = max(students, key=lambda x: students[x]["marks"])
    
    # Calculating average
    total_marks = sum(student["marks"] for student in students.values())
    average = total_marks / len(students)

    # Output
    print("\n--- Student Details ---")
    for name, details in students.items():
        print(f"{name}: Marks = {details['marks']}, Grade = {details['grade']}")

    print("\n--- Results ---")
    print(f"Topper: {topper} with {students[topper]['marks']} marks")
    print(f"Class Average: {average:.2f}")


if __name__ == "__main__":
    main()