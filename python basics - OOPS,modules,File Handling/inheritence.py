class school():

	def __init__(self,name,age):
		self.name=name
		self.age=age
		print("school member class / parent class")
		print("\n")

	def introduce(self):
		print("my name is {} amd age is {}".format(self.name,self.age))


class teacher(school):

	def __init__(self,name,age,salary):
		school.__init__(self,name,age)
		self.salary=salary
		print("teacher member class / child class")

	def introduce(self):
		school.introduce(self)
		print("salary is {}".format(self.salary))

class student(school):

	def __init__(self,name,age,marks):
		school.__init__(self,name,age)
		self.marks=marks
		print("student member class / child class")

	def introduce(self):
		school.introduce(self)
		print("marks is {}".format(self.marks))



t=teacher("ram",40,10000)
t.introduce()

s=student("rishi",20,100)
s.introduce()