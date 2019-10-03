class person():

	def __init__(self,pname,clg):
		self.name=pname
		self.college=clg

	def learn(self,subject):
		print("hello {} i am learning {}".format(self.name,subject))
	#	print("my name is {} and i am learning {}".format(self.name,self.subject)

	def intoduce(self):
		print("hello I am {}".format(self.name))
		print("i am from {}".format(self.college))

p= person("rishi","jiit")
p.learn("python")
p.intoduce()