class Student:
    """
    A class to represent a student with their personal details and academic marks.

    Attributes:
        name (str): The name of the student
        age (int): The age of the student
        mark1 (float): The first subject mark
        mark2 (float): The second subject mark
        mark3 (float): The third subject mark
    """

    def __init__(self, name, age, mark1, mark2, mark3):
        """
        Initialize a Student object with personal and academic details.

        Args:
            name (str): The name of the student
            age (int): The age of the student
            mark1 (float): The first subject mark
            mark2 (float): The second subject mark
            mark3 (float): The third subject mark
        """
        self.name = name
        self.age = age
        self.marks = [mark1, mark2, mark3]

    def display_details(self):
        """Display the student's personal details in a readable format."""
        print(f"Name: {self.name}, Age: {self.age}")

    def calculate_total(self):
        """
        Calculate the total marks of the student.

        Returns:
            float: The sum of all marks
        """
        return sum(self.marks)

    def get_average(self):
        """
        Calculate the average marks of the student.

        Returns:
            float: The average of all marks
        """
        return self.calculate_total() / len(self.marks)


# Example usage
if __name__ == "__main__":
    student1 = Student("Alice Johnson", 20, 85, 90, 88)
    student1.display_details()
    print(f"Total Marks: {student1.calculate_total()}")
    print(f"Average Marks: {student1.get_average():.2f}")
