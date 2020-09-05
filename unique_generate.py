import uuid
import sys

def print_uuid(version,namespace,namespace_value):

	if version == 0:
		print("00000000-0000-0000-0000-000000000000")

	elif version == 1:
		print(uuid.uuid1())

	elif version == 3:
		if namespace == "dns":
			print(uuid.uuid3(uuid.NAMESPACE_DNS, namespace_value))
		elif namespace == "url":
			print(uuid.uuid3(uuid.NAMESPACE_URL, namespace_value))
		elif namespace == "oid":
			print(uuid.uuid3(uuid.NAMESPACE_OID, namespace_value))
		elif namespace == "x500":
			print(uuid.uuid3(uuid.NAMESPACE_X500, namespace_value))
		else:
			print("error - uuid v3 - namespace")

	elif version == 4:
		print(uuid.uuid4())

	elif version == 5:
		if namespace == "dns":
			print(uuid.uuid5(uuid.NAMESPACE_DNS, namespace_value))
		elif namespace == "url":
			print(uuid.uuid5(uuid.NAMESPACE_URL, namespace_value))
		elif namespace == "oid":
			print(uuid.uuid5(uuid.NAMESPACE_OID, namespace_value))
		elif namespace == "x500":
			print(uuid.uuid5(uuid.NAMESPACE_X500, namespace_value))
		else:
			print("error - uuid v5 - namespace")

	else:
		print("error - uuid version")

def generate(version = 4, count = 1, namespace = "url", namespace_value = "http://python.org"):
	i = 1
	for i in range(i, count + 1):
		print_uuid(version,namespace,namespace_value)

'''
The uuid module defines the following namespace identifiers for use with uuid3() or uuid5().
	uuid.NAMESPACE_DNS
		When this namespace is specified, the name string is a fully-qualified domain name.
	uuid.NAMESPACE_URL
		When this namespace is specified, the name string is a URL.
	uuid.NAMESPACE_OID
		When this namespace is specified, the name string is an ISO OID.
	uuid.NAMESPACE_X500
		When this namespace is specified, the name string is an X.500 DN in DER or a text output format.
'''