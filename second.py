name = str(input("Plese Enter a name: "))
score = int(input("Plese Enter a score: "))
while score >=0:
    if score >=95:
        gpa = "A+"
        break
    if score >=90:
        gpa = "A"
        break
    if score >=85:
        gpa = "B+"
        break
    if score >=80:
        gpa = "B"
        break
    if score >=75:
        gpa = "C+"
        break
    if score >=70:
        gpa = "C"
        break
    if score >=65:
        gpa = "D+"
        break
    if score >=60:
        gpa = "D"
        break
    if score < 60:
        gpa = "F"
        break

print("학생이름:",name,"점수:",score,"학점:",gpa)
#grader("이호창", 99)

# 출력
#학생이름 : 이호창
#점수 : 99점
#학점 : A+
