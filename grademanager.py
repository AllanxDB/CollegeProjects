
# Class representing a student and their grades
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []     
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def highest(self):
        return max(self.grades) if self.grades else None
    
    def lowest(self):
        return min(self.grades) if self.grades else None
    
    def __str__(self):
        return f"{self.name} | Grades: {self.grades} | Avg: {self.average():.2f}"


# Dictionary mapping student names to Student objects
students = {}

def add_student():
    name = input("Enter student name: ").title()
    
    if name in students:
        print("That student already exists.")
    else:
        students[name] = Student(name)
        print(f"Added {name}!")

def add_grade():
    name = input("Enter student name: ").title()
    
    if name not in students:
        print("Student not found.")
        return
    
    try:
        grade = float(input("Enter grade (0–100): "))
    except ValueError:
        print("Invalid grade.")
        return
    
    students[name].add_grade(grade)
    print(f"Added grade {grade} to {name}.")

def show_student():
    name = input("Enter student name: ").title()
    
    if name in students:
        print(students[name])
    else:
        print("Student not found.")

def list_all_students():
    print("\n--- All Students ---")
    for student in students.values():
        print(student)
    print("---------------------\n")

def menu():
    print("===== Student Grade Manager =====")
    print("1. Add Student")
    print("2. Add Grade to Student")
    print("3. Show Student Info")
    print("4. List All Students")
    print("5. Quit")
    print("===============================")

# Main loop
def main():
    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_grade()
        elif choice == "3":
            show_student()
        elif choice == "4":
            list_all_students()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

# Run the program
if __name__ == "__main__":
    main()
