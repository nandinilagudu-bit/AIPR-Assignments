# AI-generated Student class example

class Student:
    # Constructor to initialize attributes
    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course

    # Method to display student details
    def display_details(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)


# Creating an object of the Student class
student1 = Student("Nandini", 101, "MCA")

# Calling the display method
student1.display_details()
