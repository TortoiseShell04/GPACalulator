import calc as GPACalc
import addCourse as aC
import EditGrade as editG

while True:
	choice = int(input("Would you like to calculate GPA (1) or add Courses (2)\nor Edit Grade (3) or Display Courses (4)\nOr Exit (5): "))

	if choice == 1:
		GPACalc.calcGPA()
	elif choice == 2:
		aC.addCourse()
	elif choice == 3:
		editG.editGrade()
	elif choice == 4:
		GPACalc.display()
	else:
		break
