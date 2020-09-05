import uuid
import sys

def print_uuid(version = 4):

	if version == 0:
		print("00000000-0000-0000-0000-000000000000")

	elif version == 1:
		print(uuid.uuid1())

	elif version == 4:
		print(uuid.uuid4())

	else:
		print("error")

def generate(version = 4, count = 1):
	for i in range(1, count + 1):
		print_uuid(version)