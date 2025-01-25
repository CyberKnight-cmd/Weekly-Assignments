marks = int(input("Enter your marks :"))
if(marks>=90):
    grade = 'E'
elif(marks>=80 and marks<90):
    grade = 'A'
elif(marks>=70 and marks<80):
    grade = 'B'
elif(marks>=60 and marks<70):
    grade = 'C'
elif(marks>=50 and marks<60):
    grade = 'D'
elif(marks>=35 and marks<50):
    grade = 'P'
elif(marks<35):
    grade = 'F'
else:
    grade = '!!?'
print("The grade of the student according to %i marks is :"%marks, grade)
