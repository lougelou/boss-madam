def check_grade(grade):
    if grade >= 80 and grade <= 100:
        return "You did a great job"
    elif grade >= 70 and grade <= 79:
        return "Keep it up!"
    elif grade >= 60 and grade <= 69:
        return "you passed, but there's a room for improve"
    elif grade <= 59:
        return "Better luck next time"
        
grade = int(input("Enter grade:"))   
print(check_grade(grade))                  