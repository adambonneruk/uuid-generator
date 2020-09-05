import uuid
import sys

def print_uuid(version = 4):
	print(uuid.uuid4())

def generate(version = 4, count = 1):
	#print("")
	#print("function: generatep")
	#print("function version:" + str(version))
	#print("function count:" + str(count))
	#print(uuid.uuid4())s

	for i in range(1, count + 1):
		print_uuid()