#Lab 4
#Author: Ben Dykstra

class _StudentRecord:
	def __init__(self, name, grade):
		self.name = name
		self.grade = grade

	def __str__(self):
		return "%s   %2d" % (self.name, self.grade)

def FileRead(File):
	"""A function that iterates through a file and creates a list of student records for each
	line in the file. Takes in a file as a parameter."""
	
	studentList = []
	line = 0
	
	for line in File:
		line = line.strip() #for empty lines
		if line != "":
						
			student = line.split()
			
			name = student[0] + " " + student[1]
			grade = int(student[2])
			line = _StudentRecord(name, grade)
			
			studentList.append(line)
			
	return studentList


def SortAlphabetical(studentList):
	"""Alphabetically sorts the student records based off of their nam, using an insertion sort 
	algorithm. Takes in a list of student record objects as parameter."""
	
	tempList = studentList[:]
	n = len(tempList)
	for i in range(1,n):
		myValue = tempList[i].name
		studentObject = tempList[i]
		pos = i
		while pos > 0 and myValue < tempList[pos - 1].name:
			tempList[pos] = tempList[pos - 1]
			pos -= 1

		tempList[pos] = studentObject

	return tempList

def SortGrade(studentList):
	"""Alphabetically sorts the student records based off of their grade, using an insertion sort 
	algorithm. Takes in a list of student record objects as parameter."""
	
	tempList = studentList[:]
	n = len(tempList)
	for i in range(1,n):
		
		myValue = tempList[i].grade
		studentObject = tempList[i]
		pos = i
		while pos > 0 and myValue > tempList[pos - 1].grade:
			tempList[pos] = tempList[pos - 1]
			pos -= 1
				
		tempList[pos] = studentObject

	return tempList
	

def RecordWrite(alphaRecord, GradeRecord):
	"""Writes the student's records onto a file with each of their letter grades. Takes in a list
	sorted records as a parameter."""

	outputFile = open("procgrade.txt", "w")
	outputFile.write("Student records by letter grades: \n")
	for i in GradeRecord:
		StudentName = i.name
		#print(StudentName)
		StudentGrade = i.grade
		#print(StudentGrade)
		if StudentGrade < 60:
			outputFile.write("%16s %4d %s \n" % (StudentName, StudentGrade, "F"))
		elif 60 <= StudentGrade < 70:
			outputFile.write("%16s %4d %s \n" % (StudentName, StudentGrade,"D"))
		elif 70 <= StudentGrade < 80:
			outputFile.write("%16s %4d %s \n" % (StudentName, StudentGrade, "C"))
		elif 80 <= StudentGrade < 90:
			outputFile.write("%16s %4d %s \n" % (StudentName, StudentGrade, "B"))
		elif 90 <= StudentGrade :
			outputFile.write("%16s %4d %s \n" % (StudentName, StudentGrade, "A"))

	outputFile.write("\n Student records in alphabetical order: \n")
	for i in alphaRecord:
		StudentName = i.name
		StudentGrade = i.grade
		if StudentGrade < 60:
			outputFile.write("%16s     %2d    F \n" % (StudentName, StudentGrade))
		elif 60 <= StudentGrade < 70:
			outputFile.write("%16s     %2d    D \n" % (StudentName, StudentGrade))
		elif 70 <= StudentGrade < 80:
			outputFile.write("%16s     %2d    C \n" % (StudentName, StudentGrade))
		elif 80 <= StudentGrade < 90:
			outputFile.write("%16s     %2d    B \n" % (StudentName, StudentGrade))
		elif 90 <= StudentGrade :
			outputFile.write("%16s     %2d    A \n" % (StudentName, StudentGrade))


#--------------------------------------------------------------------------------#
#main program

def main():
	inputFile  = open("rawgrade.txt", "r", encoding = "UTF-8")

	AllDuhStudents = FileRead(inputFile)
	
	
	alphabeticalStudents = SortAlphabetical(AllDuhStudents)
	StudentsByGrade = SortGrade(AllDuhStudents)
	
	for i in StudentsByGrade:
		print("%s   %2d" % (i.name, i.grade))
	print()
	for i in alphabeticalStudents:
		print("%s   %2d" % (i.name, i.grade))
	print()
	for i in AllDuhStudents:
		print("%s   %2d" % (i.name, i.grade))
	#write students in alphabetical and grade order to output file 
	RecordWrite(alphabeticalStudents, StudentsByGrade)

	inputFile.close()

main()





