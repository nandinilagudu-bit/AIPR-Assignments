# Function to classify a person's age group using nested if-elif-else

def classify_age(age):
    if age < 0:
        print("Invalid age entered.")
    elif age <= 12:
        print("Child")
    elif age <= 19:
        print("Teenager")
    elif age <= 59:
        print("Adult")
    else:
        print("Senior Citizen")

# Example call
classify_age(25)
# Alternate version using nested conditional expressions

def classify_age_short(age):
    category = (
        "Invalid age" if age < 0 else
        "Child" if age <= 12 else
        "Teenager" if age <= 19 else
        "Adult" if age <= 59 else
        "Senior Citizen"
    )
    print(category)

# Example call
classify_age_short(70)
