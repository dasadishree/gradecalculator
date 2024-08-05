def calculate_grade(grades):
    if not grades:
        return "No grades provided"
    
    average = sum(grades) / len(grades)
    
    if average >= 95:
        return 'A+'
    elif average >= 90:
        return 'A'
    elif average >= 85:
        return 'B+'
    elif average >= 80:
        return 'B'
    elif average >= 75:
        return 'C+'
    elif average >= 70:
        return 'C'
    elif average >= 65:
        return 'D+'
    else:
        return 'F'
    
    return average, letter_grade


grades = []
num_grades = int(input("How many grades do you want to enter? "))
    
for num in range(num_grades):
    grade = float(input("Enter 1 grade: "))
    grades.append(grade)
    
average, letter_grade = calculate_grade(grades)
    
print("The average grade is: " + str(average))
print("The letter grade is: " + str(letter_grade))