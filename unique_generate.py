import uuid
import sys

def print_uuid(version = 4):
	if version == 1:
		print("v1")
	elif version == 2:
		print("v2")
	elif version == 3:
		print("v3")
	elif version == 4:
		print(uuid.uuid4())

def generate(version = 4, count = 1):
	for i in range(1, count + 1):
		print_uuid(version)