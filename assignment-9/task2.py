class SruStudent:
    # Manual: class to hold student basic info and fee status
    def __init__(self, name, roll_no, hostel_status=False, fees_paid=0.0):
        # Initialize student attributes
        self.name = name                # student's full name
        self.roll_no = roll_no          # roll number / id
        self.hostel_status = hostel_status  # True if in hostel, False otherwise
        self.fees_paid = float(fees_paid)   # total fees paid

    def fee_update(self, amount):
        """Add amount to fees_paid (manual comment)."""
        # Validate amount
        if amount < 0:
            raise ValueError("amount must be non-negative")
        # Update total fees paid
        self.fees_paid += amount

    def display_details(self):
        """Return a formatted string of student details."""
        details = (
            f"Name        : {self.name}\n"
            f"Roll Number : {self.roll_no}\n"
            f"Hostel      : {'Yes' if self.hostel_status else 'No'}\n"
            f"Fees Paid   : {self.fees_paid:.2f}"
        )
        return details

# Example usage
if __name__ == "__main__":
    s = SruStudent("Anita Rao", "CS2025", hostel_status=True, fees_paid=1500)
    s.fee_update(500)
    print(s.display_details())

class SruStudentAI:
    # AI: Represents a student with basic identity and financial attributes.
    def __init__(self, name, roll_no, hostel_status=False, fees_paid=0.0):
        # AI: Store basic identity fields provided by caller.
        self.name = name                # AI: Student's full name for display/records.
        self.roll_no = roll_no          # AI: Unique identifier for the student.
        self.hostel_status = hostel_status  # AI: Boolean flag whether student lives in hostel.
        self.fees_paid = float(fees_paid)   # AI: Monetary value representing fees paid to date.

    def fee_update(self, amount):
        # AI: Ensure the payment amount is valid (non-negative).
        if amount < 0:
            raise ValueError("amount must be non-negative")
        # AI: Increase cumulative fees_paid by the new payment amount.
        self.fees_paid += amount

    def display_details(self):
        # AI: Build a multi-line string that clearly formats the student's data.
        details = (
            f"Name        : {self.name}\n"
            f"Roll Number : {self.roll_no}\n"
            f"Hostel      : {'Yes' if self.hostel_status else 'No'}\n"
            f"Fees Paid   : {self.fees_paid:.2f}"
        )
        # AI: Return the formatted string for UI/CLI display.
        return details

# Example usage
if __name__ == "__main__":
    s_ai = SruStudentAI("Rahul Verma", "EE2101", hostel_status=False, fees_paid=2000)
    s_ai.fee_update(300)
    print(s_ai.display_details())
