import json

def addCourse():
    NumberOfAddedCourses = int(input("How many courses are you gonna add: "))

    CoursesGrade = open("Grades.json","r")
    CoursesText = json.load(CoursesGrade)

    i = 1

    while i<=NumberOfAddedCourses:
        length = len(CoursesText["Courses"])
        id = length+1
        name = input("Enter course name:")
        hours = int(input("Enter course hours: "))
        grade = input("Enter course grade: ")
        CoursesText["Courses"].append({"Name":name,"Hours":hours,"Grade":grade,"ID":id})
        i+=1

    JsonFile = open("Grades.json","w")

    dumpingText = json.dumps(CoursesText,indent = 4)

    JsonFile.write(str(dumpingText))
