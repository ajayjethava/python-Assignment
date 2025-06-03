#  Create a mini-project where students combine conditional statements, loops, and functions
#  to create a basic Python application, such as a simple calculator or a grade management
#  system.




def input_subjects_and_marks():
    subjects = []
    marks = []
    num_subjects = int(input("How many subjects do you want to enter? "))
    
    for i in range(num_subjects):
        subject = input(f"Enter the name of subject {i+1}: ")
        subjects.append(subject)
        while True:
            mark = input(f"Enter marks for {subject} (0-100): ")
            if mark.isdigit() and 0 <= int(mark) <= 100:
                marks.append(int(mark))
                break
            else:
                print("Please enter valid marks between 0 and 100.")
    return subjects, marks

def calculate_average(marks):
    return sum(marks) / len(marks)


def determine_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'


def display_results(subjects, marks, average, grade):
    print("\n--- Grade Report ---")
    for i in range(len(subjects)):
        print(f"{subjects[i]}: {marks[i]}")
    print(f"Average Marks: {average:.2f}")
    print(f"Overall Grade: {grade}")

def main():
    subjects, marks = input_subjects_and_marks()
    average = calculate_average(marks)
    grade = determine_grade(average)
    display_results(subjects, marks, average, grade)


if __name__ == "__main__":
    main()
