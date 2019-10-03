
if __name__=='__main__':
	#what to do if module run directly
	print("m1 module %s",(__name__))

else:
	#what to do if this module is imported
	print("i am m1, else block")