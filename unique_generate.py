import uuid
import sys

def generate(version = 4, count = 1):
	print(uuid.uuid4())
	print(str(version) + " " + str(count))