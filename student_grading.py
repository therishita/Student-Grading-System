
# STUDENT MANAGEMENT AND GRADING SYSTEM

SUBJECTS = ["Physics", "Mathematics", "Chemistry",
            "Computer Science", "English"]

students = {}

# Function to input valid marks
def input_marks(subject):
    while True:
        marks = input("Enter marks in " + subject + " (out of 100): ")
        if marks.replace(".", "", 1).isdigit():
            marks = float(marks)
            if marks >= 0 and marks <= 100:
                return marks
            else:
                print("Invalid marks! Enter marks between 0 and 100.")
        else:
            print("Invalid input! Please enter a valid number.")

# Function to calculate total, percentage and grade
def calculate_result(marks):
    total = sum(marks)
    percentage = total / 5
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    else:
        grade = "F"
    return total, percentage, grade

# Function to add a student
def add_student():
    print("\n--- ADD STUDENT ---")
    roll = input("Enter Roll Number: ").upper()
    if roll == "":
        print("Roll number cannot be empty!")
    elif roll in students:
        print("Roll number already exists!")
    else:
        name = input("Enter Student Name: ").upper()
        if name == "":
            print("Student name cannot be empty!")
        else:
            marks = []
            for subject in SUBJECTS:
                mark = input_marks(subject)
                marks.append(mark)
            students[roll] = {
                "name": name,
                "marks": marks
            }
            print("\nStudent added successfully!")

# Function to display student details
def display_student(roll):
    student = students[roll]
    total, percentage, grade = calculate_result(student["marks"])
    print("\n========== STUDENT REPORT ==========")
    print("Name:", student["name"])
    print("Roll Number:", roll)
    print("------------------------------------")
    for i in range(5):
        print(SUBJECTS[i] + ":", student["marks"][i], "/ 100")
    print("------------------------------------")
    print("Total Marks:", round(total, 2), "/ 500")
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)
    print("====================================")

# Function to view all students
def view_students():
    print("\n--- ALL STUDENT RECORDS ---")
    if len(students) == 0:
        print("No student records available!")
    else:
        for roll in students:
            display_student(roll)

# Function to search for a student
def search_student():
    print("\n--- SEARCH STUDENT ---")
    roll = input("Enter Roll Number: ").upper()
    if roll in students:
        display_student(roll)
    else:
        print("Student not found!")

# Function to edit student marks
def edit_marks():
    print("\n--- EDIT STUDENT MARKS ---")
    roll = input("Enter Roll Number: ").upper()
    if roll not in students:
        print("Student not found!")
    else:
        print("Student Name:", students[roll]["name"])
        print("\nEnter the updated marks:")
        new_marks = []
        for subject in SUBJECTS:
            mark = input_marks(subject)
            new_marks.append(mark)
        students[roll]["marks"] = new_marks
        print("\nAll student marks updated successfully!")
        display_student(roll)

# Function to delete a student
def delete_student():
    print("\n--- DELETE STUDENT ---")
    roll = input("Enter Roll Number: ").upper()
    if roll not in students:
        print("Student not found!")
    else:
        display_student(roll)
        confirm = input("Are you sure you want to delete? (yes/no): ")
        if confirm.lower() == "yes":
            del students[roll]
            print("Student record deleted successfully!")
        else:
            print("Deletion cancelled!")

# MAIN MENU
while True:
    print("\n========================================")
    print("       STUDENT MANAGEMENT SYSTEM")
    print("========================================")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Edit Student Marks")
    print("5. Delete Student")
    print("6. Exit")
    print("========================================")
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        edit_marks()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("\nThank you for using the Student Management System!")
        print("Program terminated.")
        break
    else:
        print("Invalid choice! Please select between 1 and 6.")