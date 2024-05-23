"""
score: score of the user
grade: string value of the score
grading_block: function to categorise the scores to respective grades
"""
score = int(input("Enter student score: "))


#gradingfunction
def grading_block(score):
    # if block
    if score >= 70 and score <= 100:
        grade = "A"
    elif score >= 60 and score <= 69:
        grade = "B"
    elif score >= 50 and score <= 59:
        grade = "C"
    elif score >= 45 and score <= 49:
        grade = "D"
    elif score >= 40 and score <= 44:
        grade = "E"
    elif score >= 0 and score <= 39:
        grade = "F"
    else:
        print("Wrong Input")
    
    print("The student grade is",grade)

grading_block(score)