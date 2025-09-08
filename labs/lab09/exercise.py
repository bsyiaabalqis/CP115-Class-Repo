# Different comparison operators
marks = 85   # Try different values: 100, 0, 75, 60
total_marks = 100
percentage = (marks / total_marks) * 100

print(f"Student scored: {percentage}%")

# Using different comparison operators
if percentage == 100:
    print("Perfect Score! Outstanding achievement!")
elif percentage > 90:
    print("Grade: A+ - Exceptional!")
elif percentage >= 80:
    print("Grade: A - Excellent!")
elif percentage >= 70:
    print("Grade: B - Good!")
elif percentage >= 60:
    print("Grade: C - Satisfactory!")
elif percentage > 0:
    print("Grade: F - Fail, but you tried!")
else:  # percentage == 0
    print("Grade: F - No marks scored!")


# Complete system with boolean logic
marks = 85
total_marks = 100
attendance_percentage = 100
extra_credit = 5  # Bonus points

percentage = (marks / total_marks) * 100
print(f"Student scored: {percentage}%")
print(f"Attendance: {attendance_percentage}%")
print(f"Extra credit: {extra_credit} points")

# Enhanced grading with boolean logic
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Base Grade: {grade}")

# Honor Roll: (Grade A or B) AND perfect attendance
honor_roll = (grade == "A" or grade == "B") and attendance_percentage == 100
print(f"Honor Roll: {'Yes!' if honor_roll else 'No'}")
  
  # Clear grouping with parentheses
if (percentage >= 80) or (extra_credit > 0):
    print("Honor Roll")

student_grade = 95 

if student_grade >= 90:
    print("Excellent performance")

# elif positioning - can have multiple elif statements
student_grade = 85

if student_grade >= 90:
    print("Excellent performance")
elif student_grade >= 80:    # After if
    print("Good performance") 
elif student_grade >= 70:    # After elif
    print("Satisfactory performance")
elif student_grade >= 60:    # After elif
    print("Minimum performance")

# else positioning - always last
student_grade = 65

if student_grade >= 90:
    print("Excellent performance")
elif student_grade >= 80:
    print("Good performance")
elif student_grade >= 70:
    print("Satisfactory performance") 
elif student_grade >= 60:
    print("Minimum performance")
else:                        # Always positioned last
    print("Below minimum performance")

# Multiple independent health checks - use multiple if statements
weight = 70  # kg
height = 1.75  # meters
age = 25
exercise_hours = 2  # per week

bmi = weight / (height * height)

# Each check is independent - multiple can be True
if bmi >= 25:
    print("Recommendation: Consider weight management")
    
if age >= 40:
    print("Recommendation: Schedule regular health checkups")
    
if exercise_hours < 3:
    print("Recommendation: Increase physical activity")
    
if bmi < 18.5:
    print("Recommendation: Consider increasing caloric intake")

# BMI classification - use if-elif-else chain
weight = 60  # kg  
height = 1.75  # meters
bmi = weight / (height * height)

print(f"BMI: {bmi:.1f}")

# Only one classification should apply
if bmi >= 30:
    print("BMI Category: Obese")
elif bmi >= 25:
    print("BMI Category: Overweight")  
elif bmi >= 18.5:
    print("BMI Category: Normal weight")
else:
    print("BMI Category: Underweight")

# Correct: Most specific conditions first
score = 95

if score == 100:
    print("Perfect score!")
elif score >= 90:  
    print("A grade")
elif score >= 80:
    print("B grade")
else:
    print("Below B grade")