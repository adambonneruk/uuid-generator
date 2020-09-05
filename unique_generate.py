import uuid
import sys

def print_uuid(version,urnFlag):

	if urnFlag:
		urnString = "urn:uuid:"
	else:
		urnString = ""

	if version == 0:
		print(urnString + "00000000-0000-0000-0000-000000000000")

	elif version == 1:
		print(urnString + str(uuid.uuid1()))

	elif version == 4:
		print(urnString + str(uuid.uuid4()))

	else:
		print("error")

def generate(version = 4, count = 1, urnFlag = True):
	i = 1
	for i in range(i, count + 1):
		print_uuid(version,urnFlag)