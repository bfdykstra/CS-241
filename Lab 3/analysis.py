#Lab 4
#Author: Ben Dykstra

class StudentRecord:
	def __init__(self):
		self.name = None
		self.grade = None

def FileRead(File):
	for line in File:
		student = line.split()
		int(student[1])
		
		#line = StudentRecord()
		
		#line.name = studentName
		#line.grade = studentGrade
		studentList = []
		studentList.append(student)
	return studentList


def FileSortAlphabetical(studentList):
	studentList.sort()

def FileSortGrade(studentList):
	for i in studentList:
		studentList[i][1].sort()


