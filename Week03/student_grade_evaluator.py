# Program purpose: Validate student scores, calculate the total out of 100, 
# assign a grade, and determine the progression decision.

# 1. Accept inputs
student_name = input("Enter student name: ")

try:
    coursework = float(input("Enter coursework score (out of 30): "))
    exam = float(input("Enter examination score (out of 70): "))
except ValueError:
    print("\nError: Please enter valid numbers for the scores.")
    exit()

# 2 & 3. Validate scores (0-30 for coursework, 0-70 for exam)
if coursework < 0 or coursework > 30:
    print("\nError: Invalid coursework score. Must be between 0 and 30. No result calculated.")
elif exam < 0 or exam > 70:
    print("\nError: Invalid examination score. Must be between 0 and 70. No result calculated.")
else:
    # 4. Calculate total out of 100
    total_score = coursework + exam
    
    # 5. Assign grade (Standard Scheme: A: 70+, B: 60-69, C: 50-59, D: 45-49, E: 40-44, F: <40)
    if total_score >= 70:
        grade = "A"
    elif total_score >= 60:
        grade = "B"
    elif total_score >= 50:
        grade = "C"
    elif total_score >= 45:
        grade = "D"
    elif total_score >= 40:
        grade = "E"
    else:
        grade = "F"
        
    # 6. Display progression decision (Pass if >= 50, Resit required if < 50)
    if total_score >= 50:
        progression = "Pass"
    else:
        progression = "Resit required"
        
    # 7. Display a clear result summary
    print("\n" + "=" * 45)
    print(f" ACADEMIC RESULT SUMMARY: {student_name.upper()} ")
    print("=" * 45)
    print(f"Coursework (Max 30):          {coursework}")
    print(f"Examination (Max 70):         {exam}")
    print(f"Total Score (Max 100):        {total_score}")
    print(f"Assigned Grade:               {grade}")
    print(f"Progression Decision:         {progression}")
    print("=" * 45)
