import json

def editGrade():
    Grades = open("Grades.json","r")

    GradesText = Grades.read()

    GradeDict = json.loads(GradesText)

    CourseArray = GradeDict["Courses"]

    i = int(input("Enter ID of the course you want to edit the grade of: "))
    for Course in CourseArray:
        if Course["ID"] == i:
            print(f'\nName: {Course["Name"]} \nHours: {Course["Hours"]} \nGrade: {Course["Grade"]} \nID: {Course["ID"]}\n')

    gradeVal = input("What is the grade of this course?: ")


    for course in CourseArray:
        if course["ID"] == i:
            course["Grade"] = gradeVal

    JSONffile = open("Grades.json","w")

    JSONffile.write(str(json.dumps(GradeDict, indent=4)))
    