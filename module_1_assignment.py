# Student Grade Management System

# Function to calculate average marks
def calculate_average(marks):
    return sum(marks) / len(marks)

# Function for grade
def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

# Main Program
while True:
    try:
        # Input 5 marks in one line
        marks = list(map(float, input("Enter marks for 5 subjects: ").split()))

        # Check if exactly 5 marks are entered
        if len(marks) != 5:
            print("Please enter exactly 5 marks.")
            continue

        # Validate marks range
        valid = True
        for mark in marks:
            if mark < 0 or mark > 100:
                print("Marks must be between 0 and 100.")
                valid = False
                break

        if not valid:
            continue

        break

    except ValueError:
        print("Please enter numeric values.")

# Calculate average and grade
average = calculate_average(marks)
grade = get_grade(average)

# Display results
print("Average Marks:", round(average, 1))
print("Grade:", grade)