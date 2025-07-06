def input_student_data():
    """
    Function to collect student information from user input.
    Returns: student name, age, and list of marks
    """
    # Get student's name
    name = input("Enter student name: ")
    
    # Get student's age and convert to integer
    age = int(input(f"Enter age for {name}: "))
    
    # Create empty list to store marks
    marks = []
    
    # Ask how many courses the student has (2 or 3)
    num_courses = int(input(f"How many courses for {name} (2 or 3)? "))
    
    # Loop to collect marks for each course
    for i in range(num_courses):
    # Get mark for each course and convert to decimal number
      mark = float(input(f"Enter mark for course {i+1}: "))
    # Add the mark to our list
        marks.append(mark)
    
    # Return all the collected information
    return name, age, marks

def calculate_average(marks):
    """
    Function to calculate the average of marks.
    Takes a list of marks and returns the average.
    """
    # Add all marks together and divide by number of marks
    return sum(marks) / len(marks)

def display_student_data(student_data):
    """
    Function to display all student information in a neat format.
    Takes the student data dictionary and prints it nicely.
    """
    print("\n--- Student Grades ---")
    
    # Loop through each student in our data
    for name, info in student_data.items():
        print(f"Student: {name}")
        print(f"  Age: {info['age']}")
        print(f"  Marks: {info['marks']}")
        # Show average rounded to 2 decimal places
        print(f"  Average Grade: {info['average']:.2f}")
        print("-" * 30)  # Print a line separator

def student_management():
    """
    Main function that manages the entire student data collection process.
    This is where everything comes together.
    """
    # Create empty dictionary to store all student data
    student_data = {}
    
    # Ask how many students we want to enter
    num_students = int(input("Enter the number of students: "))
    
    # Loop to collect data for each student
    for _ in range(num_students):
        # Get student information using our input function
        name, age, marks = input_student_data()
        
        # Calculate average marks for this student
        avg = calculate_average(marks)
        
        # Store all student info in our dictionary
        # Using student name as the key
        student_data[name] = {
            'age': age,
            'marks': marks,
            'average': avg
        }
    
    # Display all collected student data
    display_student_data(student_data)

# Start the program by calling the main function
student_management()
