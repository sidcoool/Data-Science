class dog():

	def __init__(self,pbreed):
		self.breed=pbreed
		self.activities=[]

	def __secretfunc(self):
		print("i am a secret function of {}".format(self.breed))

	def doactivity(self,act):
		self.activities.append(act)

	def showall(self):
		print(self.breed)
		print(self.activities)
		self.__secretfunc()

d1=dog("german shephard")
d2=dog("goldman")

d1.doactivity("jump")
d1.doactivity("roll")

d2.doactivity("catch")
d2.doactivity("not roll")

d1.showall()
d2.showall()

#d1.__secretfunc()  will not work as secretfunc is a private fnction

