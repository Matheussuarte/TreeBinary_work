from Tree import Tree

class Student:
    def __init__(self, name, registration, course, grade):

        self.name = name
        self.registration = registration
        self.course = course
        self.grade = grade

    def __str__(self):

        return (
            f"Name: {self.name} | "
            f"Registration: {self.registration} | "
            f"Course: {self.course} | "
            f"Grade: {self.grade}"
        )

class System:
    def __init__(self):

        # tree sorted by grade
        self.grades = Tree(lambda student: student.grade)

        # tree sorted by name
        self.names = Tree(lambda student: student.name.lower())

    def register(self):
        name = input("Name: ")
        registration = input("Registration: ")
        course = input("Course: ")
        grade = float(input("Grade: "))

        student = Student(
            name,
            registration,
            course,
            grade
        )

        self.grades.add(student)
        self.names.add(student)

    def rankingHighestToLowest(self):
        print("\nRanking:")
        self.grades.reverseOrder()

    def alphabeticalOrder(self):
        print("\nStudents A-Z:")
        self.names.inOrder()

    def searchByName(self):
        name = input("Student name: ")
        result = self.names.search(
            name.lower()
        )

        if result:
            print(result)
        else:
            print("Student not found")

def menu():
    system = System()

    while True:
        print("""
====== STUDENT MANAGEMENT SYSTEM ======

1 - Register student
2 - Grade ranking
3 - A-Z list
4 - Search student
0 - Exit
""")

        option = input("Option: ")

        if option == "1":
            system.register()

        elif option == "2":
            system.rankingHighestToLowest()

        elif option == "3":
            system.alphabeticalOrder()

        elif option == "4":
            system.searchByName()

        elif option == "0":
            break

menu()