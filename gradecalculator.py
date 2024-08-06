def calculate_grade(grades):
    if not grades:
        return None, "No grades provided"
    
    average = sum(grades) / len(grades)
    
    if average >= 95:
        letter_grade = 'A+'
    elif average >= 90:
        letter_grade = 'A'
    elif average >= 85:
        letter_grade =  'B+'
    elif average >= 80:
        letter_grade = 'B'
    elif average >= 75:
        letter_grade =  'C+'
    elif average >= 70:
        letter_grade =  'C'
    elif average >= 65:
        letter_grade =  'D+'
    elif average <= 65:
        letter_grade = 'F'

    return average, letter_grade
    


grades = []
num_grades = int(input("How many grades do you want to enter? "))
    
for num in range(num_grades):
    grade = float(input("Enter 1 grade: "))
    grades.append(grade)
    
average, letter_grade = calculate_grade(grades)

print(f"\n{'Grade Report':^30}")
print(f"{'-' * 30}")
print(f"Number of Grades: {num_grades:>20}")
print(f"Average Grade: {average:>20.2f}")
print(f"Letter Grade: {letter_grade:>20}")