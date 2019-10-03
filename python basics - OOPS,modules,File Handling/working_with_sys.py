import sys

def add():
	print(int(sys.argv[1])+int(sys.argv[2]))

add()

print(sys.version)
#interpeter will search for packages in these paths
print(sys.path)

print(sys.maxsize)
print(type(sys.stdin))
print(sys.stdout)