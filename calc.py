import json

def calcGPA():
    Coursesfile = open("Grades.json","r")

    GPAfile = open("GPA.json", "r")
    GradePoint = GPAfile.read()
    SortedGradePoint = json.loads(GradePoint)

    SortedGrades = json.loads(Coursesfile.read())
    TotalHours = 0
    tGPA = 0
    courseGPA = 0
    NAHours = 0

    for Course in SortedGrades["Courses"]:
        print(f'Name: {Course["Name"]} \nHours: {Course["Hours"]} \nGrade: {Course["Grade"]} \nID: {Course["ID"]}\n')
        TotalHours += Course["Hours"]
        for grade in SortedGradePoint["Grades"]:
            if (Course["Grade"] == grade["Name"]):
                courseGPA = grade["Value"]
                break
        if Course["Grade"] == "NA":
                NAHours+= Course["Hours"]
        else:
            tGPA += courseGPA*Course["Hours"]
        
    FinalGPA = tGPA/ (TotalHours-NAHours)

    print(f"GPA : {FinalGPA}")
        
    exitWord = input("Enter anything to exit: ")  

def display():
    Coursesfile = open("Grades.json","r")
    
    SortedGrades = json.loads(Coursesfile.read())
    for Course in SortedGrades["Courses"]:
        print(f'Name: {Course["Name"]} \nHours: {Course["Hours"]} \nGrade: {Course["Grade"]} \nID: {Course["ID"]}\n')

